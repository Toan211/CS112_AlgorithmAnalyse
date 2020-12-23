k = int(input())
a = []
for i in range (0,k):
    a.append(int(input()))
n = len(a)
a.append(1)

def dnc (a,l,r):
    if l > r : return 0
    if l == r : return a[l]*a[l-1]*a[l+1]
    ma = float ('-inf')
    for i in range (l, r+1):
        ma = max(ma, dnc(a,l,i-1)+dnc(a,i+1,r) + a[i]*a[l-1]*a[r+1])
    return ma
    
print (dnc(a,0,n-1))