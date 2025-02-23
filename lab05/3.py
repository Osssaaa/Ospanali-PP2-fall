import re
pattern = r'\b[a-z]+_[a-z]+\b'
test_strings = ["hello_world", "snake_case_example", "test_", "_start", "no_underscore"]

for string in test_strings:
    if re.search(pattern, string):
        print(f"Matched: {string}")