
def unique(list):
    new_list=[]
    for i in list:
        if i in new_list:
            pass
        else:
            new_list.append(i)
    return new_list
list = list(map(int, input().split()))
print(unique(list))
