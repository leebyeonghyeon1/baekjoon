#입력: 첫째 줄에 행렬의 크기 N 과 M이 주어진다.
N, M = map(int,input().split())

if N<=100 and M<=100 : pass
A,B=[],[] #초기화

#Matrix A
for _ in range(N):
    row = list(map(int,input().split()))
    A.append(row) #N개의 row 생성

#Matrix B
for _ in range(N):
    row = list(map(int,input().split()))
    B.append(row) #N개의 row 생성

for row in range(N):
    for col in range(M):
        print(A[row][col]+B[row][col], end=" ")
    print()