import math
import random

# 1. 
def gr_to_ou(gram):
    return gram * 28.3495231

# 2. 
def far_to_cel(F):
    return (F - 32) * (5 / 9)

# 3. 
def solve(numheads, numlegs):
    rabbits = (numlegs / 2) - numheads
    chickens = numheads - rabbits
    return f'There are {int(rabbits)} rabbits and {int(chickens)} chickens'

# 4. 
def prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def filter_prime(lst):
    return [num for num in lst if prime(num)]

# 5. 
def perm(s, ans=""):
    if len(s) == 0:
        print(ans)
        return
    for i in range(len(s)):
        rest = s[:i] + s[i+1:]
        perm(rest, ans + s[i])

# 6. 
def reverse(sentence):
    return " ".join(sentence[::-1])

# 7. 
def three_after_three(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] == 3 and numbers[i + 1] == 3:
            return True
    return False

# 8. 
def spy_game(nums):
    code = [0, 0, 7]
    for num in nums:
        if num == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

# 9. 
def volume(radius):
    return (4 / 3) * math.pi * (radius ** 3)

# 10. 
def unique(lst):
    new_list = []
    for i in lst:
        if i not in new_list:
            new_list.append(i)
    return new_list

# 11. 
def palindrome(string):
    return string == string[::-1]

# 12. 
def histogram(lst):
    for i in lst:
        print('*' * i)

# 13. 
def guess_number():
    name = input('Hello! What is your name? ')
    count = 1
    our_num = random.randint(1, 20)
    print(f'Well, {name}, I am thinking of a number between 1 and 20.')

    while True:
        try:
            number = int(input('Take a guess: '))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if number == our_num:
            print(f'Good job, {name}! You guessed my number in {count} guesses!')
            break
        elif number > our_num:
            print('Your guess is too high.')
        else:
            print('Your guess is too low.')

        count += 1