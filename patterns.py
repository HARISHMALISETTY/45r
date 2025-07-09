# AJAY RAO
# SHIVA LINGA
# TEJA
# PRASHANTHI
# shreeja
# sandhya
# poojitha
# Anitha J
# nani
# ravindra chowdary
# salman
# persis 
# uday kiran 
# anusha


for x in range(1,6):
    row=""
    for y in range(x):
        row+="*"
    print(row)

for x in range(1,6):
    row=0
    for y in range(x):
        row=row*10+x
    print(row)
# 1
# 22
# 333
# 4444
# 55555

for x in range(1,6):
    row=0
    for y in range(1,x+1):
        row=row*10+y
    print(row)

# x-->1
# row=0
# y-->1 time starts with 0
# 1.row=0*10+0-->prints 0

# x--->2
# row=0
# y--->2 times starts from 0
# 1.row=0*10+0--->0
# 2.row=0*10+1--->1

# x--->3
# row=0
# y-->3 times starts from 0
# 1.row=0*10+0-->0
# 2.row=0*10+1-->1
# 3.row=1*10+2--->12





# x-->1
# 0*10+a-->1

# x-->2
# row=0
# 1.0*10+2--->2
# 2.2*10+2--->22

# x--->3
# row=0
# 1.0*10+3-->3
# 2.3*10+3--->33
# 3.33*10+3--->333
# # 1
# # 12
# # 123
# # 1234
# # 12345





# x=1
# row=""
# y-->1 time--->row-->*

# x=2
# row=""
# y-->2
# row="*"
# row="**"

# x=3
# row=""
# y--->3 "***"

# x=4
# row=""
# y--->4 "****"

# 1,2,3
# 123
# 1*10+2-->12
# 12*10+3-->123