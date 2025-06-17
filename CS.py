# print("statement1")
# print("statement2")
# a=5
# b=10
# if(a>b):
#     print("statement3")
# print("statement4")

# a=10
# if(not a<5):
#     print("true statement")
# else:
#     print("false statement")

# def match_status(team, match_won):
#     if(match_won):
#         print(f"{team} won the match")
#     else:
#         print(f"{team} lost the match")

# match_status("SRH", True)
# match_status("CSK", False)
# match_status("RCB", True)
# match_status("MI", False)

# def login_system(email,password):
#     if(email =='harish@gmail.com' and password == 'Harish@123'):
#         print("Login successful")
#     else:
#         print("Login failed")

# input_email = input("Enter your email: ")
# input_password = input("Enter your password: ") 
# login_system(input_email, input_password)


# if-elif-else statements are used to execute a block of code based on a more conditions.


# if(condition is true):
#     # execute this block of code
#     print("Condition is true")
# elif(condition is true):
#     # execute this block of code
#     print("Condition is true")
# else:
#     # execute this block of code
#     print("Condition is false")

# def check_number(num):
#     if(num > 0):
#         print("Positive number")
#     elif(num < 0):
#         print("Negative number")
#     else:
#         print("Zero")
# ip=int(input("Enter a number: "))
# check_number(ip)

def college_selection_basedon_rank(eamcet_status,rank=0):
    if(eamcet_status==True):
        if(rank<=10000):
            print("got seat in JNTUH")
        elif(rank>10000 and rank<=25000):
            print("got seat in MALLAREDDY")
        elif(rank>25000 and rank<=50000):
            print("got seat in SRI INDHI ENG COLLEGE")
        else:
            print("got seat in local eng college")
    else:
        print("either re-attempt or join in b.com/b.sc")

# college_selection_basedon_rank(True,10000)
# college_selection_basedon_rank(False)

# def login_system(login,user_role):
#     if(login == True):
#         if(user_role == "admin"):
#             return "Welcome Admin"
#         else:
#             return "Welcome User"
#     else:
#         return "Go and login first"    
# print(login_system(True, "user"))

# if having knowledge on f.e+b.e+db--->full stack developer
# else having knowledge on f.e---> front end developer
# else having knowledge on b.e---> back end developer
# else having knowledge on db---> database developer
# else no knowledge---> go and join in 10000coders


# TERINARY OPERATOR

# we will use terinary operator for short statements and also assigning value 
# to variable based on condition.

# print("true statement") if True else print("False statement")

# a=5
# x=4 if a>10 else 5
# print(x)

# a=3
# b=4

# print("a is largest than b") if a>b else print (" b is greater than a")






a,b,c=5,8,2
if a<b and a<c:
	print("a is smallest")
elif b<c:
	print("b is smallest")
else:
     print("c is smallest")