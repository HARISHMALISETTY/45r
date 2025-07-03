# #neon num
# #perfect square
# #perfect number
# #sunny num

# # 9-->9^2-->81-->8+1=9
# # 1-->1^2-->1--->1
# # 1.find the square of the given num
# # 2.sum of the digits of o/p

# # num=12
# # square=num*num
# # sum=0
# # while square>0:
# #     ld=square%10
# #     sum+=ld
# #     square=square//10
# # print(sum)

# # if(sum == num):
# #     print(f"{num}is neon num")
# # else:
# #     print(f"{num} is not a neon num")

# #print squares of given range
# #range-->10
# n=40
# is_square=False
# for i in range(1,n+1):    
#     if(i*i == n):
#         is_square=True
#         break
    
# if(is_square):
#     print(f"{n} is a perfect square")
# else:
#     print(f"{n} is not a perfect square")


#find the factors for given num
num=28
sum=0
for x in range(1,num):
    if(num%x==0):
        sum+=x
if(sum==num):
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")
