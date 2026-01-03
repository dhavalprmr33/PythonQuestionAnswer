largest = None
while True:
    num = (input("enter number or 'done' to finish :"))
    if num == 'done' :
        break
    try :
        num = float(num)
        if largest is None or num > largest :
            largest = num

    except:
        print("invalid input")
    print("largest num is :",largest )