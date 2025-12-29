#brute force
contributions=list(map(int,input().split()))
l1=[]
for i in range(len(contributions)):
    prod=1
    for j in range(len(contributions)):
        if i!=j:
            prod*=contributions[j]
    l1.append(prod)
print(l1)    

    