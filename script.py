def chooseHardLevel():
    global S, X, lastCommandList
    S = "S"
    X = "X"
    lastCommandList = [S, X]
    while True:
        basic.show_string("" + (lastCommandList._pick_random()))
        basic.pause(2000)
        if lastCommandList._pick_random() == S:
            if input.button_is_pressed(Button.AB):
                chooseToPlayHard()
            elif input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
                basic.show_string(X)
                basic.pause(2000)
        elif lastCommandList._pick_random() == X:
            if input.button_is_pressed(Button.AB):
                chooseToExit()
            elif input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
                basic.show_string(S)
                basic.pause(2000)
def chooseToPlayHard():
    global Heart, Diamant, Smiley, Square, LeftTriangle, Giraffe, hardImageList, incorrectChoiceCounter
    Heart = images.icon_image(IconNames.HEART)
    Diamant = images.icon_image(IconNames.DIAMOND)
    Smiley = images.icon_image(IconNames.HAPPY)
    Square = images.icon_image(IconNames.SQUARE)
    LeftTriangle = images.icon_image(IconNames.LEFT_TRIANGLE)
    Giraffe = images.icon_image(IconNames.GIRAFFE)
    hardImageList = [Heart, Diamant, Smiley, Square, LeftTriangle, Giraffe]
    game.set_score(0)
    while True:
        basic.clear_screen()
        basic.show_string("Now it's your turn to choose the images you've seen")
        basic.clear_screen()
        index = 0
        while index <= randint(0, len(hardImageList) - 1):
            hardImageList[index].show_image(0)
            basic.pause(2000)
            index += 1
        if ((hardImageList._pick_random() == Heart and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Square and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Giraffe)):
            if input.button_is_pressed(Button.AB):
                basic.show_string("Correct")
                game.add_score(1)
                if game.score() == 2:
                    basic.show_string("Congratulations!")
                else:
                    index2 = 0
                    while index2 <= randint(0, len(easyImageList) - 1):
                        easyImageList[index2].show_image(0)
                        basic.pause(2000)
                        index2 += 1
        elif ((hardImageList._pick_random() == Heart and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Heart and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Square and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Square and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Square and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Square and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Square and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Square and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Heart and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Giraffe) or 
              (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Heart and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Square and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Square and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Square and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Square and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Square and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Square and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Giraffe) or 
              (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Heart and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Square and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Square and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Square and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Square and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Square and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Square and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Smiley  and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Giraffe) or
              (hardImageList._pick_random() == Square and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Heart and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Square and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Square and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Square and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Square and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Square and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Square and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Square and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Giraffe) or
              (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Heart and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Square and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Square and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Square and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Square and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Square and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Square and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Giraffe) or
              (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Heart and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Heart and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Diamant and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Smiley and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Square and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Square and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Square and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Square and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Square and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Square and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == LeftTriangle and hardImageList._pick_random() == Giraffe) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Heart) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Diamant) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Smiley) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Square) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == LeftTriangle) or (hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Giraffe and hardImageList._pick_random() == Giraffe)):
            if input.button_is_pressed(Button.AB):
                basic.show_string("Incorrect")
                incorrectChoiceCounter = 0
                incorrectChoiceCounter += 1
                if incorrectChoiceCounter >= 2:
                    game.game_over()
                    led.stop_animation()
                else:
                    index3 = 0
                    while index3 <= randint(0, len(easyImageList) - 1):
                        easyImageList[index3].show_image(0)
                        basic.pause(2000)
                        index3 += 1
def chooseEasyLevel():
    global S, X, lastCommandList
    S = "S"
    X = "X"
    lastCommandList = [S, X]
    while True:
        basic.show_string("" + (lastCommandList._pick_random()))
        basic.pause(2000)
        if lastCommandList._pick_random() == S:
            if input.button_is_pressed(Button.AB):
                chooseToPlayEasy()
            elif input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
                basic.show_string(X)
                basic.pause(2000)
        elif lastCommandList._pick_random() == X:
            if input.button_is_pressed(Button.AB):
                chooseToExit()
            elif input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
                basic.show_string(S)
                basic.pause(2000)
