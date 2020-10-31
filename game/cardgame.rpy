
init python:

    neighbours = []
    pp = 0
    mp = 0

    import random

    def checkCardToBattle(list, listEnemies):
        if list:
            if list[0] == listEnemies[0]:
                return True

    def setBackground(list, posx, posy, returnAction):

        if list:
            card = list[0]
            if card.owner == 1:
                ui.add(card.picture, xpos = posx, ypos = posy)
            else:
                ui.add(card.picture2, xpos = posx, ypos = posy)
        else:
            ui.imagebutton("img99.png", xpos = posx, ypos = posy, clicked = ui.returns(returnAction))

    class card(object):
        def __init__(self, name, picture, picture2, top, bottom, left, right, position, owner):
            self.name = name
            self.picture = picture
            self.picture2 = picture2
            self.top = top
            self.bottom = bottom
            self.left = left
            self.right = right
            self.position = position
            self.owner = owner



        def artificial(self):
            global number
            number = 1
            while number < 10:
                neighbours = []
                self.position = number
                self.owner = 2
                self.pick_neighbours()
                if self.position == 1 and len(enemies) == 0:
                    self.battle_cardsa1()
                    if len(enemies) == 1:
                        self.position = 1
                        return
                if self.position == 2 and len(enemies) == 0:
                    self.battle_cardsa2()
                    if len(enemies) == 1:
                        self.position = 2
                        return
                if self.position == 3 and len(enemies) == 0:
                    self.battle_cardsa3()
                    if len(enemies) == 1:
                        self.position = 3
                        return
                if self.position == 4 and len(enemies) == 0:
                    self.battle_cardsa4()
                    if len(enemies) == 1:
                        self.position = 4
                        return
                if self.position == 5 and len(enemies) == 0:
                    self.battle_cardsa5()
                    if len(enemies) == 1:
                        self.position = 5
                        return
                if self.position == 6 and len(enemies) == 0:
                    self.battle_cardsa6()
                    if len(enemies) == 1:
                        self.position = 6
                        return
                if self.position == 7 and len(enemies) == 0:
                    self.battle_cardsa7()
                    if len(enemies) == 1:
                        self.position = 7
                        return
                if self.position == 8 and len(enemies) == 0:
                    self.battle_cardsa8()
                    if len(enemies) == 1:
                        self.position = 8
                        return
                if self.position == 9 and len(enemies) == 0:
                    self.battle_cardsa9()
                    if len(enemies) == 1:
                        self.position = 9
                        return

                number += 1

                if number == 9:
                    return

        #def battleBottom(self):
            #if neighbours:
                #if self.get_bottom() > i.get_top():
                    #i.change_owner()

        def battle_cards1(self):
            global neighbours
            for i in neighbours:
                if i is not None and i.owner != self.owner:
                    if i.position == 2:
                        if self.get_right() > i.get_left():
                            i.change_owner()
                    if i.position == 4:
                        if self.get_bottom() > i.get_top():
                            i.change_owner()

        def battle_cards2(self):
            global neighbours
            for i in neighbours:
                if i is not None and i.owner != self.owner:
                    if i.position == 1:
                        if self.get_left() > i.get_right():
                            i.change_owner()
                    if i.position == 3:
                        if self.get_right() > i.get_left():
                            i.change_owner()
                    if i.position == 5:
                        if self.get_bottom() > i.get_top():
                            i.change_owner()

        def battle_cards3(self):
            global neighbours
            for i in neighbours:
                if i is not None and i.owner != self.owner:
                    if i.position == 2:
                        if self.get_left() > i.get_right():
                            i.change_owner()
                    if i.position == 6:
                        if self.get_bottom() > i.get_top():
                            i.change_owner()

        def battle_cards4(self):
            global neighbours
            for i in neighbours:
                if i is not None and i.owner != self.owner:
                    if i.position == 1:
                        if self.get_top() > i.get_bottom():
                            i.change_owner()
                    if i.position == 5:
                        if self.get_right() > i.get_left():
                            i.change_owner()
                    if i.position == 7:
                        if self.get_bottom() > i.get_top():
                            i.change_owner()

        def battle_cards5(self):
            global neighbours
            for i in neighbours:
                if i is not None and i.owner != self.owner:
                    if i.position == 2:
                        if self.get_top() > i.get_bottom():
                            i.change_owner()
                    if i.position == 4:
                        if self.get_left() > i.get_right():
                            i.change_owner()
                    if i.position == 6:
                        if self.get_right() > i.get_left():
                            i.change_owner()
                    if i.position == 8:
                        if self.get_bottom() > i.get_top():
                            i.change_owner()

        def battle_cards6(self):
            global neighbours
            for i in neighbours:
                if i is not None and i.owner != self.owner:
                    if i.position == 3:
                        if self.get_top() > i.get_bottom():
                            i.change_owner()
                    if i.position == 5:
                        if self.get_left() > i.get_right():
                            i.change_owner()
                    if i.position == 9:
                        if self.get_bottom() > i.get_top():
                            i.change_owner()

        def battle_cards7(self):
            global neighbours
            for i in neighbours:
                if i is not None and i.owner != self.owner:
                    if i.position == 4:
                        if self.get_top() > i.get_bottom():
                            i.change_owner()
                    if i.position == 8:
                        if self.get_right() > i.get_left():
                            i.change_owner()

        def battle_cards8(self):
            global neighbours
            for i in neighbours:
                if i is not None and i.owner != self.owner:
                    if i.position == 5:
                        if self.get_top() > i.get_bottom():
                            i.change_owner()
                    if i.position == 7:
                        if self.get_left() > i.get_right():
                            i.change_owner()
                    if i.position == 9:
                        if self.get_right() > i.get_left():
                            i.change_owner()

        def battle_cards9(self):
            global neighbours
            for i in neighbours:
                if i is not None and i.owner != self.owner:
                    if i.position == 6:
                        if self.get_top() > i.get_bottom():
                            i.change_owner()
                    if i.position == 8:
                        if self.get_left() > i.get_right():
                            i.change_owner()

        def change_owner(self):
            global mp
            global pp
            if self.owner == 1:
                self.owner = 2
                mp += 1
                renpy.play("flipping.mp3")
            elif self.owner == 2:
                self.owner = 1
                pp += 1
                renpy.play("flipping.mp3")


        def pick_neighbours(self):
            if self.position == 1:
                if b2:
                    neighbours.append(b2[0])
                if b4:
                    neighbours.append(b4[0])

            if self.position == 2:
                if b1:
                    neighbours.append(b1[0])
                if b3:
                    neighbours.append(b3[0])
                if b5:
                    neighbours.append(b5[0])

            if self.position == 3:
                if b2:
                    neighbours.append(b2[0])
                if b6:
                    neighbours.append(b6[0])

            if self.position == 4:
                if b1:
                    neighbours.append(b1[0])
                if b5:
                    neighbours.append(b5[0])
                if b7:
                    neighbours.append(b7[0])

            if self.position == 5:
                if b2:
                    neighbours.append(b2[0])
                if b4:
                    neighbours.append(b4[0])
                if b6:
                    neighbours.append(b6[0])
                if b8:
                    neighbours.append(b8[0])

            if self.position == 6:
                if b3:
                    neighbours.append(b3[0])
                if b5:
                    neighbours.append(b5[0])
                if b9:
                    neighbours.append(b9[0])

            if self.position == 7:
                if b4:
                    neighbours.append(b4[0])
                if b8:
                    neighbours.append(b8[0])

            if self.position == 8:
                if b5:
                    neighbours.append(b5[0])
                if b7:
                    neighbours.append(b7[0])
                if b9:
                    neighbours.append(b9[0])

            if self.position == 9:
                if b6:
                    neighbours.append(b6[0])
                if b8:
                    neighbours.append(b8[0])

            return neighbours


        def battle_cardsa1(self):
            global neighbours
            for i in neighbours:
                if i is not None and i.owner != self.owner:
                    if i.position == 2:
                        if self.get_right() > i.get_left():
                            if not b1:
                                b1.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return
                    if i.position == 4:
                        if self.get_bottom() > i.get_top():
                            if not b1:
                                b1.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return

        def battle_cardsa2(self):
            global neighbours
            for i in neighbours:
                if i is not None and i.owner != self.owner:
                    if i.position == 1:
                        if self.get_left() > i.get_right():
                            if not b2:
                                b2.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return
                    if i.position == 3:
                        if self.get_right() > i.get_left():
                            if not b2:
                                b2.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return
                    if i.position == 5:
                        if self.get_bottom() > i.get_top():
                            if not b2:
                                b2.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return

        def battle_cardsa3(self):
            global neighbours
            for i in neighbours:
                if i is not None and i.owner != self.owner:
                    if i.position == 2:
                        if self.get_left() > i.get_right():
                            if not b3:
                                b3.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return
                    if i.position == 6:
                        if self.get_bottom() > i.get_top():
                            if not b3:
                                b3.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return

        def battle_cardsa4(self):
            global neighbours
            for i in neighbours:
                if i is not None and i.owner != self.owner:
                    if i.position == 1:
                        if self.get_top() > i.get_bottom():
                            if not b4:
                                b4.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return
                    if i.position == 5:
                        if self.get_right() > i.get_left():
                            if not b4:
                                b4.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return
                    if i.position == 7:
                        if self.get_bottom() > i.get_top():
                            if not b4:
                                b4.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return

        def battle_cardsa5(self):
            global neighbours
            for i in neighbours:
                if i is not None and i.owner != self.owner:
                    if i.position == 2:
                        if self.get_top() > i.get_bottom():
                            if not b5:
                                b5.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return
                    if i.position == 4:
                        if self.get_left() > i.get_right():
                            if not b5:
                                b5.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return
                    if i.position == 6:
                        if self.get_right() > i.get_left():
                            if not b5:
                                b5.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return
                    if i.position == 8:
                        if self.get_bottom() > i.get_top():
                            if not b5:
                                b5.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return

        def battle_cardsa6(self):
            global neighbours
            for i in neighbours:
                if i is not None and i.owner != self.owner:
                    if i.position == 3:
                        if self.get_top() > i.get_bottom():
                            if not b6:
                                b6.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return
                    if i.position == 5:
                        if self.get_left() > i.get_right():
                            if not b6:
                                b6.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return
                    if i.position == 9:
                        if self.get_bottom() > i.get_top():
                            if not b6:
                                b6.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return

        def battle_cardsa7(self):
            global neighbours
            for i in neighbours:
                if i is not None and i.owner != self.owner:
                    if i.position == 4:
                        if self.get_top() > i.get_bottom():
                            if not b7:
                                b7.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return
                    if i.position == 8:
                        if self.get_right() > i.get_left():
                            if not b7:
                                b7.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return

        def battle_cardsa8(self):
            global neighbours
            for i in neighbours:
                if i is not None and i.owner != self.owner:
                    if i.position == 5:
                        if self.get_top() > i.get_bottom():
                            if not b8:
                                b8.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return
                    if i.position == 7:
                        if self.get_left() > i.get_right():
                            if not b8:
                                b8.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return
                    if i.position == 9:
                        if self.get_right() > i.get_left():
                            if not b8:
                                b8.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return

        def battle_cardsa9(self):
            global neighbours
            for i in neighbours:
                if i is not None and i.owner != self.owner:
                    if i.position == 6:
                        if self.get_top() > i.get_bottom():
                            if not b9:
                                b9.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return
                    if i.position == 8:
                        if self.get_left() > i.get_right():
                            if not b9:
                                b9.append(self)
                                enemies.append(self)
                                enemy_deck.remove(self)
                                return

        def get_top(self):
            return self.top

        def get_right(self):
            return self.right

        def get_bottom(self):
            return self.bottom

        def get_left(self):
            return self.left

    def enemy_turn2(c4, c5):
        global luck
        if not c4:
            luck = random.randint(0, (len(enemy_deck)-1))
            c5.append(enemy_deck[luck])
            c4.append(enemy_deck.pop(luck))

    barbarians = card("barbarians","img0.png", "img0a.png", 2,3,2,6, 0, 0)
    barbarians2 = card("barbarians","img0.png", "img0a.png", 2,3,2,6, 0, 0)
    goblins = card("goblins","img1.png", "img1a.png", 1,3,3,5, 0, 0)
    goblins2 = card("goblins","img1.png", "img1a.png", 1,3,3,5, 0, 0)
    archers = card("archers","img2.png", "img2a.png", 4,1,7,6, 0, 0)
    archers2 = card("archers","img2.png", "img2a.png", 4,1,7,6, 0, 0)
    skeletons = card("skeletons","img33.png", "img3a.png", 2,1,3,5, 0, 0)
    skeletons2 = card("skeletons","img33.png", "img3a.png", 2,1,3,5, 0, 0)
    dart_goblin = card("dart_goblin","img4.png", "img4a.png", 2,1,6,1, 0, 0)
    dart_goblin2 = card("dart_goblin","img4.png", "img4a.png", 2,1,6,1, 0, 0)
    mosquetear = card("mosquetear","img5.png", "img5a.png", 6,3,7,2, 0, 0)
    mosquetear2 = card("mosquetear","img5.png", "img5a.png", 6,3,7,2, 0, 0)
    valkyrie = card("valkyrie","img6.png", "img6a.png", 2,7,3,6, 0, 0)
    valkyrie2 = card("valkyrie","img6.png", "img6a.png", 2,7,3,6, 0, 0)
    knight = card("knight","img7.png", "img7a.png", 2,6,3,6, 0, 0)
    knight2 = card("knight","img7.png", "img7a.png", 2,6,3,6, 0, 0)
    baby_dragon = card("baby_dragon","img8.png", "img8a.png", 8,3,8,1, 0, 0)
    baby_dragon2 = card("baby_dragon","img8.png", "img8a.png", 8,3,8,1, 0, 0)

    night_witch = card("night_witch","img9.png", "img9a.png", 10,3,10,1, 0, 0)
    night_witch2 = card("night_witch","img9.png", "img9a.png", 10,3,10,1, 0, 0)
    princess = card("princess","img10.png", "img10a.png", 8,3,10,5, 0, 0)
    princess2 = card("princess","img10.png", "img10a.png", 8,3,10,5, 0, 0)
    mini_pekka = card("mini_pekka","img11.png", "img11a.png", 2,4,4,7, 0, 0)
    mini_pekka2 = card("mini_pekka","img11.png", "img11a.png", 2,4,4,7, 0, 0)
    hog_rider = card("hog_rider","img12.png", "img12a.png", 3,5,6,7, 0, 0)
    hog_rider2 = card("hog_rider","img12.png", "img12a.png", 3,5,6,7, 0, 0)
    mega_knight = card("mega_knight","img13.png", "img13a.png", 4,10,6,7, 0, 0)
    mega_knight2 = card("mega_knight","img13.png", "img13a.png", 4,10,6,7, 0, 0)
    bowler = card("bowler","img14.png", "img14a.png", 1,8,7,7, 0, 0)
    bowler2 = card("bowler","img14.png", "img14a.png", 1,8,7,7, 0, 0)
    minions = card("minions","img15.png", "img15a.png", 4,2,4,3, 0, 0)
    minions2 = card("minions","img15.png", "img15a.png", 4,2,4,3, 0, 0)
    lava_hound = card("lava_hound","im16.png", "img16a.png", 10,8,4,4, 0, 0)
    lava_hound2 = card("lava_hound","img16.png", "img16a.png", 10,8,4,4, 0, 0)
    prince = card("prince","img17.png", "img17a.png", 2,6,3,6, 0, 0)
    prince2 = card("prince","img17.png", "img17a.png", 2,6,3,6, 0, 0)

