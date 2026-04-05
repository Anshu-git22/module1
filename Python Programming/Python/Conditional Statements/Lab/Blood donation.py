age = int(input("Enter age: "))
weight = int(input("Enter weight: "))

if age >= 18:
    if weight >= 50:
        print("Eligible for blood donation")
    else:
        print("Weight too low")
else:
    print("Age too low")
