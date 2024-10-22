l = [1, 3, 9]

# --- old method ----
# squared = []
# for i in l:
#     squared.append(i**2)

# --- comprehension ---
squared = [i**2 for i in l]

print(squared)    