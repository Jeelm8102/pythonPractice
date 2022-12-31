digits,upper_case,lower_case,space=0,0,0,0
str=input("Enter the String : ")
for i in range (len(str)):
    if str[i].isdigit():
        digits+=1
    elif str[i].isupper():
        upper_case+=1
    elif str[i].islower():
        lower_case+=1
    elif str[i].isspace():
        space+=1
    else:
        pass
print("Length of the string is : ",len(str))   
print("Number of digits are : ",digits)
print("Number of Upper case letters are : ",upper_case)
print("Number of Lower case letters are : ",lower_case)
print("Number of Spaces are : ",space)