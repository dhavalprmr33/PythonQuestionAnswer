#Compare three numbers and print the greatest.

A = float(input("enter number "))
B = float(input("enter number "))
C = float(input("enter number "))

if A > B and A > C:
    print(A,"gretest")
elif B > C and C > A:
    print(B,"gretest")
else:print(C,"gretest")