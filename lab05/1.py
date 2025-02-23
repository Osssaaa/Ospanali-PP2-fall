import re

pattern = r'ab*'
test_strings = ["a", "ab", "abb", "ac", "b", "ba"]

for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"Matched: {string}")