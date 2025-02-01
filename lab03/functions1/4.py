import math
def prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
def filter_prime(list):
    print([num for num in list if prime(num) == True])
numbers = list(map(int, input().split()))
filter_prime(numbers)