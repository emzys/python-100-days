#Step 5

import random
# from replit import clear
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
guess_count = 6
end_game = False
guesses = []
display = []

print(f'{logo}')

#Testing code
print(f'\nThe solution is {chosen_word}.')

#Create blanks
for _ in range(word_length):
    display += "_"

# print(stages[guess_count])
while not end_game:
    print(stages[guess_count])
    print(display)
    if len(guesses) > 0:
        print(f"\nSo far you guessed: {(', '.join(guesses))}.")
    guess = input("\nGuess a letter: ").lower()
    # clear()

    if guess in guesses:
        print(f"\nYou have already guessed \"{guess}\".")
        continue
    else:
        guesses += guess

    if guess in chosen_word:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
        if chosen_word == ''.join(display):
            end_game = True
            print(f"{display}\nThe word is: {chosen_word}!\nYou win!")
    else:
        guess_count -= 1
        print(
            f"Wrong guess! The word does not include \"{guess}\". \n{guess_count} tries left."
        )
        if guess_count <= 0:
            end_game = True
            print(f"You lose. The word you were looking for is: {chosen_word}")

print(stages[guess_count])
