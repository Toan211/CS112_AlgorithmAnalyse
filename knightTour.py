def backtracking(start,path, column, row):
    move_x = [ 1 ,2 ,-1, 2, -2,-2, 1, -1]
    move_y = [ 2 ,1 , 2,-1,  1,-1,-2 ,-2]
    x = ord(start[0]) - 97
    y = int(start[1])
    if(len(path) == row*column):
        return (True,path)
    for i in range (0, len(move_x)):
        newX = x + move_y[i]
        newY = y + move_x[i]
        if newX >= 0 and newX < column and newY >= 1 and newY <= row:
            next = chr(newX + 97) + str(newY)
            if next in path:
                pass
            else:
                path.append(next)
                if backtracking(next, path, column, row)[0] == True:
                    return (True,path)
                else:
                    path.pop()
    return (False,path)
row,column = input().split()
row1 = int(row)
column1 = int(column)
stack = []
start = input()
stack.append(start)
back = backtracking(start, stack , column1, row1)
if back[0] == True:
    print(*back[1])