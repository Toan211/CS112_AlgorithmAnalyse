def check(ip):
    ip = ip.split(".")
    for i in ip:
        if(len(i) > 3 or int(i) > 255 or int(i) < 0):
            return False
        if(len(i) > 1 and int(i) == 0):
            return False
        if(len(i) > 1 and int(i) != 0 and i[0] == '0'):
            return False
    return True

def convert(ip):
    size = len(ip)
    if size > 12: 
        return [] 
    snew = ip 
    l = [] 
    for i in range(1, size - 2): 
        for j in range(i + 1, size - 1): 
            for k in range(j + 1, size): 
                snew = snew[:k] + "." + snew[k:]
                snew = snew[:j] + "." + snew[j:]
                snew = snew[:i] + "." + snew[i:]
                # Check for the validity of combination 
                if check(snew): 
                    l.append(snew) 
                      
                snew = ip 
                  
    return l 
i = input()
s = convert(i)
for i in range (0,len(s)):
    print(s[i])