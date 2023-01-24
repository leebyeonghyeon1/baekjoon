#문제: 입력 받은 대로 출력하는 프로그램
while True:
    #출력: 입력받은 그대로 출력한다.
    try:
        #예외 발생할 수도 있는 코드
        print(input())
    except EOFError: #입력 끝남 에러
        #예외 발생시 실행되는 코드
        break #나가