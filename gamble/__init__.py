from otree.api import *
import numpy as np

doc = """
Iowa Gambling Task. See: "Insensitivity to future consequences following damage to human prefrontal cortex"
(Bechara et al, 1994)
"""


class C(BaseConstants):
    NAME_IN_URL = 'gamble'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 5

    # randomization is done within a block of 10 trials, see figure 1 of the 1994 paper
    BLOCK_SIZE = 10
    NUM_BLOCKS = 10

    # should be greater than block_size * num_blocks
    NUM_TRIALS = 50# in the classic game it is 100

    # these are the rewards for each deck, which are constant
    REWARDS = [
        np.random.randint(0, 10),  
        np.random.randint(0, 10), 
        np.random.randint(0, 10), 
        np.random.randint(0, 10)]
    var = [
        np.random.randint(0, 2.5),  
        np.random.randint(0, 10 ), 
        np.random.randint(0, 2.0), 
        np.random.randint(0, 8.0)]
    

class Subsession(BaseSubsession):
    pass


# def generate_block():
# import random

# rewards = [[150, 200, 250, 300, 350], [1250], [50, 50, 50, 50, 50], [250]]
# for ele in rewards:
# add zeroes until it has 10 elements
# ele += [0] * (C.BLOCK_SIZE - len(ele))
# random.shuffle(ele)
# return rewards


def creating_session(subsession: Subsession):
    # session = subsession.session
    import random

    # rewards = [[], [], [], []]
    # for i in range(C.NUM_BLOCKS):
    # block = generate_block()
    # rewards[0] += block[0]
    # rewards[1] += block[1]
    # rewards[2] += block[2]
    # rewards[3] += block[3]

    # session.gamble_rewards = rewards

    for p in subsession.get_players():
        deck_layout = ['A', 'B', 'C', 'D']
        random.shuffle(deck_layout)
        p.deck_layout = ''.join(deck_layout)


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # how many they have selected from each deck
    num0 = models.IntegerField(initial=0)
    num1 = models.IntegerField(initial=0)
    num2 = models.IntegerField(initial=0)
    num3 = models.IntegerField(initial=0)
    num_trials = models.IntegerField(initial=0)
    deck_layout = models.StringField()
    isleader = models.BooleanField(initial=False)



def inc(deck):
    import random as rd
    return rd.gauss(C.REWARDS[deck],C.var[deck])

def live_method(player: Player, data):
    import math as m
    my_id = player.id_in_group

    session = player.session
    # data will contain A, B, C, D

    # guard
    if player.num_trials == C.NUM_TRIALS:
        return {my_id: dict(finished=True)}

    resp = {}
    if 'letter' in data:
        letter = data['letter']
        deck = player.deck_layout.index(letter)
        field_name = 'num{}'.format(deck)
        cur_count = getattr(player, field_name)
        reward = m.floor(inc(deck)) #C.REWARDS[deck]  # session.gamble_rewards[deck][cur_count]  #
        # cost = session.iowa_costs[deck][cur_count]
        payoff = reward  # - cost
        player.payoff += payoff
        cur_count += 1
        setattr(player, field_name, cur_count)
        player.num_trials += 1
        resp.update(reward=reward)

    if player.num_trials == C.NUM_TRIALS:
        resp.update(finished=True)

    resp.update(cum_payoff=player.payoff, num_trials=player.num_trials)

    return {my_id: resp}


class Play(Page):
    live_method = live_method


class Results(Page):
    @staticmethod
    def before_next_page(player, timeout_happened):
        subsession = player.subsession
        players = subsession.get_players()

        results = []
        
        for p in players:
            #print("Player group:" + str(p.id_in_group) + " Player Id in group:" + str(p.id_in_group) + " Player PayOff:" + str(p.payoff))
            dictionary = { "PlayerId": p.id_in_group, "PayOff":p.payoff}
            results.append(dictionary)
               
        results.sort(key = lambda x:x['PayOff'], reverse=True)
       
        '''for s in results:
           print (s)
        '''
        print("Player Number:", len(players))
        nbLeaders = len(players)/4 # must be NBPLAYER/PLAYERS_PER_GROUP of the next task, how to get it?
       
        for p in players:
            p.participant.vars["isLeader"] = False
            p.isleader = False
            i=0
            while i < nbLeaders:
                #print("result;",results[i]['PlayerId'])
                if(p.id_in_group == results[i]['PlayerId']):
                    p.participant.vars["isLeader"] = True
                    p.isleader = True
                    break
                i+=1
   
class WaitToPlay(WaitPage):
    pass

page_sequence = [Play, Results, WaitToPlay]
