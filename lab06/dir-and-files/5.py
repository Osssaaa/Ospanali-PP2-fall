import os
f = open(r"C:\\Users\\User\\Desktop\\code\\git-lessons\\lab06\\dir-and-files\\output.txt", "w")
list = [1, 2, 3, 4]
for i in list:
    if i == list[0]:
        f.write("[")
    if i != list[-1]:
        f.write(f"{str(i)}, ")
    if i == list[-1]:
        f.write(f"{str(i)}]")
f.close()