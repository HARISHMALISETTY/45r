
# fruit1,fruit2,fruit3,fruit4=["apple","banana","grapes","pineapple"]

# x,y,z,*res=["apple","banana",
#             "grapes","lemon",
#             "pineapple","guava",
#             "mango","kiwi",
#             "orange",
#             "strawberry"]

# print(y)

# def sample():
#     print("hello")
#     return "hii"
# print(sample())

#positional
#default params
#arbitrary--->whenever u dont count of args 
#keyword--->when u dont know seq/position of args
#kywordarbitrary-->when u dont know position and counr of args


# def sample(**x):
#     print(x)
# # sample(fn="ram",age=30,ln="charan")
# 1.how to unpack every element
# 2.how to unpack frst 3 elements
# 3.how to unpack frst 3 and last 3

# a,b,*c,d,e=[1,2,3,4,5,6,7,8]
# print(d)

# a,b,*x,y=[1,23,45,12,"a","x","hii"]

# print(a,b,x,y)

# a,b,*x=(1,2,3,4,5)
# print(a,b,x) #here rest of the nums stores in the form of list only

# a,b,*res,x,y=(7,8,9,"hii","python","java","kiran","naresh")
# print(res)

# x={1,2,3,4}
# x={"a","b","c","d"}
# print(x)

# num="hello"
# print(hash(num))

# set1={1,2,3,4,5}
# print(set1)

# set2={"hii","hello","python"}
# print(set2)

# a,b,*c={"dell","lenovo","hp","macbook","windows"}
# print(a,b,c)

# dict={"name":"kiran","age":25,"city":"hyd","blood_group":"b+ve"}
# a,*b,c=dict 
# print(c)

# list1={1,2,3,4}
# list2={5,6,7,8}
# op=list1|list2
# print(op)

#merging sets using unpacking
a={1,2,3}
c={4,5,6}
b={"hi","hello","some"}
# op={*a,*c,*b}
# print(op)

#merging two lists
x=[1,2,3]
y=[4,5,6]
# op=[*x,*y]
# print(op)

#merging two tuples
# t1=(1,4,5)
# t2=(9,10,34)
# otp=(*t1,*t2)
# print(otp)

# #merging dictionaries
# dict1={"key1":"value1"}
# dict2={"key2":"value2"}

# odt={**dict1,**dict2}
# print(odt)

# [1,2,3,4,5,6]

#comprehensions

# list=[1,2,3,4,5]
# op=[]

# 1.iterate every element
# 2.apply any operation
# 3.filter based on condition

#this is the code without comprehension
# for x in list:
#     y=x+2
#     if(y%2==0):
#         op.append(y)
# print(op)

#with comprehension

# combination of operation,
# iteration and filteration(optional) 
# in single line and can create new collection

# list1=["html","css","js","python"]

# op=[x.upper() for x in list1 if(len(x)<=3)]
# print(op)
# def even(num):
#     if(num%2==0):
#         return True #returnig a boolen value or  anum or a string

# op=[x for x  in range(1,10) if even(x)] 
# #creates a new collection 
# # with specific range of numbers
# print(op)

# sample(demo())

#create a collection of squares of numbers from 1 to 5
#Double each number in a list
#create a collection of length of the each string from a list of strings
#reverse each word and form a collection using slicing
def factorial(num):
    fact=1
    for x in range(1,num+1):
        fact=fact*x
    return fact #returns factorial of 1,2,3,4,5

# def perfect_num(num):
#     # print(num)
#     sum=0
#     for x in range(1,num):
#         if(num%x==0):
#             sum+=x
#     if(sum==num):
#         return True
#     else:
#         return False

# op={i:factorial(i) for i in range(1,5)}

# print(op)


# 1.iteration 
# 2.filteration 
# 3.operation