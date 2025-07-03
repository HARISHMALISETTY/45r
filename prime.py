def prime_check(num):   
    if num==1:
        print(f"{num} is neither prime nor composite")
    elif num<0:
        print("only positive integers allowed")
    else:
        is_Prime=True
    for x in range(2,num):
        if(num%x==0):
            is_Prime=False
            break
    if(is_Prime):
        # print(f"{num} is prime")
        return True
    else:
    #  print(f"{num} is not prime")
        return False

# prime_check(15)

def prime_range(s,e):
    for x in range(s,e+1):
        if(prime_check(x)):
            print(x)
prime_range(10,30)
# task
#using comprehensions-->create collection of prime numbers  in certain range
