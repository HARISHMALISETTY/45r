# recursion:
# A function calling itself continuosly until a 
# certain condition meets is called recursion

def open_gift_box(n):
    print(f" {n}th box opened")
    if n==1:
        print("found gift")
    else:
        open_gift_box(n-1)
open_gift_box(5)

#sunny num and neon num-->how to check


