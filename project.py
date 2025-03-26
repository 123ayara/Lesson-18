try:
    age=(input("Enter your age:")).strip()
    if not age.isdigit():
        print("Error: Age must be a positive integer")
    age=int(age)
    if age%2==0:
        print(age,"is an even number")
    else:
        print(age,"is an odd number")
except Exception as e:
    print("An unexpected error occurred:",e)