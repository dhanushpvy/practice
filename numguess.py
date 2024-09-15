import random
n=random.randint(1,1000)
while(1):
    d=int(input("Enter Your Guessing(1 to 1000):"))
    if(d>n):
        print("high")
    elif(d<n):
        print("low")
    else:
        print("You Made It The Number Is:",n)
        break