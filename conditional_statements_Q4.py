#input year and check if it's a leap year.

Year = int(input("enter a running year:"))
if Year % 4 == 0:
    print(Year,"is a leap year")
else:print(Year,"isn't a leap year")