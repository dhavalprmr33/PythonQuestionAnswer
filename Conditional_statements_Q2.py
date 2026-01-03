#Take a number and check iif it's dividible by 3 and 5.

Number = int(input("enter a number:"))
divideby3 = Number % 3 == 0
divideby5 = Number % 5 == 0

if divideby3 and divideby5:
    print(Number,"divide by 3 and 5")
elif divideby3 == True:
    print(Number,"divide by 3")
elif divideby5 == True:
    print(Number, "divide by 5")
else:print(Number,"isn't divide by 3 and 5")
