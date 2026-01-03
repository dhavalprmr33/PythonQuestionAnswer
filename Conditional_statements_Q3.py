#Input marks and print grade (A,B,C,fail)

math = float(input("Enter math marks:"))
science = float(input("Enter science marks:"))
physics = float(input("Enter physics marks:"))
total = math + science + physics
average = total/3

if average >= 90:
    print("your grade is A")
elif average >= 80:
    print("your grade is B")
elif average >= 70:
    print("your grade is C")
elif average >= 40:
    print("your grade is D")
else:print("You are FAIL")