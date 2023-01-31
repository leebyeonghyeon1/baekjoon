#입력: 2차원 평면 위의 점 N개
n=int(input())

pos=[]
for _ in range(n): 
    x,y=map(int, input().split())
    pos.append([y, x])
pos.sort()

for y, x in pos:
    print(x, y)