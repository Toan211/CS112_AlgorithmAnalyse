def subset_sum(set, n, summ): 

    if (summ < 0):
        return False
    subset =([[False for i in range(summ + 1)]  
            for i in range(n + 1)]) 
    for i in range(0, n): 
        subset[i][0] = True
    for i in range(1, summ + 1): 
        subset[0][i]= False
    for i in range(1, n + 1): 
        for j in range(1, summ + 1): 
            if j<set[i-1]: 
                subset[i][j] = subset[i-1][j] 
            if j>= set[i-1]: 
                subset[i][j] = max(subset[i-1][j], 
                                   subset[i - 1][j-set[i-1]])   
    return subset[n][summ] 
a = list(map(int,input("\nEnter the numbers : ").strip().split()))
summ = int(input())
bruh = subset_sum(a,len(a),summ)
if bruh == True:
    print('Correct')
else:
    print('False')