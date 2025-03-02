text = input()
clean_text = text.lower().replace(' ', '')
reversed_text = clean_text[::-1]
print(clean_text == reversed_text)