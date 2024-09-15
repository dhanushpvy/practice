a=0
b=1
n=int(input())
for i in range(n):
    print(a,end=' ')
    t=b
    b=a+b
    a=t