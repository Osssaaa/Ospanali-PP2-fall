thistuple = ("apple", "banana", "cherry")
print(thistuple)                            

print(len(thistuple))                       

thistuple = ("banana",)
print(type(thistuple))                      

thistuple = ("banana")
print(type(thistuple))                      

#Date Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
tuple4 = ("abc", 34, True, 40, "male")

# Convert the tuple into a list
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)

# Unpack Tuples
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)                                
print(yellow)                               
print(red)                                  

# Using Asterisk "*"
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)                                
print(yellow)                               
print(red)                                  

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)                                
print(tropic)                               
print(red)                                  

# Join Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)                              

fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)          