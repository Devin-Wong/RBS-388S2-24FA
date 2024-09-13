def main():
    radius = 2
    area_value = area(radius)
    print(f"The area of a circle with radius {radius} is {area_value}.")

def square(a):
    return a**2

def area(r):
    return 3.14 * square(r)

main()