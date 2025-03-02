word=str(input())
upper = 0
lower = 0
for i in word:
    if i.isupper():
        upper+=1
    if i.islower():
        lower+=1
print('lower:', lower)
print('upper', upper)