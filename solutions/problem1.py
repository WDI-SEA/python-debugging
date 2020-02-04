# Import packages
import random

# Declare min and max constants
MIN = 1
MAX = 10

# Pick a random number as the right answer
answer = random.randint(MIN, MAX)

print(f'I\'m thinking of a number between {MIN} and {MAX}')

# Have the user guess until they get the answer correct
while True:
    guess = int(input('Guess a number? '))

    # Do something with that answer
    if guess == answer:
        print(f'{guess} is correct - YOU WIN!')
        break
    elif guess < answer:
        print(f'{guess} is too low!')
    else:
        print(f'{guess} is too high!')
