
init python:
    import random

label start:

    #"Let's start"

    $ x = random.randint(1, 3)
    if x == 1:
        $ enemy_deck = [bowler2, skeletons2, mini_pekka2, valkyrie2, baby_dragon2]
    if x ==2:
        $ enemy_deck = [minions2, princess2, hog_rider2, knight2, bowler2]
    else:
        $ enemy_deck = [lava_hound2, archers2, mega_knight2, barbarians2, mosquetear2]

    call cardgame1

    jump computer2

label computer2:

    "Do you want to play again?"
    menu:
        "yes":
            jump start
        "No":
            return
