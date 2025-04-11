import random
words = [
    "python", "streamlit", "database", "function", "variable",
    "algorithm", "condition", "loop", "hangman", "syntax",
    "compile", "debug", "object", "class", "inheritance",
    "module", "package", "list", "dictionary", "string",
    "boolean", "integer", "float", "exception", "recursion"
]
word_to_guess=random.choice(words)
guessed_letters=[]
lives=6

print("🎮 Welcome to Hangman!")
print("_"*len(word_to_guess))

while lives > 0:
    guess=input("\nGuess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⛔ Please enter a single letter.")
        continue
    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("✅ Good guess!")
    else:
        lives-=1
        print(f"❌ Wrong! You have {lives} lives left.")

    #Show current progress
    display_word=[letter if letter in guessed_letters else "_" for letter in word_to_guess]
    print("".join(display_word))

    #Win condition
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word!")
        break

#lose condition
if lives == 0:
    print(f"\n💀 Game Over! The word was '{word_to_guess}'.")