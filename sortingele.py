lst=[]
n=int(input("Enter number of Elements: "))
print("Enter the Elements of the list: ")
for i in range(0,n):
    ele=input()
    lst.append(ele)
lst.sort()
print("The sorted list is: ",lst)