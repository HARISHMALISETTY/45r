# list=["apple","banana","orange","banana","apple","grape","orange"]

# op={"apple":2,"banana":2,"orange":2,"grape":1}

# dict={}

# for fruit in list:
#     if fruit in dict:
#         dict[fruit]+=1
#     else:
#         dict[fruit]=1
# print(dict)
        

# str="banana" 
# op=["b","a","n","a","n","a"]
# dict={}

# for fruit in str:
#     if fruit in dict:
#         dict[fruit]+=1
#     else:
#         dict[fruit]=1
# print(dict)  

str="banana" 
# op=["b","a","n","a","n","a"]  
op=[]
for x in str:
    # op+=x
    if x not in op:
        op+=x
print(op)
