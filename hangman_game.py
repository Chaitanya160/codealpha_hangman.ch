import random

def choose_word():
    words = ["python", "developer", "hangman", "algorithm", "function"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def hangman():
    print("🎮 Welcome to Hangman!")

    word = choose_word()
    guessed_letters = []
    attempts = 6

    while attempts > 0:
        print("\nWord:", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            attempts -= 1
            print(f"Wrong guess! Attempts left: {attempts}")

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 Congratulations! You guessed the word:", word)
            return

    print("\n❌ Game Over! The word was:", word)


if __name__ == "__main__":
    hangman()