


def count(i, le):
    if (i-1<0):
        money = le[i]*le[i+1]
    elif (i+1 == len(le)):
        money = le[i+1]*le[i]
    else:
        money = le[i-1]*le[i]*le[i+1]
    return money


def comp(money, maxMoney):
    if (money > maxMoney):
        maxMoney = money

def abc(le):
    for i in range (0, len(le)):
        money2 = count(i, le)
        

n = int(input())
k = []
for i in range (0,n):
    k.append(int(input()))

