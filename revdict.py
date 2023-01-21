#Write a program to invert keys and values of dictionary
dict1={1: 'abc', 2: 'def', 3: 'ghi'}
rev_dict=dict(map(reversed,dict1.items()))
print(rev_dict)