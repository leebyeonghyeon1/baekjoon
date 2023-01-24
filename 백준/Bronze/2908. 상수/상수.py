#입력
A,B=map(int,input().split())
#조건;세 자리 수
if 100<=A<=999 :
    if 100<=B<=999 :
        #조건;같지 않아야 함
        if A!=B :
            #조건;0이 포함되지 않아야 함
            if not '0' in str(A):
                if not '0' in str(B):
                    #문자열 뒤집기(슬라이싱기능 사용)
                    A=int(str(A)[::-1])
                    B=int(str(B)[::-1])
                    result=A if A>B else B
                    print(result)