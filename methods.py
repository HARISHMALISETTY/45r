# import math,random,copy

# # x=-5.25
# # op=math.trunc(x)

# # print(op)

# # x=-6
# # op=math.fabs(x) #return absolute value by ignoring sign as a floating value.

# # print(op)
#  #it is the simple code for generaing 4 digit otp.
# # x=random.randint(10,10000)
# # print(x)

# # y=random.random() #generate floating values b/w 0 and 1
# # print(y)

# # z=random.uniform(5,8)
# # print(z)

# # ip=[1,2,3]

# # op=random.choice(ip)
# # print(op)

# #write a function to return 6 digit otp.

# # print(random.randint(1,9))


# # str="hEllO"

# # op=str.lower() #it is used to convert into lowercase
# # op1=str.upper() #it is used to convert into uppercase


# # k=["HELLO","hi","PYTHON","css","js","react","DJANGO"]

# # print("uppercase")
# # for x in k:
# #     if(x==x.upper()):
# #         print(x)

# # print("lowercase")
# # for y in k:
# #     if(y==y.lower()):
# #         print(y)


# # str="hello world"
# # op=str.capitalize()
# # print(op)

# # str1="hello world some thing"
# # op1=str1.title()
# # print(op1)

# # str2="javaSCRipT"
# # op2=str2.swapcase()
# # print(op2)

# # str="    welcome   "
# # print(len(str))
# # op=str.strip() #it is removing white space both sides if the string
# # op=str.lstrip() #it is removing white space at starting of the string.
# # op=str.rstrip() #it is removing white space at the ending of the string
# # print(len(op))
# # print(op)

# # str="JAGAN is the C.M of AP."
# # op=str.replace("JAGAN","CBN")
# # print(op)

# # line="kingdom"
# # op1=line.replace("ki","pi")
# # print(op1)

# # ip="wlcom"

# # op=ip.find("e")
# # print(op)

# # statement="python is easy to learn"
# # op=statement.find("easy")
# # print(op)

# # skills=["python-eAsy",
# #         "java-difficult",
# #         "js-easY",
# #         "react-Easy",
# #         "html-EASY",
# #         "git-moderate"]



# # skills=["python-eAsy   ",
# #         "java-difficult",
# #         "   easY-js",
# #         "react-Easy   ",
# #         "   EASY-html",
# #         "git-moderate"]

# # print the strings which are having easy as a substring 

# #lower(),strip(),find()
# #rfind() is used to last occurance of the character in a string.

# # str="welcome hello"
# # op=str.rfind("e")
# # print(op)

# # str="pyrthtonysq"
# # op=str.rfind("t",3,6)
# # print(op)

# #in find,rfind and index, we have additional two parameters-->
# # start and (end-1) points for searching.

# # op1=str.count("y",4,10)
# # # print(op1)

# # st_name="53r-karthik"
# # op2=st_name.startswith("45r")
# # print(op2)

# # list_of_students=["45r-karthik","45r-alekya","45r-harish","45r-anusha","53r-sukumar","53r-sandhya","53r-suresh"]

# # print("45r-students list")
# # for student in list_of_students:
# #     if(student.startswith("45r")):
# #         print(student)

# # print("53r-students list")

# # for stud in list_of_students:
# #     if(stud.startswith("53r")):
# #         print(stud)



# # str="alpha123betic"

# # op=str.isalpha() # returns true if all are alphabetes
# # print(op)

# # str1="1234"
# # op1=str1.isdigit() #returns true if all are numeric values
# # print(op1)


# # str2="abc123"
# # op2=str2.isalnum() #returns true if contains both numeric and alphabetic
# # print(op2)

# # list1=[1,2,3,4,5]

# # list1.append(6)
# # print(list1) #updated list by adding 6 at the end of the list.

# # ip=["123","456","abc","a12b","xyz456","xyz"]
# # digit=[]
# # alpha=[]
# # alnum=[]
# # for i in ip:
# #     if(i.isdigit()):
# #         digit.append(i)
# #     elif(i.isalpha()):
# #         alpha.append(i)
# #     else:
# #         alnum.append(i)
# # print(f"digit={digit}")
# # print(f"alpha={alpha}")
# # print(f"alnum={alnum}")


# # # str="hHllo"
# # str="Hello World"
# # #op=str.islower()
# # # op=str.isupper()
# # # op=str.istitle()

# # print(op)


# #split is used to split the characters by seperator from a string and insert into a list.

# # str="s-o-m-e"
# # op=str.split("-")
# # print(op)

# # str1="s_o_m_e_t_hing"
# # op1=str1.split("_",3)
# # print(op1)

# # str1="some*thin_h_k_*k"
# # op1=str1.split("_")
# # print(op1)

# # studs="kiran*kumar*vikky*shiva*naresh*shafi"
# # op2=studs.split("*")
# # op2=studs.split("*",3)
# # op1=studs.split("*",3)
# # op2=studs.rsplit("*",3)
# # print(op1,"left split")
# # print(op2,"right split")

# # ["kiran","kumar","vikky","shiva","naresh","shafi"]

# # mul_str="""hello
# # 45r
# # welcome"""
# # op_mul=mul_str.splitlines()
# # print(op_mul)

