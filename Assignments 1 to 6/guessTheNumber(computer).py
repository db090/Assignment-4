low = 1
high = 100
feedback = ''

while feedback != 'c':
    guess = (low + high) // 2
    print(f"My guess is {guess}")
    feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").lower()

    if feedback == 'h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1

print("Yay! I guessed it right! 🎉")
