def three_after_three(numbers):
    i = 0
    while i < len(numbers) - 1 :
        if numbers[i] == 3 and numbers[i+1] ==3 :
            return True
            break
        i+=1
    return False
array = list(map(int, input().split()))
print(three_after_three(array))