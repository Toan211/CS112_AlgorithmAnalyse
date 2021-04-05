def subset_sum(sett,i, summ):
    if summ == 0:
        return True
    elif summ < 0 or i == 0:
        return False
    else:
        return(subset_sum(sett,i-1,summ) or subset_sum(sett,i-1,summ-sett[i-1]))
#n = int(input())
a = list(map(int,input("\nEnter the numbers : ").strip().split()))
summ = int(input())
#sett = []

#for i in range(0,n):
#    k = int(input())
#    sett.append(k)

bruh = subset_sum(a,len(a),summ)
if bruh == True:
    print('Correct')
else:
    print('False')