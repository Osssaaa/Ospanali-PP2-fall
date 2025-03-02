for i in range(65, 91):  
    f = open(chr(i) + ".txt", "w")  
    f.write("This is " + chr(i) + ".txt")  
    f.close()  

print("Файлы A.txt - Z.txt созданы")