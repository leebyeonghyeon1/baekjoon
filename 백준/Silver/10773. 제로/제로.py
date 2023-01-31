K=int(input())
if 1 <= K <= 100000:pass
klist=[0]
for _ in range(K):
    i=int(input())
    if i==0:
        klist.pop()
    else :
        klist.append(i)
print(sum(klist))