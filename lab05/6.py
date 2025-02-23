import re
pattern = r'a.*b$'
test_strings = ["ab", "axb", "a123b", "a", "b", "abc"]

for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"Matched: {string}")