def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y!=0:
       return x/y
    else:
        return "Error! Devision by zero"
print("Select Operation")

print("1.add")
print("2.Subtarct")
print("3.Multiply")
print("4.Divide")

choice=input("Enter choice(1/2/3/4)")

num1=int(input("Enter a number"))
num2=int(input("Enter a number"))

if choice=='1':
    print(f"the result is:{add(num1,num2)}")

elif choice=='2':
    print(f"the result is:{subtract(num1,num2)}")

elif choice=='3':
    print(f"the result is:{multiply(num1,num2)}")

elif choice=='4':
    print(f"the result is:{divide(num1,num2)}")

else:
    print("invalid input")