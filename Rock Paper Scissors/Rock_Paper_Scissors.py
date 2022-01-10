import getpass


#The Winner function compares both player inputs and outputs who won
def Winner(player1choice, player2choice):
    if player1choice == player2choice:
        print("It's a tie!")
    elif player1choice == 'ROCK' or 'rock':
        if player2choice == 'SCISSORS' or 'scissors':
            print("ROCK wins!\nCongratulations, "+user1+"!")
        elif player2choice == 'PAPER' or 'paper':
            print("PAPER wins!\nCongratulations, "+user2+"!")
        else:
            print("Sorry! Someone didn't choose one of the three choices... Try again!")
    elif player1choice == 'SCISSORS' or 'scissors':
        if player2choice == 'PAPER' or 'paper':
            print("SCISSORS wins!\nCongratulations, "+user1+"!")
        elif player2choice == 'ROCK' or 'rock':
            print("ROCK wins!\nCongratulations, "+user2+"!")
        else:
            print("Sorry! Someone didn't choose one of the three choices... Try again!")
    elif player1choice == 'PAPER' or 'paper':
        if player2choice == 'ROCK' or 'rock':
            print("PAPER wins!\nCongratulations, "+user1+"!")
        elif player2choice == 'SCISSORS' or 'scissors':
            print("SCISSORS wins!\nCongratulations, "+user2+"!")
        else:
            print("Sorry! Someone didn't choose one of the three choices... Try again!")
    else:
        print("Whoops! Try again, but this time please make sure to select one of the three choices: ROCK, PAPER, or SCISSORS!")

while True:
    #Basic introduction
    print("\nWelcome to Rock, Paper, Scissors!")
    #Rules of the game
    print("\n          RULES        ")
    print("**************************")
    print("** ROCK beats SCISSORS  **")
    print("** PAPER beats ROCK     **")
    print("** SCISSORS beats PAPER **")
    print("**************************")
    
    #Prompts both players for their names and assigns them a player number
    user1 = input("\n\nWhat's your name? ")
    print("Player 1 will be:", user1)
    user2 = input("\nWhat's your name? ")
    print("Player 2 will be:", user2)
    
    player1choice = getpass.getpass(prompt="\nPlayer 1's turn: ") #Hides the Player 1 selection
    player2choice = getpass.getpass(prompt ="Player 2's turn: ") #Hides the Player 2 selection
    
    player1choice = player1choice.upper() #Reads in every entry for Player 1 into uppercase
    player2choice = player2choice.upper() #Reads in every entry for Player 2 into uppercase
    
    #Declares a showdown between two choices, in order by player number
    print("\n\nIn today's showdown we have", player1choice, "VS", player2choice+"!!!\n") 
    
    #Calls the Winner function to determine a winner of the showdown
    Winner(player1choice, player2choice)

    #Prompts the user if they would like to play again
    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            break
        print("Invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        break


