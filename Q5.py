import math
def find_area(radius):
    return math.pi * radius * radius
def find_perimeter(radius):
        return 2 * math.pi *  radius

r = float(input("enter a Radius of circle(radius):"))

area = find_area(r)
perimeter = find_perimeter(r)

print("circle area:",area)
print("circle perimeter:",perimeter)
