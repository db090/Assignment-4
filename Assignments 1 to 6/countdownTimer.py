import time

seconds:int=int(input("Enter seconds: "))

for i in range(seconds,0,-1):
    print(f" Time left: {i} seconds")
    time.sleep(1)

print("\n⏰ Time's up!")