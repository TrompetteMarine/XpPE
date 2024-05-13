from otree.api import *


doc = """
Voting.
"""


class C(BaseConstants):
    NAME_IN_URL = 'live_coordination'
    PLAYERS_PER_GROUP = 4
    NUM_ROUNDS = 10
    MAX_POINTS = 5
    CHOICES = [0, 1]
    MAJORITY = PLAYERS_PER_GROUP#int(PLAYERS_PER_GROUP / 2) + 1


class Subsession(BaseSubsession):

    pass

#def creating_session(subsession: Subsession):
#    for g in subsession.get_groups():
#       for p in g.get_players():
#           print("Player group:" + str(p.id_in_group) + " Player Id in group:" + str(p.id_in_group) + " Player PayOff:" + str(p.payoff))


class Group(BaseGroup):
    contribution = models.CurrencyField()
    count = models.IntegerField(initial=0)


class Player(BasePlayer):
    vote = models.IntegerField()
    isleader = models.BooleanField(initial=False)
    realId = models.IntegerField()


# PAGES
class Coordinate(Page):
    @staticmethod
    def js_vars(player: Player):
        return dict(my_id=player.id_in_group, leader=player.isleader)

    @staticmethod
    def live_method(player: Player, data):
        group = player.group

        if 'vote' in data:
            try:
                vote = int(data['vote'])
            except Exception:
                print('Invalid message received', data)
                return
            if not vote in C.CHOICES:
                print('Invalid message received', data)
                return
            player.vote = vote
        players = group.get_players()

        #tallies = {vote: 0 for vote in C.CHOICES}
        votes = []
         
        group.count = 0
        for p in players:
            vote = p.field_maybe_none('vote')
            print("vote is", vote)
            if vote is not None:
                votes.append([p.id_in_group, vote])
                group.count +=1
                print("Group Count is:",  group.count)
                if  group.count == 4:
                    group.contribution = vote
                    return {0: dict(finished=True)}

        # if you don't want to show who voted, use 'tallies' instead of 'votes'.
        return {0: dict(votes=votes)}

    @staticmethod
    def is_displayed(player: Player):
        """Skip this page if a deal has already been made"""
        group = player.group
        contribution = group.field_maybe_none('contribution')
        return contribution is None

    @staticmethod
    def error_message(player: Player, values):
        group = player.group
        # anti-cheating measure
        if group.field_maybe_none('contribution') is None:
            return "Not done with this page"


class Results(Page):
   pass

class ShuffleWaitPage(WaitPage):

    wait_for_all_groups = True
    @staticmethod
    def after_all_players_arrive(subsession):
        print("Shuffle Start")

        #get participant status
        players = subsession.get_players()
        tmpPlayers = []

        for p in players:
            print("player:", p )
            print("vars:", p.participant.vars )
            print("player id:" + str(p.id_in_group) + " Is Leader:" + str(p.participant.vars['isLeader']))
            print("participan id", p.participant.id)
            print("participan:", p.participant)
            p.isleader = False
            if p.participant.vars['isLeader'] == True :
                 p.isleader = True
            
            dictionary = { "PlayerId": p.participant.id, "IsLeader":p.isleader, "absvalue": 0}
            tmpPlayers.append(dictionary)
                
        tmpPlayers.sort(key = lambda x:x['PlayerId'], reverse=False)
        base=tmpPlayers[0]["PlayerId"]-1

        for p in tmpPlayers:
            p["absvalue"]=p["PlayerId"]-base

        tmpPlayers.sort(key = lambda x:x['IsLeader'], reverse=True)
        
        print("sorted players:", tmpPlayers)

        nbgroup = int(len(tmpPlayers) / C.PLAYERS_PER_GROUP)

        print("nbgroup", nbgroup)

        newmatrix=[]
        for g in range(0,nbgroup):
            print("creating group:", g) #currently g is not the real group number?,but it works as here is act as a counter...
            val=[]
            val.append(tmpPlayers[g]["absvalue"])
            
            for p in range(0, C.PLAYERS_PER_GROUP-1):
                
                offset = nbgroup+p+g*(C.PLAYERS_PER_GROUP-1)

                print("offset:", offset)
                val.append(tmpPlayers[offset]["absvalue"])

            print("val:", val)
            newmatrix.append(val)

        subsession.set_group_matrix(newmatrix) 

        #shuffle group

class Anim(WaitPage):
    template_name = 'canvas.html'

class WaitToPlay(WaitPage):
    pass

page_sequence = [ShuffleWaitPage, Coordinate, Results, WaitToPlay]