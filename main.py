import random

words = ["python", "london", "garden", "plants", "coffee"]

secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_incorrect_guesses = 6

print("Welcome to Hangman!")

while incorrect_guesses < max_incorrect_guesses:
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word = display_word + letter
        else:
            display_word = display_word + "_"

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_incorrect_guesses - incorrect_guesses)

    if "_" not in display_word:
        print("You won!")
        break

    guess = input("Guess one letter: ").lower()

    if len(guess) != 1:
        print("Please enter only one letter.")

    elif guess in guessed_letters:
        print("You already guessed that letter.")

    else:
        guessed_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")
        else:
            incorrect_guesses = incorrect_guesses + 1
            print("Wrong guess!")

if incorrect_guesses == max_incorrect_guesses:
    print("\nGame over!")
    print("The word was:", secret_word)