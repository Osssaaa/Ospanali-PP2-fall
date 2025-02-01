def perm(s, ans):
    if len(s) == 0:
        print(ans)
        return
    for i in range(len(s)):
        a = s[i]
        left = s[:i]
        right = s[i+1 :]
        rest = left + right
        perm(rest, ans + s[i])
word = str(input())
perm(word, '')