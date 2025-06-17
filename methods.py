import math,random

# x=-5.25
# op=math.trunc(x)

# print(op)

# x=-6
# op=math.fabs(x) #return absolute value by ignoring sign as a floating value.

# print(op)
 #it is the simple code for generaing 4 digit otp.
# x=random.randint(10,10000)
# print(x)

# y=random.random() #generate floating values b/w 0 and 1
# print(y)

# z=random.uniform(5,8)
# print(z)

# ip=[1,2,3]

# op=random.choice(ip)
# print(op)

#write a function to return 6 digit otp.

# print(random.randint(1,9))


# str="hEllO"

# op=str.lower() #it is used to convert into lowercase
# op1=str.upper() #it is used to convert into uppercase


# k=["HELLO","hi","PYTHON","css","js","react","DJANGO"]

# print("uppercase")
# for x in k:
#     if(x==x.upper()):
#         print(x)

# print("lowercase")
# for y in k:
#     if(y==y.lower()):
#         print(y)


# str="hello world"
# op=str.capitalize()
# print(op)

# str1="hello world some thing"
# op1=str1.title()
# print(op1)

# str2="javaSCRipT"
# op2=str2.swapcase()
# print(op2)

# str="    welcome   "
# print(len(str))
# op=str.strip() #it is removing white space both sides if the string
# op=str.lstrip() #it is removing white space at starting of the string.
# op=str.rstrip() #it is removing white space at the ending of the string
# print(len(op))
# print(op)

# str="JAGAN is the C.M of AP."
# op=str.replace("JAGAN","CBN")
# print(op)

# line="kingdom"
# op1=line.replace("ki","pi")
# print(op1)

# ip="wlcom"

# op=ip.find("e")
# print(op)

# statement="python is easy to learn"
# op=statement.find("easy")
# print(op)

# skills=["python-eAsy",
#         "java-difficult",
#         "js-easY",
#         "react-Easy",
#         "html-EASY",
#         "git-moderate"]



# skills=["python-eAsy   ",
#         "java-difficult",
#         "   easY-js",
#         "react-Easy   ",
#         "   EASY-html",
#         "git-moderate"]

# print the strings which are having easy as a substring 

#lower(),strip(),find()
#rfind() is used to last occurance of the character in a string.

# str="welcome hello"
# op=str.rfind("e")
# print(op)

# str="pyrthtonysq"
# op=str.rfind("t",3,6)
# print(op)

#in find,rfind and index, we have additional two parameters-->
# start and (end-1) points for searching.

# op1=str.count("y",4,10)
# # print(op1)

# st_name="53r-karthik"
# op2=st_name.startswith("45r")
# print(op2)

# list_of_students=["45r-karthik","45r-alekya","45r-harish","45r-anusha","53r-sukumar","53r-sandhya","53r-suresh"]

# print("45r-students list")
# for student in list_of_students:
#     if(student.startswith("45r")):
#         print(student)

# print("53r-students list")

# for stud in list_of_students:
#     if(stud.startswith("53r")):
#         print(stud)



# str="alpha123betic"

# op=str.isalpha() # returns true if all are alphabetes
# print(op)

# str1="1234"
# op1=str1.isdigit() #returns true if all are numeric values
# print(op1)


# str2="abc123"
# op2=str2.isalnum() #returns true if contains both numeric and alphabetic
# print(op2)

# list1=[1,2,3,4,5]

# list1.append(6)
# print(list1) #updated list by adding 6 at the end of the list.

# ip=["123","456","abc","a12b","xyz456","xyz"]
# digit=[]
# alpha=[]
# alnum=[]
# for i in ip:
#     if(i.isdigit()):
#         digit.append(i)
#     elif(i.isalpha()):
#         alpha.append(i)
#     else:
#         alnum.append(i)
# print(f"digit={digit}")
# print(f"alpha={alpha}")
# print(f"alnum={alnum}")


# # str="hHllo"
# str="Hello World"
# #op=str.islower()
# # op=str.isupper()
# # op=str.istitle()

# print(op)


#split is used to split the characters by seperator from a string and insert into a list.

# str="s-o-m-e"
# op=str.split("-")
# print(op)

# str1="s_o_m_e_t_hing"
# op1=str1.split("_",3)
# print(op1)

# str1="some*thin_h_k_*k"
# op1=str1.split("_")
# print(op1)

# studs="kiran*kumar*vikky*shiva*naresh*shafi"
# op2=studs.split("*")
# op2=studs.split("*",3)
# op1=studs.split("*",3)
# op2=studs.rsplit("*",3)
# print(op1,"left split")
# print(op2,"right split")

# ["kiran","kumar","vikky","shiva","naresh","shafi"]

# mul_str="""hello
# 45r
# welcome"""
# op_mul=mul_str.splitlines()
# print(op_mul)

# seq={"js","python","sql"}
# op="HELLO".join(seq)
# print(op)

# str="hello {name} welcome to {city}"
# op=str.format(name="john",city="hyd")
# op1=str.format(name="harish",city="bnglr")
# print(op)
# print(op1)
