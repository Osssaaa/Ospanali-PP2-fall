fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
print("--------")
for x in "banana":
  print(x)
print("--------")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
print("--------")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)
print("--------")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
print("--------")
for x in range(6):
  print(x)
print("--------")
for x in range(2, 6):
  print(x)
print("--------")
for x in range(2, 30, 3):
  print(x)
print("--------")
for x in range(6):
  print(x)
else:
  print("Finally finished!")
print("--------")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
  for y in fruits:
    print(x, y)