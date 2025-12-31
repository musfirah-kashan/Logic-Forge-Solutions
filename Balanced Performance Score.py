#brute force
scoresA=list(map(int,input().split()))
scoresB=list(map(int,input().split()))
total=scoresA+scoresB
total.sort()
n=len(total)
if n%2==0:
    median=(total[n//2-1]+ total[n//2])/2
else:
    median=(total[n//2])
print(median)        