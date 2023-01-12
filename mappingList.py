#Write a program to map 2 lists into a dictionary
list1=[]
list2=[]
n1=int(input("Enter the values for first list1: "))
for i in range(0,n1):
    ele1=input()
    list1.append(ele1)
n2=int(input("Enter the values for first list2: "))
for j in range(0,n2):
    ele2=input()
    list2.append(ele2)
dictionary=dict(zip(list1,list2))
print(dictionary)
