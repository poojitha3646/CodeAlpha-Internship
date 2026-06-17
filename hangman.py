import random

words = ["python", "java", "javascript", "html", "css", "clanguage"]

word = random.choice(words)
guessed_letters = []
attempts = 6

print("=" * 40)
print("        HANGMAN GAME")
print("=" * 40)

while attempts > 0:

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Attempts Left:", attempts)

    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word.")
        print("Word:", word)
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1:
        print("Please enter only one letter.")
        continue

    if not guess.isalpha():
        print("Please enter an alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct Guess!")
    else:
        attempts -= 1
        print("❌ Wrong Guess!")

if attempts == 0:
    print("\n Game Over!")
    print("The word was:", word)

print("\nThank You For Playing!")