
import random
import time

def main():

    


    VARboard = ["*", "*", "*", "*", "*", "*", "*", "*", "*"] #initializes an empty board

    def MakeBoard():
        print(VARboard[0] + "|" + VARboard[1] + "|" + VARboard[2] + "\n-----\n" + VARboard[3] + "|" + VARboard[4] + "|" + VARboard[5] + "\n-----\n" + VARboard[6] + "|" + VARboard[7] + "|" + VARboard[8]) #prints the board


    Wstreak = 0 
    Lstreak = 0
    Tstreak = 0
    goAgain = ("y") #streak counter/loop maker
    while goAgain.lower() == "y":
        VARboard = ["*", "*", "*", "*", "*", "*", "*", "*", "*"] #makes sure board starts empty

        print("REBOOTING Tic Tac Toe Wizard beep boop beep...")
        time.sleep(3)
        print("CURRENT WINNING STREAK: " + str(Wstreak))
        time.sleep(1)
        print("CURRENT LOSING STREAK: " + str(Lstreak))
        time.sleep(1)
        print("CURRENT TIE STREAK: " + str(Tstreak), "\n")
        time.sleep(3)
        
        print("\nWELCOME TO MY WONDEROUS WIZARD CAVE!\nTry me in tic tac toe...\nwho will go first? Me or You?") #you can switch up who will play first but you are always X
            
        while True: 
            firstTurn = input("").upper()
            if firstTurn == "ME":
                print("\nAlright.. you're X")
                break
            elif firstTurn == "YOU":
                print("\nI'll be going first")
                break
            else:
                print ("\nplease input exactly Me or You")
        
        print("select a difficulty: smart as rocks(1) or dullest tool in the shed(2)! Enter a 1 or 2.") #I tried to make a second difficulty that would make decisions based on what you do in a very simple manner. It always starts in the center for added difficulty
            
        while True: 
            difficulty = input("")
            if difficulty == "1":
                print("\nI'm picking at random!")
                dif = 1
                break
            elif difficulty == "2":
                print("\nI'll be using some strategy!") #bro is capping so hard rn
                dif = 2
                break
            else:
                print ("\nplease input exactly 1 or 2")

        print("Do you know my rules??(y/n)") 

        while True: 
            tutorial = input("").upper()
            if tutorial == "Y":
                print("\nLet's get to it then!")
                break
            elif tutorial == "N":
                while True: 
                    print("\nSo we'll alternate turns. The board is labled 1, 2, 3 across the top. 4, 5, 6 across the middle. 7, 8, 9 across the bottom. The board looks like this: ")
                    time.sleep(5)
                    print("1|2|3\n-----\n4|5|6\n-----\n7|8|9")
                    time.sleep(3)
                    print("The board will refresh every turn, to select a location type the corresponding lable into the input selector! First to three in a row in any direction wins.")
                    time.sleep(7) 
                    print("Onto the battlefield!") #briefely explains how the board is layed out in case it is confusing on what corresponds to what
                    time.sleep(3)
                    break
                break
            else:
                print ("\nplease input exactly Y or N")

        record = 0
        turn = 1
        gameOver = False 
            
                        

        def WizardTalk(): #I thought it'd be funny if the wizard said different phrases before moving to give him more personality
            WizardPhrases = ["I CAST FIREBALL UPON ", "I BET YOU NEVER SAW ", "I ENCHANT ", "YOU WOULDNT MIND IF I TOOK ", "I HAVE SLAIN MANY A FOE WITH THIS MOVE: ", "I SUMMON ", "LIGHTNIGHT BOLT UPON ", "BY MERLIN'S BEARD I WILL HAVE "]
            phraseOfThePlay = random.choice(WizardPhrases)
            if dif == 1:
                while True:
                    WizardPlay = random.randint(0, len(VARboard)-1) #these are the settings for difficulty "easy". Just randomly assigns the wizard's move
                    if VARboard[WizardPlay] == "*":
                        VARboard[WizardPlay] = "O"
                        print(phraseOfThePlay, WizardPlay+1)
                        MakeBoard()
                        print("\n")
                        break
            else:
                while True: 
                    if turn == 1:   #so if you select difficulty 2 the wizard's first move is always the middle unless its selected
                        WizardPlay = 4
                        if VARboard[WizardPlay] == "*":
                            VARboard[WizardPlay] = "O"
                            print(phraseOfThePlay, WizardPlay+1)
                            MakeBoard()
                            print("\n")
                            record = WizardPlay 

                            break
                    else: 
                        record = (VARboard.index == "X") #records a recent x input, I wasn't sure how to take the exact most recent user input so this just finds the earliest one its kind of funny bc it will successfully play a -1 which puts a O on 10
                        if VARboard[record+1] == "*":
                            VARboard[record+1] = "O"
                            print(phraseOfThePlay, record+2)
                            MakeBoard()
                            print("\n")
                            break
                        elif VARboard[record-1] == "*":
                            VARboard[record-1] = "O"
                            if record := -1:
                                record = 10 #As mentioned 10 turns into 0 which then subtracts to -1. This code is a sly work around.
                            print(phraseOfThePlay, record-1)
                            MakeBoard()
                            print("\n")
                            break 
                        else: # This was intended to make it so the program had the possibility of picking around itself. I origonally intended for the program to check if there was an empty space in front of it and to loop on a row/collumn/diagnol to attempt to score better.
                            # This was alot more difficult to do than I thought it would be. Checking for the win condition itself has been its own pain in the butt. The origonal code would just straight pave over the user input which was pretty funny but unintentional. 
                            WizardPlay = random.randint(0, len(VARboard)-1)
                            if VARboard[WizardPlay] == "*":
                                VARboard[WizardPlay] = "O"
                                print(phraseOfThePlay, WizardPlay+1)
                                MakeBoard()
                                print("\n")
                                break
        
        
        def PlayerGoes(): 
            while True:
                playerIN = int(input("Slect a position to play: "))
                if playerIN >= 1 and playerIN <=9 and VARboard[playerIN-1] == "*": #This is the play input, it turns the users input into an integer so that it can then index the board to tell if the desired space is empty or not. If it's empty it will place a X on the space. 
                    VARboard[playerIN-1] = "X"
                    MakeBoard()
                    print("\n")
                    break
                else:
                    print("Enter a valid position")

        Cwon = False
        Pwon = False

        while gameOver == False and firstTurn == "ME":
            MakeBoard()
            print("\n")
            PlayerGoes()
            if (VARboard[0] == VARboard[1] == VARboard[2] and VARboard[1]!= "*") or (VARboard[3] == VARboard[4] == VARboard[5] and VARboard[3]!= "*") or (VARboard[6] == VARboard[7] == VARboard[8] and VARboard[6]!= "*"):
                gameOver = True
                Pwon = True
                break
            if (VARboard[0] == VARboard[4] == VARboard[8] and VARboard[0]!= "*") or (VARboard[2] == VARboard[4] == VARboard[6]  and VARboard[2]!= "*"):
                gameOver = True
                Pwon = True
                break
            if (VARboard[0] == VARboard[3] == VARboard[6] and VARboard[0]!= "*") or (VARboard[1] == VARboard[4] == VARboard[7] and VARboard[1]!= "*") or (VARboard[2] == VARboard[5] == VARboard[8] and VARboard[2]!= "*"):
                gameOver = True
                Pwon = True
                break
            if "*" not in VARboard:
                gameOver = True
                Cwon = False
                Pwon = False
                break
            turn += 1 
            time.sleep(3)
            WizardTalk()
            if (VARboard[0] == VARboard[1] == VARboard[2] and VARboard[1]!= "*") or (VARboard[3] == VARboard[4] == VARboard[5] and VARboard[3]!= "*") or (VARboard[6] == VARboard[7] == VARboard[8] and VARboard[6]!= "*"):
                gameOver = True
                Cwon = True
                break
            if (VARboard[0] == VARboard[4] == VARboard[8] and VARboard[0]!= "*") or (VARboard[2] == VARboard[4] == VARboard[6]  and VARboard[2]!= "*"):
                gameOver = True
                Cwon = True
                break
            if (VARboard[0] == VARboard[3] == VARboard[6] and VARboard[0]!= "*") or (VARboard[1] == VARboard[4] == VARboard[7] and VARboard[1]!= "*") or (VARboard[2] == VARboard[5] == VARboard[8] and VARboard[2]!= "*"):
                gameOver = True
                Cwon = True
                break
            if "*" not in VARboard:
                gameOver = True
                Cwon = False
                Pwon = False
                break
        
        while gameOver == False and firstTurn == "YOU":
            MakeBoard()
            print("\n")
            time.sleep(3)
            WizardTalk()
            if (VARboard[0] == VARboard[1] == VARboard[2] and VARboard[1]!= "*") or (VARboard[3] == VARboard[4] == VARboard[5] and VARboard[3]!= "*") or (VARboard[6] == VARboard[7] == VARboard[8] and VARboard[6]!= "*"):
                gameOver = True
                Cwon = True
                break
            if (VARboard[0] == VARboard[4] == VARboard[8] and VARboard[0]!= "*") or (VARboard[2] == VARboard[4] == VARboard[6] and VARboard[2]!= "*"):
                gameOver = True
                Cwon = True
                break
            if (VARboard[0] == VARboard[3] == VARboard[6] and VARboard[0]!= "*") or (VARboard[1] == VARboard[4] == VARboard[7] and VARboard[1]!= "*") or (VARboard[2] == VARboard[5] == VARboard[8] and VARboard[2]!= "*"):
                gameOver = True
                Cwon = True
                break
            if "*" not in VARboard:
                gameOver = True
                Cwon = False
                Pwon = False
                break
            turn += 1
            PlayerGoes()
            if (VARboard[0] == VARboard[1] == VARboard[2] and VARboard[1]!= "*") or (VARboard[3] == VARboard[4] == VARboard[5] and VARboard[3]!= "*") or (VARboard[6] == VARboard[7] == VARboard[8] and VARboard[6] != "*"):
                gameOver = True
                Pwon = True
                break
            if (VARboard[0] == VARboard[4] == VARboard[8] and VARboard[0]!= "*") or (VARboard[2] == VARboard[4] == VARboard[6]  and VARboard[2]!= "*"):
                gameOver = True
                Pwon = True
                break
            if (VARboard[0] == VARboard[3] == VARboard[6] and VARboard[0]!= "*") or (VARboard[1] == VARboard[4] == VARboard[7] and VARboard[1]!= "*") or (VARboard[2] == VARboard[5] == VARboard[8] and VARboard[2]!= "*"): 
                gameOver = True
                Pwon = True
                break
            if "*" not in VARboard:
                gameOver = True
                Cwon = False
                Pwon = False
                breakme

        if gameOver == True and Pwon == True: 
            Wstreak += 1
            Lstreak = 0
            Tstreak = 0
            print("You've beaten me... I shall return to my spire to ponder this(y/n)")
            time.sleep(2)
            print("unless you'd like another??")

        if gameOver == True and Cwon == True:
            Lstreak += 1
            Wstreak = 0
            Tstreak = 0
            print("I pity you foolish mortal... a shame! Maybe face me agin some time? (y/n)")
        
        if gameOver == True and Cwon == False and Pwon == False:
            Tstreak += 1
            Wstreak = 0
            Lstreak = 0
            print("Ahh.. but a tie.. how shamefull.. Clearly we fight with our wits! How about another? (y/n)")
        
        goAgain = input(" ").strip()       #the strip here makes sure that if a y is entetred any extra spaces are removed and the lower case version is extracted by the .lower in the following line

        if goAgain.lower() != "y":
            print("Alas.. maybe our intellectual bout was not meant to be!")
            break    #completley ends the program
        

if __name__ == "__main__":
    main()        