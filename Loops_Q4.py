#Print factorial of a number using while.

number = int(input("enter a number"))
fact = 1 
i = 1
while i <= number:
    fact = fact * i 
    i  = i + 1 
    
    print("factorial of",number,"is",fact)