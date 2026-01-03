#WAP to check if a number entered by the user is odd or even
Data = int(input("enter a number ->"))
Data_2 = Data % 2
if Data_2 == 0:
    print(Data ,"is even")
else : print(Data ,"is odd")