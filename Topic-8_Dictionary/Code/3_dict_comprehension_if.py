names = ['Jack', 'Mark', 'Mary', 'Jenny']
ages = [22, 17, 23, 19]

d = {names[i]: ages[i] for i in range(len(names)) if ages[i] > 20}

print(d)

# {'Jack': 22, 'Mary': 23}