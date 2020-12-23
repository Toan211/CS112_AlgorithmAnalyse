def palindrome(Chara):
    Chara = Chara.split(" ")
    for i in Chara:
        size = len(i)
        for j in range (0, size//2):
            if(i[j] != i[size-j-1]):
                return False
    return True
def strsplit(str, i, out):
    if(i == len(str)):
        if(palindrome(out) == True):
            print(out)
    for j in reversed(range(i,len(str))):
        sub_str = str[i:j+1] + " "
        strsplit(str,j+1,out + sub_str)
    return 0
str = input()
bruh = strsplit(str,0,"")