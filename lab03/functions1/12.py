
def histogram(list):
    for i in range(len(list)):
        print('*'*list[i], end='\n')
list = list(map(int, input().split()))
histogram(list)
