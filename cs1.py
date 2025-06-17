# def find_largest(a,b,c): 
#     if a>b and a>c:
# 	    print("a is largest")
#     elif b>c:
# 	    print("b is largest")
#     else:
#         print("c is largest")

# find_largest(int(input("enter a value:")),int(input("enetr b value:")),int(input("enetr c value:")))

# def find_smallest(a,b,c): 
#     if a<b and a<c:
# 	    print("a is largest")
#     elif b<c:
# 	    print("b is largest")
#     else:
#         print("c is largest")

# find_smallest(int(input("enter a value:")),int(input("enetr b value:")),int(input("enetr c value:")))


a,b,c=10,8,3

largest_num= a if a>b and a>c else b if b>c else c

print(f"largest num is  {largest_num}")