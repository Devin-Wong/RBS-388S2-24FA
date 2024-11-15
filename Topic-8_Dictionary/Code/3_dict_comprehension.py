cities = ['PISCATAWAY', 'HIGHLAND PARK', 'FLAGTWON']
zipcode = ['08854', '08904', '08821']

d = {cities[i]:zipcode[i] for i in range(len(cities))}

print(d)
