import random

words = ["python", "computer", "program", "hangman", "keyboard", "developer","phone","tablet","coding","apple","pineapple","peach","deer","human"]

word = random.choice(words)

guessed_letters = []
wrong_letters = []
lives = 6

print("Welcome to Hangman!")

while lives > 0:
    display = ""

    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    if "_" not in display:
        print("You win!")
        break

    print(f"Lives: {lives}")
    print("Wrong letters:", " ".join(wrong_letters))

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed_letters or guess in wrong_letters:
        print("You already guessed that letter.")
        continue

    if guess in word:
        guessed_letters.append(guess)
        print("Correct!")
    else:
        wrong_letters.append(guess)
        lives -= 1
        print("Wrong!")

if lives == 0:
    print("\nGame Over!")
    print("The word was:", word)