#Use tuple unpacking to assign values to variables.

person  = ("Alex",18,"India")

name,age,country = person

print("name:",name)
print("age:",age)
print("country:",country)

# you can also ignore value using "_".

data  = ("ANNU","ANGEL","DIAMOND")
x,_,y = data
print(x,y)