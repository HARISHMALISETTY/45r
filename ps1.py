# 1.write a program to find whether input num is even or odd?

# num=5
# if(num%2==0):
#     print("it is a even number")
# else:
#     print("it is an odd number")

#using bitwise operators

# num=int(input("enter num : "))

# if(num & 1==0):
#     print("it is even")
# else:
#     print("it is odd")

#using sequences
# num=12548901357
# cnvrted=str(num)
# seq="02468"

# if(cnvrted[-1] in seq):
#     print("even")
# else:
#     print("odd")


#num is palindrome or not.

# 121,252,343,12521,12321,123454321....

# num=12121
# cnvrt=str(num)
# rev=''
# for i in range(len(cnvrt)-1,-1,-1):
#     rev=rev+cnvrt[i]
# print(rev)
# if(int(rev) == num ):
#     print("it is palindrome")
# else:
#     print("not a palindrome")


# num=125
# rev=0
# orgnl=num
# while num>0:
#     ld=num%10  #last digit
#     rev=rev*10+ld #adding that last digit to rev
#     num=num//10 #reducing number
# print(rev,num)
# if(rev==orgnl):
#     print("num is palindrome")
# else:
#     print("num is not palindrome")


ip=567
count=0
while ip>0:
    ld=ip%10
    count+=ld
    ip=ip//10
print(count)
