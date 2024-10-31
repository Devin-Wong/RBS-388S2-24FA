address = "100 Rockafeller Road, Piscataway, NJ 08854"

a = address.split(", ")
street = a[0]
city = a[1]

state_zipcode = a[2]
b = state_zipcode.split()

state = b[0]
zipcode = b[1]

print(f"Street: {street}")
print(f"City: {city}")
print(f"State: {state}")
print(f"Zipcode: {zipcode}")