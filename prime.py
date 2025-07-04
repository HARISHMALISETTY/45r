# def prime_check(num):   
#     if num==1:
#         return False
#     elif num<0:
#         return False
#     else:
#         for i in range(2,num): 
#             if num%i==0:
#                 return False
#         else:
#             return True

# # prime_check(15)

# def prime_range(s,e):
#     l=[a for a in range(s,e) if prime_check(a)]
#     print(l)
# prime_range(10,30)



# --->10---> 7 and 11
# ---->5--->3 and 7
# ---->20---->19 and 23

ip=["welcome","some","hello","python"]

#we have to iterate list---->need one for loop
#need to iterate each element--->need one more for loop

# for x in ip:
#     rev=""    
#     for y in range(len(x)-1,-1,-1):
#         # print(x[y])
#         rev+=x[y]
#     print(rev)

    

# ip1=[345,789,1254,7891,1254]
# for num in ip1: #345 789 1254 7891 1254
#     rev=0
#     while(num>0): #345 34 3
#         ld=num%10 #5 4 3
#         rev=rev*10+ld #0*10+5--->5--->5*10+4=54-->54*10+3=543
#         num=num//10 #34 #3 
#     print(rev)

# x=["ab","cd"]

# for i in x[0]:
#     for j in x[1]:
#         print(i+j)


# op--> ac,ad,bc,bd

strs=["HeLlO","SomE","ThiNg","PYthoN"]

for str in strs:
    cnvrt=""
    for char in str:
        if(char==char.upper()):
            # char.lower() #we r just cnvrtng
            cnvrt+=char.lower()
        else:
            # char.upper() #we r just cnvrng
            cnvrt+=char.upper()
        # cnvrt+=char #but here we r cncatinting nrml char only but not cnvrted
    print(cnvrt)



