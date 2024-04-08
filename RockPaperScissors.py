
import random
import time

def main():
    

    

    Wstreak = 0 #streak counters for replayability
    Lstreak = 0
    Tstreak = 0

    goAgain = ("y") #allows the game to loop
    while goAgain.lower() == "y":
        print("REBOOTING ROBO SHERRIF... beep boop beep...")  #Rock paper scissors just reminds me of a western duel
        time.sleep(3)                                        #All time.sleep functions create a brief delay between lines
        print("CURRENT WINNING STREAK: " + str(Wstreak))
        time.sleep(1)
        print("CURRENT LOSING STREAK: " + str(Lstreak))
        time.sleep(1)
        print("CURRENT TIE STREAK: " + str(Tstreak))
        time.sleep(3)
        robot_list = ['ROCK!', 'PAPER!', 'SCISSORS!']      #Generates the list of options for the script to pick from
        shoot = random.choice(robot_list)                  #Randomizes the robot's choice

        print("ALLLLRIGHHTTTYYY NOW! Pick your fighter!")
        time.sleep(3)

        print("ROCK!, PAPER!, SCISSORS!.... include the exclamation!")
        while True: 
            playIn = input("").upper()
            if playIn not in robot_list: 
                print("you seem to be a little off partner")   #loops until the player picks from the same list, the upper ensures the asnwer isn't case sensitive
            else:
                break


        print('ROCK!')
        time.sleep(1)
        print('PAPER!')
        time.sleep(1)
        print('SCISSORS!')
        time.sleep(1)
        print('SHOOT! *bang bang*')
        time.sleep(0.5)
        print("in the chaos...")
        time.sleep(1)
        print("the dust settles...")
        time.sleep(1)
        print('your opponent stands tall...')
        time.sleep(1)
        print("YOU FOOL!")
        time.sleep(1)
        print("THIS WILL BE YOUR DEMISE! I CHOOSE " + shoot)
        time.sleep(2)
        print("...")
        time.sleep(2)

        #All end events and how the streaks increment 

        if playIn == shoot:
            print("A stand still, you both shall live..")
            Tstreak += 1
            Wstreak = 0 
            Lstreak = 0

        elif playIn == "ROCK!" and shoot == "SCISSORS!" or playIn == "SCISSORS!" and shoot == "PAPER!" or playIn == "PAPER!" and shoot == "ROCK!":
            print("Nice shootin tex... you got me *dies*")
            Wstreak += 1
            Lstreak = 0
            Tstreak = 0

        else:
            print("its over partner... stand down now")
            Lstreak += 1
            Wstreak = 0
            Tstreak = 0

        time.sleep(2)
        print("Another round partner? (y/n)") #provides the option to loop gameplay
        goAgain = input(" ").strip()       #the strip here makes sure that if a y is entetred any extra spaces are removed and the lower case version is extracted by the .lower in the following line

        if goAgain.lower() != "y":
            print("Come again partner... don't be scared to meet your maker..")
            break    #completley ends the program

if __name__ == "__main__":
    main()