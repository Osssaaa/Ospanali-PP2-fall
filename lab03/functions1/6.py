def reverse(sentence):
    i = len(sentence)-1
    while i>=0:
        print(sentence[i], end=' ')
        i-=1
sentence = list(map(str, input().split()))
reverse(sentence)