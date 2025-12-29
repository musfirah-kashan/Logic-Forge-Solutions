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

#optimized method
def team(contributions):
    n=len(contributions)
    right_prod=[1]*n
    left_prod=[1]*n
    impact=[1]*n
    left=1
    for i in range(n):
        left_prod[i]=left
        left*=contributions[i]
    right=1
    for i in reversed(range(n)):
        right_prod[i]=right
        right*=contributions[i]
    for i in range(n):
        impact[i]=left_prod[i]*right_prod[i]
    return impact            
contributions=list(map(int,input().split()))
print(team(contributions))
