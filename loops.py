# # # perform cleaning for 10 times

# # # for i in range(10):
# # #     print(i)


# # #range will contains 3 parameters
# # # if we give only one--->then it will act as a ending value.
# # # if we give two---->then first one is starting value and second one is ending value
# # # if we give three---->then 1st->start 2nd->end and 3rd->step 


# # # for x in range(1,10,2):
# # #     print(x)

# # # 2x1=2
# # # 2x2=4
# # # 2x3=6


# # for i in range(1,11):
# #     print(f"2x{i}={2*i}")

# # #write a function to print multiplication table using for loop


# # data="javascript"

# # for x in data:
# #     print(x+" - hi")


# # for x in range(0,len(data),2):
# #     print(data[x])

# # list=["Harish","Kiran","Hacker","Kranthi","Kumar","Harsha",]
# # #print every element from the list
# # # for i in list:
# # #     print(i)

# # #print alternative elements which names starts with h
# # for x in range(0,len(list),2):
# #     if(list[x][0]=="H"):
# #      print(list[x])

# # # print elements which names ends with r
# # for z in range(0,len(list)):
# #     if(list[z][-1]=="r"):
# #        print(list[z])
    
# dict={"name":"santhosh","gender":"male","location":"hyd","age":25}
# for a in dict:
#    print(f"{a} is {dict[a]}")

# # name is santhosh
# # gender is male
# # location is hyd
# # age is 25


# mobiles=["samsung","nokia","apple","realme","oneplus","oppo"]

# for mble in mobiles:
#     print(mble)

#print all mobile names only from this list of dictionaries

# mble_info=[{"name":"samsung","price":25000,"RAM":8}
#            ,{"name":"nokia","price":22000,"RAM":12}
#            ,{"name":"apple","price":15000,"RAM":4}
#            ,{"name":"oneplus","price":18000,"RAM":6}]

# for mble in mble_info:
#     if(mble["price"]>20000):
    #    print(mble["name"])


# print mobile names where price is more than 20000.


# mobiles = [
#     {"name": "Apple", "model": "iPhone 16 Pro Max", "ram": 8, "camera": "48MP + 48MP + 12MP", "price": 135900},
#     {"name": "Samsung", "model": "Galaxy Z Fold6", "ram": 12, "camera": "50MP + 12MP + 10MP", "price": 138990},
#     {"name": "Google", "model": "Pixel 9 Pro XL", "ram": 12, "camera": "50MP + 48MP + 48MP", "price": 124999},
#     {"name": "Vivo", "model": "X Fold3 Pro", "ram": 12, "camera": "50MP + 64MP + 50MP", "price": 87590},
#     {"name": "Samsung", "model": "Galaxy S25 Ultra", "ram": 12, "camera": "200MP + 50MP + 10MP + 50MP", "price": 117999},
#     {"name": "Xiaomi", "model": "15 Ultra", "ram": 12, "camera": "50MP + 50MP + 200MP", "price": 109998},
#     {"name": "OnePlus", "model": "10 Pro 5G", "ram": 8, "camera": "48MP + 50MP + 8MP", "price": 50199},
#     {"name": "Sony", "model": "Xperia 1 IV", "ram": 12, "camera": "12MP + 12MP + 12MP", "price": 108999},
#     {"name": "Apple", "model": "iPhone 16 Plus", "ram": 8, "camera": "Dual Primary Camera", "price": 126999},
#     {"name": "Vivo", "model": "X200 Pro", "ram": 12, "camera": "50MP + 50MP + 200MP", "price": 87590}
# ]

1.#print mobile dictionary which is having ram more than 8

2.#print mobile dictionary having ram more than 8gb and price lessthan 120000

# for x in range(5,0,-1): 
#     print(x)

# list=["hello","hi",'welcome',"something","frontend","backend"]

# for x in range(len(list)-1,-1,-1):
#     print(list[x])


# str="something"

# for char in range(len(str)-1,-1,-1):
#     print(str[char])


# #FOR CONTROLLING THE LOOPS, WE HAVE TWO STATEMENTS
# 1.BREAK --->STOPS/EXITS THE LOOP AT CERTAIN CONDITION
# 2.CONTINUE---->SKIP/IGNORE THE CURRENT ITERATION AT CERTAINN CONDITION AND CONTINUE WITH NEXT ITERATION




# x=[1,2,3,4,5,6,7,8,9,10]
# for i in x:
#     if i==5:
#         break
#     print(i)

# str="programming"

# for char in str:
#     if(char=='g'):
#         continue
#     print(char)

# subscription=30
# for x in range(subscription+1):
#     print(x)

#i did not mentioned where to start
#i did not mentioned how to count/update
#i did not mentioned where to stop

# while(conndition):
    #statement

# subscription=30
# day=1 #mention where to start
# while(day<=subscription): #mention where to stop
#     # print(day)
#     day+=1 #mention how to update
# print(day)

# x=["html","css","js","react","python","django"]
# i=0
# while(i<len(x)):
#     print(x[i])
#     i+=1

# i=len(x)-1 #5
# while(i>=0):
#     print(x[i])
#     i-=1



#even length strings

#odd length strings

#use while loop and break/continue