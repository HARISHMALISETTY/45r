# 1.str="school"

# builin methods

# str="school"
# count=0
# search_char='o'

# for char in str:
#     if(char==search_char):
#         # print(char)
#         count+=1
# print(f"count of {search_char} in {str} is {count} ")

# num=125245
# count=0
# #find the count of occurance of 5 in given num
# cnvrt=str(num)
# for i in cnvrt:
#     if(int(i)==5):
#         count+=1
# print(count)

#count of occurance of digits which can divisible by 2 in entire num

# num=12345678
# cnvrt=str(num)
# count=0
# for i in cnvrt:
#     if(int(i)%2==0):
#         count+=1
# print(count)

# num=12345412
# digit=4
# count=0
# while(num>0):
#     ld=num%10 #getting last digit
#     if(ld==digit): #checking that last digit with digit
#         count+=1 #increasing count if match found
#     num=num//10 #reducing the num
# print(count) # final count of digit

# count of occurance of digits which can divisible by 2

# num=1245890246
# count=0
# while(num>0):
#     ld=num%10 #getting last digit
#     if(ld%2==0): #checking whether divisible by 2 or not
#         count+=1 #increasing count if it is divisible by 2
#     num=num//10 # reducing num
# print(count) #printing final count

#find the sum of the squares of all digits in a given num.
# 125-->1x1+2x2+5x5
# num=123
# squares=0
# while(num>0):
#     ld=num%10
#     squares+=ld**2
#     num=num//10
# print(squares)

#sum of cubes of each digit in a num
# num=154
# cubes=0
# while(num>0):
#     ld=num%10
#     cubes+=ld**3
#     num=num//10
# print(cubes)

#armstrong num

# 153=1x1x1 +5x5x5 +3x3x3

# 12345=1(5)+2(5)+3(5)+4(5)+5(5)

num=153
orgnl=num
length=len(str(num))
sum=0
while(num>0):
    ld=num%10
    sum+=ld**length
    num=num//10
print(sum)

if(sum==orgnl):
    print(f"{orgnl} is armstrong num")
else:
    print(f"{orgnl} is not a armstrong num")

#find maximum num in the given list
list=[4,7,1,2,8,9,10,1,3]






