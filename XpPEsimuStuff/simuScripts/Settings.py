from os import environ

session_configs= [
    dict(
        name='guess_two_thirds',
        display_name='Guees 2/3 of the Average',
        app_sequence=["guess_two_thirds","payment_info"],
        num_demo_participants=3
    ),
    dict( name='survey',app_sequence=["guess_two_thirds","payment_info"],num_demo_participants=1
         ),
    dict(name='trust',
         display_name="Trust game",
         app_sequence=["Trust"],
         num_demo_participants=2),
]