try:
    a=int(input("Enter a value of A:"))
    b=int(input("Enter a value of B:"))
    c=a/b
    print("Division is:",c)
    l=[10,20,30,40]
    index=int(input("Enter index number to fatch element:"))
    print("Element:",l[index])
except ZeroDivisionError as e:
    print("Exception Caught:",e)

except ValueError as e:
    print("Exception Caught:",e)

except IndexError as e:
    print("Exception Caught:",e)

