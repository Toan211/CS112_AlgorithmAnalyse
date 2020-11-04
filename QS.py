import sys
def partition(arr, l, r):
    x = arr[r]
    i = l
    for j in range(l, r):

        if arr[j] >= x:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[r] = arr[r], arr[i]
    return i

def kthSmallest(arr, l, r, k):
    if k > 0 and k <= r - l + 1:
        index = partition(arr, l, r)
        if index - l == k - 1:
            return arr[index]
        if index - l > k - 1:
            return kthSmallest(arr, l, index - 1, k)
        return kthSmallest(arr, index + 1, r,
                           k - index + l - 1)
    return sys.maxsize

n1, k1 = (input()).split()
n = int(n1)
k = int(k1)
lst = []
for i in range(0, n): 
    ele = int(input()) 
  
    lst.append(ele) # adding the element  
n = len(lst)

print(kthSmallest(lst, 0, n - 1, k))



