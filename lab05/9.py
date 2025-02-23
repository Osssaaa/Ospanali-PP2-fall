import re
pattern = r'([a-z])([A-Z])'
text = "InsertSpacesBetweenWords"
modified_text = re.sub(pattern, r'\1 \2', text)
print(modified_text)