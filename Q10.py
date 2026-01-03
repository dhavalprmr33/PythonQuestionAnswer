n  = int(input("enter n th value :"))
if n <= 0:
    print(" Please Enter a Positive Number ;")
else:
    a = 0
    b = 1
    count = 0
    print("fiboncci series number :")
while count < n :
    print(a , end ='')
    c = a +b
    a = b
    b = c
    count += 1