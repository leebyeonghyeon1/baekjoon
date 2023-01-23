#T:테스트 케이스의 개수(1<=T<=1000)
#R:반복횟수(1<=R<=8)
#S:문자열(S>1)
T=int(input()) #T를 받는다.
for i in range(T): #T만큼 반복
    R,S=input().split() #R과 S를 space바 차이로 구분해서 받는다.
    R=int(R) #R은 int형
    S=[R*num for num in S]#S의 각 자리를 R만큼 반복한 list
    for char in range(len(S)): #S의 자리 수 만큼 char이 0부터 증가
        print(S[char], end="")
    print()
 
