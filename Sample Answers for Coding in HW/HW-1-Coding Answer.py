def main(): # 2 pts
    radius = 3
    height = 4
    s = surface(radius, height)
    print(f"The surface of a cylinder with base radius {radius} and height {height} is {s}.") # 1 pt

def add(a, b): # 1 pt
    c = a + b
    return c

def surface(radius, height): # # 1 pt
    s = 2 * 3.14 * radius * add(radius, height)
    return s

main()