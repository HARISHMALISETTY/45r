# # life/ accessibility of a 
# # variable in Python is determined by its scope.

# # hero="Ramcharan" # hero is a global variable

# # def tollowood():
# #     actor='Allari naresh' # actor is a local variable
# #     print(hero,actor)
# # tollowood()

# # def kollywood():
# #     print(hero)
# # kollywood()

# # def bollywood():  
# #      print(hero)
# # bollywood

# def kollywood():
#     hero='surya'
#     def tollywood():
#         print(hero)
#     tollywood()
#     print(hero)
# kollywood()

y=20 # y is a global scope variable

# def sample(): 
#     x=10  #local scope variable  
#     return 'hello world'
# print(sample()) 

x=5 # x is a global scope variable
def func1():
    a=5 # enclosing scope variable
    def func2():
        b=10 #local scope variable for func2
        print( a + b)  # Accessing variable 'a' from the outer function
    func2()
func1()  # Calling func1 to execute the inner function func2
