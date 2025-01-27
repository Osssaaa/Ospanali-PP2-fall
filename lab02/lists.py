#first example
list1 = ['apple', 'banana', 'cherry', 'orange', 'berry', 'kiwi', 'melon']
list2 = [1, 8, 5, 7, 2, 7, 3]
list3 = [True, False, True, False, False]
print(type(list1))
print(type(list2))
print(type(list3))

#second example

print(list1[0],' >> ', type(list1[0]))
print(list2[0],' >> ', type(list2[0]))
print(list3[0],' >> ', type(list3[0]))
    
print(list2[2:5])           #elemenets which index [2, 5)

#third example

list0 = ['apple', 'banana', 'cherry']
list0[1:] = 'orange', 'berry'             #we can change elements of list
print(list0)

#fourth example

list0.append('kiwi')               #we can add elements to the already existed list 
print(list0)
list0.insert(1, 'melon')            #adding with index
print(list0)

#fifth example

listthislist = ["apple", "banana", "cherry"]
listthislist.remove('banana')       #first appearance of banana
listthislist.pop(1)                 #deleting by index
del listthislist                    #deleting whole list