label cardgame1:

    play music "back_sound.mp3"

    $ enemies = []
    $ allies = []
    $ turn = 0
    $ luck = 0
    $ pp = 0
    $ mp = 0
    $ b1 = []
    $ b2 = []
    $ b3 = []
    $ b4 = []
    $ b5 = []
    $ b6 = []
    $ b7 = []
    $ b8 = []
    $ b9 = []

    $ board = [b1, b2, b3, b4, b5, b6, b7, b8, b9]
    $ deck = []
    $ victory = None
    $ defeat = None
    $ draw = None
    default deck_real = [hog_rider, archers, princess, mosquetear, barbarians, valkyrie, night_witch2]
    default deck_cards = []
    $ number = 0

    python:        # para renovar o deck a cada jogo novo
        for i in deck_real:
            if i not in deck_cards:
                deck_cards.append(i)

    jump cardgamei

label cardgamei:

    call screen deck_choose

    if len(deck) < 5 or len(deck) > 5:

        jump cardgamei

    hide screen deck_choose

    if len(deck) > 4 and len(deck) < 6:
        jump cardgamei2

label cardgamei2:

    $ initiative = 0

    show screen points
    show screen cards_table

    show arena

    $ initiative = random.randint(1, 2)

    if initiative == 1:
        jump arena
    else:
        jump arena6

