
def volume(radius):
    return float(((4*3.14159265359)/3)* (radius**3))
radius=float(input())
print(f'Volume of the sphere with radius {radius} is {volume(radius)} unit cube')
