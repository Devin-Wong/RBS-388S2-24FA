cities = ['PISCATAWAY', 'HIGHLAND PARK', 'FLAGTWON']
zipcode = ['08854', '08904', '08821']

z = dict(zip(cities, zipcode))

city = 'FLAGTWON'
zc = z[city]

print(zc)
