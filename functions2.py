# # # def sample(name,age,nationality="indian"):
# # #     print(name,age,nationality)

# # # sample("sahith",25,"foreigner")

# # # #there is no need to pass arguments for default parameters
# # # #but if we pass arguments for default parameters, then the passed arguments will override the 
# # # #default parameters


# # # def sample(*num):
# # #     print(num)

# # # sample(1,2,3,4,5,6)


# # # def sample(a,b,c,*num):
# # #     print(a,b,c,num)
# # # sample(1,2,3,4,5,6,7,8,9)


# # def student(name, age,location):
# #     print(f"Name: {name}, Age: {age}, Location: {location}")

# # student(age=25,location="hyderabad",name="suresh") 
# # # keyword arguments allow you to pass arguments in any order

# # #if we dont know the number of arguments to be passed, we can use *args
# # # if we  dont know the order of the arguments to be passed,
# # #  we can use keyword arguments

# # # **kwargs
# # # *args 
# # # kwargs


# def student(*stud_info):
#     print(stud_info)

# # student(name="kiran",age=25,gender="male",location="secunderabad",)
# student("kiran",25,"male","secunderabad")


sample=lambda x: 2*x


print(sample(5))

# print(sample(5))
# print(sample(10))

#lambda does not have a name, it is an anonymous function
#lambda wont use return statement, it will return the value directly

