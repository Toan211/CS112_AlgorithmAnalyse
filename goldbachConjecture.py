def primess(n):
    lis = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if lis[i]:
            lis[i*i::2*i]=[False]*int((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3,n,2) if lis[i]]    
def binarySearch (arr, l, r, x): 
    if r >= l:
        mid = l + (r - l) // 2
        if arr[mid] == x: 
            return True 
        elif arr[mid] > x: 
            return binarySearch(arr, l, mid-1, x) 
        else: 
            return binarySearch(arr, mid + 1, r, x) 
  
    else: 
       return False
num = int(input())
primes = primess(num)
count = 0
for i in range(len(primes)):
        x = num - primes[i]
        Result = binarySearch(primes,0,len(primes)-1,x)
        if x < primes[i]:
            break
        if Result == True:
            count = count + 1
print(count)