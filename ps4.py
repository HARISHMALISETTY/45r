# # seq=["a","h","e","a","h","k","l","k"]
# seq="school"
# dict={}
# # op={"a":2,"h":2,"e":1,"k":2,"l":1}

# for i in seq:
#     if i in dict:
#         dict[i]+=1
#     else:
#         dict[i]=1
# print(dict)

# dict={"emp1":25000,"emp2":29500,"emp3":31500}
# total=0
# #total slry=86000
# for i in dict:
#     total+=dict[i]
# print(total)
# dict={"stu1":"kiran","stu2":"lakshmi","stu3":"naveen","stu4":"naresh"}
# search="kiran"
# # found=False
# count=0
# #write  a program to search studentname in given dictionary.
# for x in dict:
#     # print(dict[x])
#     if(dict[x]==search):
#         # found=True
#         count+=1
#         break
# if(count>0):
#     print(f"{search} is available in given dictionary")
# else:
#     print(f"{search} is not avaialable in given dict")

# dict1={"a":10,"b":15,"c":25,"d":15}
# dict2={"a":15,"c":15,"x":15,"y":10}
# # merged={"a":25,"b":15,"c":40,"d":15,"x":15,"y":10}
# merged={}
# for x in dict1:
#     merged[x]=dict1[x]
# for x in dict2:
#     if x in merged:
#         merged[x]+=dict2[x]
#     else:
#         merged[x]=dict2[x]
# print(merged)

#invert a dictionary
dict1={"x":2,"y":4,"z":6,"a":10}
invert={}
#op={"2":x,"4":y,"6":z,"10":a}
for i in dict1:
    value=dict1[i] 
    invert[value]=i
        
print(invert)




