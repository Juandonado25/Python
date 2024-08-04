import os
import random
import hangman_art
import hangman_words

clear = lambda: os.system('clear')

chosen_word = random.choice(hangman_words.word_list).lower()
print(f"The choosen word is {chosen_word}")
display = ["_"]*len(chosen_word)

print(hangman_art.logo)
print("Welcome to Hangman game. Guess the word and win!")

lives = 6
end_of_the_game=False
while not end_of_the_game and lives > 0:
    guess = input("Guess a letter: ").lower()
    clear()
    for i in range(len(chosen_word)):
        if  chosen_word[i]==guess:
            display[i] = guess
    aux = ""
    print(aux.join(display))
    if guess not in chosen_word:
        lives -= 1
        print(f"lives--: {lives}")
        aux = ""
        print(aux.join(display))
        print(hangman_art.stages[lives])
    if "_" not in display:
            end_of_the_game = True
            print("You Win!")
    if lives == 0:
         print(f"The word is {chosen_word}. You loose!")
    