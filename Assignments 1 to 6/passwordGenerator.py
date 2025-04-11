import random
import string

length=int(input("Enter length for your password: "))

characters=string.ascii_letters+string.digits+string.punctuation

password="".join(random.choice(characters) for _ in range(length))

print(f"Here is your new password {password}" )