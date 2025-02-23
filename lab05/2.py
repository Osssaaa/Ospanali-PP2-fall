import re
pattern = r'abb{2,3}'
test_strings = ["abb", "abbb", "abbbb", "a", "ab", "ac"]

for string in test_strings:
    if re.fullmatch(pattern, string):
        print(f"Matched: {string}")