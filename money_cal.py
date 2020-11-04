def Count(n,V,m):
    if (n == 0):
        return 1
    if (n < 0 or m < 1):
        return 0
    return Count(n - V[m - 1], V, m) + Count(n, V, m - 1)
def fastest(n,V,m):
    count = 0
    for i in range(0, m):
        if(n % V[i] != 30000 and n % V[i] != 10000 ):
            a = n // V[i]
            count = count + a
            n = n % V[i]
        else:
            if(V[i] == 200000 and n > 400000):
                count = count + 1
                n = n - V[i]
            if(V[i] == 100000 and n > 200000):
                count = count + 1
                n = n - V[i]
            if((V[i] == 50000) and n > 100000):
                 count = count + 1
                 n = n - V[i]
    return count
    
n = int(input())


a = [500000,200000,100000,50000,20000]
m = len(a)
if(n % 10000 == 0 and n <= 10000000):
    print(Count(n,a,m),fastest(n,a,m))