# # seq={"js","python","sql"}
# # op="HELLO".join(seq)
# # print(op)

# # str="hello {name} welcome to {city}"
# # op=str.format(name="john",city="hyd")
# # op1=str.format(name="harish",city="bnglr")
# # print(op)
# # print(op1)

# # op="hello {1} welcome to {0} after {2} years".format("sai","hyd",5)

# # op="hello {name} welcome to {city} after {gap} years".format(name="sai",city="hyd",gap=5)
# # print(op)

# #list methods

# # ip=[1,2,3]
# # ip.append({"name":"harish","city":"hyd"})
# # print(ip)
# # ip.append(4) #adding sinle element at the end of the list
# # ip.append(4,6,8,9) #this cant possible in append
# #using append we can add single num/string/list/tuple/set/dictionary into existing list.

# # op=ip.append(5) #append will not return anything, it will just add a new element at the end of the list.
# # print(op)

# # op=ip.extend((4,5,6)) #this will allows
# # ip.extend(4) #it wont allows in extend
# # print(ip)

# #we can add multiple elements at a time into the existing list by passing elements in the form of list/tuples.
# #extend method doesn't return anything. it will just add elements.
# #we can use list/tuples/sets/dictionaries as a argument for the extend

# # skills=["html","css","js","python","react"]
# # # op=skills.insert(2,"django")
# # # skills.insert(2,"django","aws") #it wont take more than 2 arguements\
# # skills.insert(2,["aws","angular"])

# # print(skills)
# # print(op)
# #with the help of index, we can add the element at particular index without removing/replacing existing ones
# #insert method will modify existing list but does not returns anything.

# # ip=[1,2,3,3,2,1]
# # op=ip.remove(1) 
# # #it will remove only first match of the argument and doesn't returns anything
# # print(op)


# # ip=[1,5,7,6,4,8,1,2]
# # op=ip.pop(2)
# # this will removes the elements based on the index we passes as a arguement.and return the popped out element
# # ip.pop(-2) #if we didnt mention index in argument , it will automatically removes last element from the list
# # # print(ip)
# # op=ip.clear() #clear all the items from the list and return nothing.
# # print(op)
# # op=ip.index(8,1,4)
# #index method will search for the element in the list. if the element available then returns the index of the value
# # otherwise throw an error
# #additinally we cam also pass starting and ending positions for searching
# # print(op)

# # op=ip.count(1)
# # print(op)

# nums=[45,34,12,13,19,49]
# # op=nums.sort() #it will do ascending
# # nums.sort(reverse=True) #it will do descending
# # print(nums)

# #sort method will modifies existing list by sorting the elements in ascending order.and it doesn't returns anything
# # fruits=["banana","apple","pineapple","watermelon"]
# # fruits.sort()
# # print(fruits)
# nums.reverse() #it will just reverse the list
# # print(nums)

# #shallow copy and deep copy.
# # ip1=[[1,2],[5,6]]
# # ip2=ip1.copy()


# # ip2[0][1]="hi"

# # print(ip1,ip2)

# # ip1=[["hi","hello"],["js","python"]]
# # ip2=copy.deepcopy(ip1)

# # ip2[0][1]="bye"

# # print(ip1,ip2)

# # list1=[1,2,3,[4,5,6,["hi"]]]
# # print(list1[3][3][0])

# # tp1=(1,2,3,4,5,4,"hi",9,4)

# # #count()
# # op=tp1.count(4)
# # # print(op)

# # #index()
# # op1=tp1.index(120)
# # print(op1)


# # sets and frozenset
# # #add,remove,update,clear,discard,pop,copy


# # setA={1,2,3,4}

# # setA.add(5) #add the element into the set 

# # print(setA)

# # setA.remove(2) #remove element from set

# # print(setA)

# # setA.update({8,9,10}) #we can add multiple elements at a time by passing them as list/tuples/sets

# # print(setA)

# # setB=setA.copy() #to make shallow copy of original set
# # # print(setB)
# # setA.pop()
# # print(setA)


# setA={"abc","xyz","123","hello","ytj"} 

# # setA.pop()#it will remove a random element from the set

# # setA.pop("xyz") # arguements can not accepts here.
# # print(setA)
# # setA.remove("abcd") #if arugumented value is not present in the set, it will throw error but discard won't
# print(setA)
# setA.clear() #clears the entire set and makes empty set
# print(setA)


#union

setA={1,2,3,4}
setB={12,13,50,120,2}
# setC=setA.union(setB) #combines all the values from both the sets
# setC=setA.intersection(setB) #takes only common unique elements from the both sets
# setC=setB.difference(setA) #check the different element in setB by comparing with setA
# setC=setA.difference(setB) #check the different element in setA by comparing with setB
is_subset=setA.issubset(setB) #checking all the values of setA are available in setB or not
is_superset=setB.issuperset(setA) 
# checking all the  values of setA are available 
# in setB or not to check whether setB is superset or not
is_disjoint=setA.isdisjoint(setB) #to check common elements are available or not in two sets
setC=setA.symmetric_difference(setB) #take elements which are not common in boths sets. opposite to intersection
print(setC)