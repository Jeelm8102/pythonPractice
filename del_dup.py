//deleting duplicate values from list
ini_list=[1,2,3,4,5,4,3,2,1,5]
print("The original list is : " + str(ini_list))

new_list=[]
for i in ini_list:
    if i not in new_list:
        new_list.append(i)
        
print("The list after deleting the duplicate is : " + str(new_list))