//counting the occurance of a element coming how many number of times 
lst=['a',1,2,3,'a']
e=input("Enter the element to be searched ")
count=0
for i in range(0,len(lst)):
    if(lst[i]==e):
        count=count+1
    else:
        # count=1
        continue

if count==0:
    print(e,"No element found in list ")
else:
    print(e,"found",count,"times in list ")        