label arena:

    if turn == 9:
        jump arenafinal

    call screen deck
    # choose the card

    #$ turn += 1

    if _return == "fight":
        jump arena1

label arena1:

    call screen arena
    # show the arena to place the card 1-9

    python:
    # give the card the position, owner and get the neighbours
        x = _return
        board[x - 1].append(allies[0])
        board[x - 1][0].owner = 1
        board[x - 1][0].position = _return
        board[x - 1][0].pick_neighbours()

    jump arena2

label arena2:
# delete the card from the player's deck
    pause 0.7

    python:
        if not allies:
            pass
        else:
            for i in allies:
                for e in deck:
                    if i is e:
                        deck.remove(e)

    jump arena4

label arena4:

    python:
        if b1:
            for i in b1:
                for e in allies:
                    if i is e:
                        i.battle_cards1()
        if b2:
            for i in b2:
                for e in allies:
                    if i is e:
                        i.battle_cards2()
        if b3:
            for i in b3:
                for e in allies:
                    if i is e:
                        i.battle_cards3()
        if b4:
            for i in b4:
                for e in allies:
                    if i is e:
                        i.battle_cards4()
        if b5:
            for i in b5:
                for e in allies:
                    if i is e:
                        i.battle_cards5()
        if b6:
            for i in b6:
                for e in allies:
                    if i is e:
                        i.battle_cards6()
        if b7:
            for i in b7:
                for e in allies:
                    if i is e:
                        i.battle_cards7()
        if b8:
            for i in b8:
                for e in allies:
                    if i is e:
                        i.battle_cards8()
        if b9:
            for i in b9:
                for e in allies:
                    if i is e:
                        i.battle_cards9()

    jump arena5

