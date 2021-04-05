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

a = list(map(int,input("\nEnter the numbers : ").strip().split()))
summ = int(input())


bruh = subset_sum(a,summ)
print(bruh)