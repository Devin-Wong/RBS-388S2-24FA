s = "rutgers"
c = "e"

res = -1
for i in range(len(s)):
    if s[i]==c:
        res = i
        break

print(res)