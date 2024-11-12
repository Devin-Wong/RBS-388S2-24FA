def summarize_data(x):
    return min(x), sum(x)/len(x), max(x)

l = [1, 2, 5]

minimum, mean, maximum = summarize_data(l)

print(minimum, mean, maximum)