def chooseToPlayEasy():
    global Heart, Diamant, Smiley, Square, easyImageList, incorrectChoiceCounter
    Heart = images.icon_image(IconNames.HEART)
    Diamant = images.icon_image(IconNames.DIAMOND)
    Smiley = images.icon_image(IconNames.HAPPY)
    Square = images.icon_image(IconNames.SQUARE)
    easyImageList = [Heart, Diamant, Smiley, Square]
    game.set_score(0)
    while True:
        index4 = 0
        while index4 <= len(easyImageList) - 1:
            easyImageList[index4].show_image(0)
            basic.pause(2000)
            index4 += 1
        basic.clear_screen()
        basic.show_string("Now it's your turn to choose the images you've seen")
        basic.clear_screen()
        index5 = 0
        while index5 <= randint(0, len(easyImageList) - 1):
            easyImageList[index5].show_image(0)
            basic.pause(2000)
            index5 += 1
        if ((easyImageList._pick_random() == Heart and easyImageList._pick_random() == Diamant) or (easyImageList._pick_random() == Diamant and easyImageList._pick_random() == Smiley) or (easyImageList._pick_random() == Smiley and easyImageList._pick_random() == Square)):
            if input.button_is_pressed(Button.AB):
                basic.show_string("Correct")
                game.add_score(1)
                if game.score() == 2:
                    basic.show_string("Congratulations!")
                else:
                    index6 = 0
                    while index6 <= randint(0, len(easyImageList) - 1):
                        easyImageList[index6].show_image(0)
                        basic.pause(2000)
                        index6 += 1
        elif ((easyImageList._pick_random() == Heart and easyImageList._pick_random() == Heart) or (easyImageList._pick_random() == Heart and easyImageList._pick_random() == Smiley) or (easyImageList._pick_random() == Heart and easyImageList._pick_random() == Square) or (easyImageList._pick_random() == Diamant and easyImageList._pick_random() == Diamant) or (easyImageList._pick_random() == Diamant and easyImageList._pick_random() == Heart) or (easyImageList._pick_random() == Diamant and easyImageList._pick_random() == Square) or (easyImageList._pick_random() == Smiley and easyImageList._pick_random() == Smiley) or (easyImageList._pick_random() == Smiley and easyImageList._pick_random() == Heart) or (easyImageList._pick_random() == Smiley and easyImageList._pick_random() == Diamant) or (easyImageList._pick_random() == Square and easyImageList._pick_random() == Square) or (easyImageList._pick_random() == Square and easyImageList._pick_random() == Diamant) or (easyImageList._pick_random() == Square and easyImageList._pick_random() == Smiley)):
            if input.button_is_pressed(Button.AB):
                basic.show_string("Incorrect")
                incorrectChoiceCounter = 0
                incorrectChoiceCounter += 1
                if incorrectChoiceCounter >= 2:
                    game.game_over()
                    led.stop_animation()
                else:
                    index7 = 0
                    while index7 <= randint(0, len(easyImageList) - 1):
                        easyImageList[index7].show_image(0)
                        basic.pause(2000)
                        index7 += 1                
def chooseTheDifficultyLevel():
    global E, H, secondCommandsList
    E = "E"
    H = "H"
    secondCommandsList = [E, H]
    while True:
        basic.show_string("" + (secondCommandsList._pick_random()))
        basic.pause(2000)
        if secondCommandsList._pick_random() == E:
            if input.button_is_pressed(Button.AB):
                chooseEasyLevel()
            elif input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
                basic.show_string(H)
                basic.pause(2000)
        elif secondCommandsList._pick_random() == H:
            if input.button_is_pressed(Button.AB):
                pass
            elif input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
                basic.show_string(E)
                basic.pause(2000)
def chooseToExit():
    basic.show_string("Bye")
    led.stop_animation()
secondCommandsList: List[str] = []
H = "H"
E = "E"
incorrectChoiceCounter = 0
easyImageList: List[Image] = []
hardImageList: List[Image] = []
Giraffe: Image = None
LeftTriangle: Image = None
Square: Image = None
Smiley: Image = None
Diamant: Image = None
Heart: Image = None
lastCommandList: List[str] = []
S = "S"
X = "X"
D = "D"
X = "X"
firstCommandsList = [D, X]
while True:
    basic.show_string("" + (firstCommandsList._pick_random()))
    basic.pause(2000)
    if firstCommandsList._pick_random() == X:
        if input.button_is_pressed(Button.AB):
            chooseToExit()
        elif input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
            basic.show_string(D)
            basic.pause(2000)
    elif firstCommandsList._pick_random() == D:
        if input.button_is_pressed(Button.AB):
            chooseTheDifficultyLevel()
        elif input.button_is_pressed(Button.A) or input.button_is_pressed(Button.B):
            basic.show_string(X)
            basic.pause(2000)
