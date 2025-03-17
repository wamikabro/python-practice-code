import copy

listt = [1,2,3,4,5]

def copyTheListOnly(listt, change):
    listt[0] = change

copyTheListOnly(copy.copy(listt), "It won't change the original list")

print(listt)

copyTheListOnly(listt, "It will change the original list")
print(listt)
