
import random

name = str(input('Hello! What is your name? '))
count = 0
our_num=random.randint(1,20)
print(f'Well, {name}, I am thinking of a number between 1 and 20. ', end = '\n')
while True:
    number = int(input('Take a guess.'))
    if number == our_num:
        print(f'Good job, {name}! You guessed my number in {count} guesses! ')
        break
    if number > our_num:
        print(f'Your guess is too high. ')
    if number < our_num:
        print(f'Your guess is too low. ')
    count+=1
