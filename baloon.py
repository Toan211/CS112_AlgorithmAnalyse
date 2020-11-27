def getMax(A): 
    N = len(A) 
    A = [1] + A + [1]# Add Bordering Balloons 
    dp = [[0 for x in range(N + 2)] for y in range(N + 2)]
      
    for length in range(1, N + 1): 
        for left in range(1, N-length + 2): 
            right = left + length -1
            for last in range(left, right + 1): 
                dp[left][right] = max(dp[left][right],  
                                      dp[left][last-1] +
                                      A[left-1]*A[last]*A[right + 1] + 
                                      dp[last + 1][right]) 
    return(dp[1][N]) 
  
# Driver code 
n = int(input())
A = []
for i in range (0,n):
    A.append(int(input()))
print(getMax(A))