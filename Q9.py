score = float(input("enter a value between 0.0 and 1.0 :"))
if score >= 1.0 :
    print("ERROR")
elif score <= 0.0:
    print("ERROR")
elif score >= 0.9:
    print("grade : A")
elif score >= 0.8:
    print("grade : B")
elif score >= 0.7:
    print("grade : C")
elif score >= 0.6:
    print("grade : D")
elif score <= 0.6:
    print("grade : F")
else:
    print("ERROR")