def count(s, c):
    count = 0
    for i in range(len(s)):
        if s[i]==c:
            count += 1
    return count

def find_repetition(s):
    s = s.upper()
    for i in range(len(s)):
        c = s[i]
        times = count(s, c)
        if times>1:
            return True
    return False  

s = "rbs"
res = find_repetition(s)
print(res)