label arena5:

    pause 1.0

    $ turn += 1
    $ allies = []
    $ neighbours = []
    if turn == 9:
        jump arenafinal

    jump arena6

label arena6:

    pause 1.0

    while len(enemies) == 0:

        python:
            for i in enemy_deck:
                i.artificial()

        if len(enemies) == 0:
            jump arena7

    if enemies:
        $ turn += 1
        jump arena8

    jump arena7

label arena7:

    $ test = 0
    $ neighbours = []

    while len(enemies) == 0:
        $ test = random.randint(1, 9)

        python:
            if test == 1:
                if not b1:
                    c5 = enemies
                    enemy_turn2(b1, c5)
                    for i in b1:
                        for e in enemies:
                            if i is e:
                                i.owner = 2
                                i.position = 1
                                i.pick_neighbours()

            if test == 2:
                if not b2:
                    c5 = enemies
                    enemy_turn2(b2, c5)
                    for i in b2:
                        for e in enemies:
                            if i is e:
                                i.owner = 2
                                i.position = 2
                                i.pick_neighbours()

            if test == 3:
                if not b3:
                    c5 = enemies
                    enemy_turn2(b3, c5)
                    for i in b3:
                        for e in enemies:
                            if i is e:
                                i.owner = 2
                                i.position = 3
                                i.pick_neighbours()

            if test == 4:
                if not b4:
                    c5 = enemies
                    enemy_turn2(b4, c5)
                    for i in b4:
                        for e in enemies:
                            if i is e:
                                i.owner = 2
                                i.position = 4
                                i.pick_neighbours()

            if test == 5:
                if not b5:
                    c5 = enemies
                    enemy_turn2(b5, c5)
                    for i in b5:
                        for e in enemies:
                            if i is e:
                                i.owner = 2
                                i.position = 5
                                i.pick_neighbours()

            if test == 6:
                if not b6:
                    c5 = enemies
                    enemy_turn2(b6, c5)
                    for i in b6:
                        for e in enemies:
                            if i is e:
                                i.owner = 2
                                i.position = 6
                                i.pick_neighbours()

            if test == 7:
                if not b7:
                    c5 = enemies
                    enemy_turn2(b7, c5)
                    for i in b7:
                        for e in enemies:
                            if i is e:
                                i.owner = 2
                                i.position = 7
                                i.pick_neighbours()

            if test == 8:
                if not b8:
                    c5 = enemies
                    enemy_turn2(b8, c5)
                    for i in b8:
                        for e in enemies:
                            if i is e:
                                i.owner = 2
                                i.position = 8
                                i.pick_neighbours()

            if test == 9:
                if not b9:
                    c5 = enemies
                    enemy_turn2(b9, c5)
                    for i in b9:
                        for e in enemies:
                            if i is e:
                                i.owner = 2
                                i.position = 9
                                i.pick_neighbours()

    if enemies:
        $ turn += 1

    jump arena8

