#Sorting the List By The Count of Upper Case
n=int(input())
l=[]
f=[]
for i in range(n):
    l.append(input().strip())
for i in l:
    c=0
    for j in i:
        if(j.isupper()): 
            c+=1
    f.append(c)
for i in range(n):
    r=max(f)
    for j in range(n):
        if(r == f[j]):
            print(l[j])
            f[j]=-1