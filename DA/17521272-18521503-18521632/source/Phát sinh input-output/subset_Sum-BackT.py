def subset_sum(array, target_sum, start=0, target_array=[]):  # dangerous default value
    solutions = set()

    for idx in range(start, len(array)):
        target_array.append(array[idx])

        if sum(target_array) == target_sum:
            solutions.add(tuple(target_array))
            target_array.pop()
            solutions |= subset_sum(array, target_sum, start + 1)
            break

        solutions |= subset_sum(array, target_sum, idx + 1)

        target_array.pop()

    return solutions
with open("input10.txt", "r") as f:
    b = f.readline()
    a = list(map(int,b.split()))
    summ = int(f.readline())
OutFile = open("output10.txt","w")
    

#a = list(map(int,input("\nEnter the numbers : ").strip().split()))
#summ = int(input())


bruh = subset_sum(a,summ)
bruh2 = list(bruh)
if len(bruh) == 0 and summ != 0:
    OutFile.writelines("False")
elif summ == 0:
    OutFile.writelines("Sum is 0 so it's alway correct")
else:
    OutFile.writelines(" ".join(map(str,bruh2[0])))