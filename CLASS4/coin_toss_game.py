import numpy as np
import os
os.system("clear")
playAgain = "Y"

def place_your_bets(input_tosses, heads_or_tails, player_1_guess, player_2_guess):
    #
    countHeads = 0
    countTails = 0
    n_tosses = 0

    while n_tosses < int(input_tosses):
        Results = np.random.random() > 0.5
        n_tosses += 1

        if Results == True:
            countHeads += 1
            print("Heads!")
        else:
            countTails += 1
            print("Tails!")

    print("In", input_tosses, "tosses there were",countHeads, "heads, and", countTails, "tails.")

    if heads_or_tails == "H": final_count = countHeads
    else: final_count = countTails
    
    if abs(int(player_1_guess) - final_count) < abs(int(player_1_guess) - final_count): 
        winner = "Player 1"
    else: winner = "Player 2"

    return winner



#setup a loop to allow the user to keep playing. Exits the loop if the variable is not "Y"
while playAgain == "Y":

    #Setup the game rules:
    print("Welcome to the game of heads or tails.","\n\n")
    print(" ___ Setting up the game. ___")

    #first select to pick heads or tails to count for the game
    while True:
        heads_or_tails = input("To start the game, please pick heads or tails (H or T): ")
        if heads_or_tails.upper() == "H" or heads_or_tails.upper() == "T": break
        else: print("Sorry, I can't understand that. Please pick 'H' or 'T'.")

    if heads_or_tails == "H":
        h_t_description = "Heads"
    else:
        h_t_description = "Tails"

    #Enter the number of tosses to be performed.
    while True:
        input_tosses = input("Players, please enter the number of tosses: ")
        try: 
            int(input_tosses)
            break
        except: print("Please enter an integer for the number of tosses...")

    #Setup the guesses:
    print("\n")
    print("___ Starting a game with ",input_tosses," tosses for ", h_t_description +". ___")
    while True:

        player_1_guess = input("Player 1, what is your guess for how many " + h_t_description.lower() + " in " + str(input_tosses) + " tosses? ")
        player_2_guess = input("Player 2, what is your guess for how many " + h_t_description.lower() + " in " + str(input_tosses) + " tosses? ")

        #check that both guesses are integers.
        try:
            int(player_1_guess)
            int(player_2_guess)
            break
        except: print("Please enter an integer for the number of guesses...")

    print(place_your_bets(input_tosses, heads_or_tails, player_1_guess, player_2_guess) + " is the winner.","\n")

    playAgain = input("Would you like to play again? (Y or N) ")
    os.system("clear")

