
def palindrome(string):
    return string == string[::-1]
string = str(input())
print(palindrome(string))
