# *****
# ****
# ***
# **
# *

# for x in range(5,0,-1):
#     row=""
#     for y in range(x):
#         row+="*"
#     print(row)

# 55555
# 4444
# 333
# 22
# 1

# for x in range(5,0,-1):
#     row=0
#     for y in range(x):
#         row=row*10+x
#     print(row)

# for x in range(5,0,-1):
#     row=0
#     for y in range(x+1):
#         row=row*10+y
#     print(row)

# for x in range(5,0,-1):
#     row=0
#     for y in range(x,0,-1):
#         row=row*10+y
#     print(row)


# 54321
# 5432
# 543
# 54
# 5

for x in range(5,0,-1):
    row=0
    for y in range(5,5-x,-1):
        row=row*10+y
    print(row)

# x=5
# y will start at 5 and ends at 5-x=5-5=0=before 0

# 1-->0*10+5=row=5
# 2-->5*10+4=row=54
# 3-->54*10+3=row=543
# 4-->543*10+2=5432
# 5--->5432*10+1=54321

# x=4
# y will start at 5 and ends at 5-4=1 = before 1
# 1-->0*10+5=row=5
# 2-->5*10+4=row=54
# 3-->54*10+3=row=543
# 4-->543*10+2=5432

# x=3
# y will start at 5 and ends at 5-3=2=before 2
# 1-->0*10+5=row=5
# 2-->5*10+4=row=54
# 3-->54*10+3=row=543

