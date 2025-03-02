with open("output.txt", "r") as source, open("text.txt", "w") as destination:
    destination.write(source.read())