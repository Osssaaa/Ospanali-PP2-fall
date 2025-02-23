import re
pattern = r'[A-Z][a-z]+'
test_strings = ["Hello", "Python", "java", "J", "AB", "CamelCase"]

for string in test_strings:
    if re.search(pattern, string):
        print(f"Matched: {string}")