label arena8:

    python:
        if (checkCardToBattle(b1, enemies)):
            b1[0].battle_cards1()

        if (checkCardToBattle(b2, enemies)):
            b2[0].battle_cards2()

        if (checkCardToBattle(b3, enemies)):
            b3[0].battle_cards3()

        if (checkCardToBattle(b4, enemies)):
            b4[0].battle_cards4()

        if (checkCardToBattle(b5, enemies)):
            b5[0].battle_cards5()

        if (checkCardToBattle(b6, enemies)):
            b6[0].battle_cards6()

        if (checkCardToBattle(b7, enemies)):
            b7[0].battle_cards7()

        if (checkCardToBattle(b8, enemies)):
            b8[0].battle_cards8()

        if (checkCardToBattle(b9, enemies)):
            b9[0].battle_cards9()

    jump arena9

label arena9:

    $ enemies = []
    $ neighbours = []

    if turn == 9:
        jump arenafinal

    jump arena

label arenafinal:

    play music "menu_song.mp3" fadeout 1.0

    if pp > mp:
        $ victory = True
        "You win!"
        pause 1.0

    elif mp > pp:
        $ defeat = True
        "You lose the game. Try again."
        pause 1.0

    elif mp == pp:
        $ draw = True
        "Draw. Not bad. Try again."
        pause 1.0

    jump arenafinal2

