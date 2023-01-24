#입력: 
A,B=map(int,input().split())

#문제: 
#A@B의 결과를 출력해주는 함수
def cal(A,B):
    print((A+B)*(A-B))

#조건:
if 1<=A<=100000 and 1<=B<=100000:
    if A<=1000 and B<=1000: #서브태스크 1
        #출력:
        cal(A,B)