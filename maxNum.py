a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=int(input("Enter third number:"))
if (a>b and  a>c):
    print("Maximum is a:",a)
elif (b>c and b>a):
    print("Maximum is b:",b)
elif (c>a and c>b):
    print("Maximum is c:",c)
    