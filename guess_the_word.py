#Alexis Christiansen
#CIS256 Fall 2026
#Programming Assignment 4

#import random for random selection
import random

#list of words for the game to select words from
word_list = ['moose','tiger','tree','velvet','luminous','generator','radiance']

#assigning a variable to choose a random word
select_word = random.choice(word_list)

#creating the number of attempts allowed in the guessing game
attempts = 10

#creating empty guess list to append later on to show guess attempts. 
guesses = []

#print statement to let the user know we are going to play a game
print("Let's play guess the word!")

#while True loop to play the game 
while True:
    for letter in select_word:
        if letter in guesses:
            #used end = ' ' to print on the same line
            print(letter, end = ' ')
        else:
            print('_', end = ' ')

    #print statement to break printing on the same line
    print('')

    print(f'Number of attempts left: {attempts}.')
    print(f'Guessses: {guesses}')

    #create input to get users guess
    guess = input('Please make a guess: ')

    #created an if statement to handle if the user is more one letter
    if len(guess) == 1:
        guesses.append(guess)
    else:
        print('Input can only be one letter.')

    #if statement to reduce attempts when a letter in the word is not there
    if guess not in select_word:
        attempts -= 1
        #if statement to continue game if attemtps are greater than 0
        if attempts > 0:
            print('Try again.')
        else: 
            print('Game over.')
            break
