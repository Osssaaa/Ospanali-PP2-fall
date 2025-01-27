set1 = {4, 3, 2, True, 'aaaa', 'bbb', 'cccc', False}
set2 = {4, 3, 2}
print(set1)
print(set2)
print(4 in set1)
print(4 not in set1)
print(7 in set1)
set1.add("orange")
print(set1)

print('\n', '____________________________', '\n')

fruits = {'apple', 'banana', 'qwerty'}
tropical = {'pineapple', 'kiwi'}
fruits.update(tropical)
print(fruits)