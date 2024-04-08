import ticTacToe
import RockPaperScissors
import HangMan

def main_menu():
    while True:
        
        choice = input("Which game would you like to play?\n1. Rock Paper Scissors at High Noon\n2. Tic Tac Toe with a Wizard\n3. Hang Man also at Noon\nEnter number: ")
        if choice == '1':
            RockPaperScissors.main()
            break
        elif choice == '2':
           ticTacToe.main()
           break
        elif choice == '3':
            HangMan.main()
            break
        else:
            print("Invalid choice, please enter 1, 2, or 3.")

if __name__ == "__main__":
    while True:
        main_menu()
        if input("Play another game? (y/n): ").lower() != 'y':
            break