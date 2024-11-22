# counting
def count(l, c):
    n = 0
    for i in l:
        if i==c:
            n += 1
    return n 

s = "Rutgers,RBS"
# get upper case
s = s.upper()

# obtain the unique letters in the string
chars = set(s)

# count each charactor in s
freq = []
for c in chars:
    n = count(s, c)
    freq.append(n)

# zip
z = dict(zip(chars, freq))
print(z)





       