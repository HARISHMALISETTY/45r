# 1.what will be the output of the following code?and explain why?

# x = 10
# def show():
    
#     print(x)
# show()
# print(x)

# 2.what will be the output of the following code?and explain why?

# def outer():
#     x = 10
#     def inner():
#         print(x)
#     inner()

# outer()

# 3. What will be the output of the following code? And explain why?

# x = "global"
# def outer():
#     global x
#     x = "global changed"
#     def inner():
#         global x
#         x = "global changed"
#         # print(x)
#     inner()
#     # print("outer:", x)
# outer()
# print("global:", x)



# x=5
# def sample():
#     # x=6
#     global x #decleration of x as global variable    
#     x+=5
#     print(x)
# sample()



# x="harish"
# print(x)
# def sample():
#     global x 
#     x="kiran" #here iam updating the global variable x
#     print(x)
# sample()
# print(x)  



print("hello world") 
print("welcome to python programming")
