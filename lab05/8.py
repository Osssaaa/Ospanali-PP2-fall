import re
pattern = r'(?=[A-Z])'
text = "SplitAtUppercaseLetters"
words = re.split(pattern, text)
print(words)