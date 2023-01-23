T=int(input()) #T를 받는다.
if 1<=T<=1000:pass
for i in range(T) : #T만큼 반복
    R,S=input().split() #R과 S를 space바 차이로 구분해서 받는다.
    R=int(R) #R은 int형
    if 1<=R<=8: pass
    S=[R*num for num in S]#S의 각 자리를 R만큼 반복한 list
    if len(S)>1: pass
    for char in range(len(S)): #S의 자리 수 만큼 char이 0부터 증가
        print(S[char], end="")
    print()
