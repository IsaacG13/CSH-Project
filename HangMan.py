import random
import time

def main():  

    def hangTheMan(numTurns): #I copy/pasted this section from code I found online. The previous way I was attempting to set this up was too visually confusing.
                            #Sets up the death sequence 
        stages = [ 
                    """
                        -------
                        |      |
                        |      O
                        |   ~~~|~~~
                        |      |
                        |     / \
                        |
                       _|___
                    """,
                    
                    """
                        -------
                        |      |
                        |      O
                        |   ~~~|~~~
                        |      |
                        |     / 
                        |
                       _|___
                    """,
                
                    """
                        -------
                        |      |
                        |      O
                        |   ~~~|~~~
                        |      |
                        |      
                        |
                       _|___
                    """,
                    
                    """
                        -------
                        |      |
                        |      O
                        |   ~~~|
                        |      |
                        |     
                        |
                       _|___
                    """,
                    
                    """
                        -------
                        |      |
                        |      O
                        |      |
                        |      
                        |
                        |
                       _|___
                    """,
                    
                    """
                        -------
                        |      |
                        |      O
                        |  
                        |      
                        |     
                        |
                       _|___
                    """,
                
                    """
                        -------
                        |      |
                        |      
                        |   
                        |      
                        |    
                        |
                       _|___
                    """
        ]
        return stages[numTurns]



    Wstreak = 0 
    Lstreak = 0
    goAgain = ("y") #another streak counter


    while goAgain.lower() == "y":
        
        print("REBOOTING Robo Executioner...")
        time.sleep(3)
        print("CURRENT WINNING STREAK: " + str(Wstreak))
        time.sleep(1)
        print("CURRENT LOSING STREAK: " + str(Lstreak))
        time.sleep(1)
        print("Howdy there... Here in the wild west...")
        time.sleep(2)
        print("dead men tell no tales")
        time.sleep(3)
        print("You got what it takes to get your buddy here off the gallows?")
        time.sleep(2)
        print("If you can guess what word I'm thinkin of I'll let him go.. try your best now")
        time.sleep(3)
        
        #I just made a long list of the first words that came to mind to pick from 
        sherriffsWords = ["mayonaise", "guns", "marmalade", "jeremy", "shower", "noise", "album", "bank", "train", "crayon", "zoo", "xylaphone", "meow", "freedom", "robber", "knife", "computer", "python", "wowzers", "holy", "trouble", "empire", "snail", "woof", "half", "pie", "easy", "password", "key", "guess", "snippet", "sniper", "tool", "index", "fund", "sail", "horse", "fish", "pip"]
        sherriffChoice = random.choice(sherriffsWords).upper() #picks a random word from the list in all upper case letters
        numTurns = 6

        LettersUsed = [] #establishes the list that clarifies what letters have been used
        mango = "_" * len(sherriffChoice) #creates a string that represents how many mystery letters there are in the chosen word by multiplying _ by the length of the word
        guessedL = False #sets the win condition as false

    
        print(hangTheMan(numTurns)) #prints the hang man based on how many turns are remaining, the less turns the closer to death he is.
        print(mango, "\n") #\n allows you to insert a new line within a string

        while not guessedL and numTurns != 0:
            now = input("Take your best guess partner: ").upper()

            if len(now) == 1 and now.isalpha():
                if now in LettersUsed:
                    print(hangTheMan(numTurns))
                    print("Silly you, you've already tried this one") 
                    print("Used letter list: ", LettersList)  #this checks to see if the letter you tried has been attempted before

                elif now not in sherriffChoice: 
                    numTurns -=1 #removes a turn so that the proper hangman is printed
                    print(hangTheMan(numTurns))
                    print("I don't think so pal.. looks like your buddys hurtin")
                    LettersUsed.append(now) #adds the input letter to the used list
                    LettersList = ' '.join(LettersUsed) #updates the used list
                    print("Used letter list: ", LettersList) #prints the used list for reference
                    print(mango, "\n") #prints the current state of the word the player is guessing
                    

                else: 
                    print(hangTheMan(numTurns))
                    print("You're onto something Tex", now, " is goin up on the board!")
                    LettersUsed.append(now)
                    LettersList = ' '.join(LettersUsed)
                    print("Used letter list: ", LettersList) 
                    tree = list(mango) #creates a list based on the current state of the word being guessed upon 
                    indexin = [i for i, letter in enumerate(sherriffChoice) if letter == now] #loops when a letter in the word chosen by the script is the same as a letter just guessed by the player causing the program to search for that letter's index in the word
                    for index in indexin:
                        tree[index] = now #sets the indexed portions of the word = to the input letter 
                    mango = "".join(tree) #updates the word being guessed upon to reflect the accurate location(s) of the guessed letter
                    print(mango, "\n")

                    if "_" not in mango: #checks to see if the word has been solved and sets the win condition to true
                        guessedL = True

            else:
                print("I don't get what you're sayin there stranger... use a valid format...") #if an invalid entry is made this catches it

        

            if guessedL:  #increments streaks and sets up loop the same as the rock paper scissors game
                Wstreak += 1
                Lstreak = 0
                print("well..")
                time.sleep(2)
                print("I guess you earned your buddies freedom.. Don't be a stranger now! How about we put him back up there for another round? (y/n)")
                goAgain = input(" ").strip()
            if goAgain.upper() != "Y":
                print("I'll be seein ya then!")
                break

        
        if numTurns == 0: #incrememnts streaks
            Wstreak = 0
            Lstreak += 1
            time.sleep(2)
            print("Ah.. a bit emberassing for you..")
            time.sleep(2)
            print("#awkward....")
            time.sleep(2)
            print("....")
            time.sleep(2)
            print("""
                        ----------
                       |          |
                       | O    O   |
                      (    ^       )     
                       |_|_|_|_|_|
                         |_|_|_| 
                    """,) #funny skull emoji 
            time.sleep(2)
            print("Looks like your pal there went belly up! sucks to suck I was thinkin of", sherriffChoice, "case you were curious.") #tells the player the correct answer after they lost
            time.sleep(4)
            print("I say we bring him back from the dead and go again. What do you say? Hows another round sound? (y/n)")#asks to loop   
            goAgain = input(" ").strip()
            if goAgain.upper() != "Y":
                print("I'll be seein ya then!")
                break

if __name__ == "__main__":
    main()       


