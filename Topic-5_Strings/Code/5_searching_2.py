def find(s, c):
    res = -1
    for i in range(len(s)):
        if s[i]==c:
            res = i
            break
    return res

s = "rutgers"
c = "e"
print(find(s,c))