label arenafinal3:
    "You lost the game."
    $ defeat = True
    jump arenafinal2

label arenafinal2:

    hide screen deck
    hide screen cards_table
    hide screen points
    hide screen arena
    hide arena

    stop music fadeout 5.0

    #jump computer
    return

#############################################################################

screen deck:

    grid 2 3:
        xalign 0.95
        yalign 0.1
        spacing 1
        for i in deck:
            imagebutton idle i.picture:
                hover (im.MatrixColor(i.picture, im.matrix.brightness(0.20)))
                action AddToSet(allies, i), Play("sound", "click.ogg"), Return("fight")
        for i in range (len(deck), 6):
            text Null()

screen deck_choose:
    add "grid.png"
    if len(deck) < 5:
        grid 4 4:
            xalign 0.1
            yalign 0.3
            spacing 1
            for i in deck_cards:
                imagebutton:
                    idle i.picture
                    hover (im.MatrixColor(i.picture, im.matrix.brightness(0.35)))
                    action AddToSet(deck, i), Play("sound", "click.ogg"), RemoveFromSet(deck_cards, i) xalign 0.20 yalign 0.20
            for i in range (len(deck_cards), 16):
                text Null()

    vbox:
        xalign 0.8
        yalign 0.4
        grid 3 2:
            for i in deck:
                imagebutton:
                    idle i.picture
                    hover (im.MatrixColor(i.picture, im.matrix.brightness(0.35)))
                    action AddToSet(deck_cards, i), RemoveFromSet(deck, i), Play("sound", "click.ogg") xalign 0.20 yalign 0.20
            for i in range (len(deck), 6):
                text Null()

    vbox:
        xalign 0.9
        yalign 0.65
        if len(deck) == 5:
            frame:
                textbutton _("Done") action Jump("cardgamei2") xpadding 20 ypadding 30

screen cards_table:

    python:
        setBackground(b1, 350, 70, 0)
        setBackground(b2, 510, 70, 0)
        setBackground(b3, 670, 70, 0)
        setBackground(b4, 350, 290, 0)
        setBackground(b5, 510, 290, 0)
        setBackground(b6, 670, 290, 0)
        setBackground(b7, 350, 520, 0)
        setBackground(b8, 510, 520, 0)
        setBackground(b9, 670, 520, 0)

screen points:
    text "Player \n [pp]":
          size 27
          xalign 0.1
          yalign 0.8

    text "Enemy \n [mp]":
          size 27
          xalign 0.1
          yalign 0.7

    vbox:
        xalign 0.1
        yalign 0.95
        frame:
             textbutton _("Give Up") action Jump("arenafinal3") xpadding 20 ypadding 20

screen arena:

    if allies:
        for i in allies:
            add [i.picture]:
                xalign 0.85
                yalign 0.7

    vbox:
        xalign 0.85
        yalign 0.9
        frame:
            textbutton _("Return") action Hide("arena"), RemoveFromSet(allies, i), Jump("arena") xpadding 20 ypadding 30

    python:
        setBackground(b1, 350, 70, 1)
        setBackground(b2, 510, 70, 2)
        setBackground(b3, 670, 70, 3)
        setBackground(b4, 350, 290, 4)
        setBackground(b5, 510, 290, 5)
        setBackground(b6, 670, 290, 6)
        setBackground(b7, 350, 520, 7)
        setBackground(b8, 510, 520, 8)
        setBackground(b9, 670, 520, 9)
