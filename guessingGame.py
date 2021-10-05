import random

guessTaken = 0

number = random.randint(1, 20)
print("Im thinking of a number between 1 and 20")

for guessTaken in range(5):
    guess = int(input("Take a guess: "))

    if guess == number:
        break
    
    if guess > number:
        print("Too High")

    if guess < number:
        print("Too Low")

if guess == number:
    print(f"Congratulations! the answer was {number} you answered correctly in {guessTaken} trys")

if guess != number:
    print(f"Sorry you lose, the answer is {number}")