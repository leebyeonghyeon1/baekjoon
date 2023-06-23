# 프로그램: 최단 거리 방을 배정
## floor와 room을 각각 계산 후, 이어붙여서 출력

# variable
T = int(input())  # 테스트 데이터

for i in range(T):
    # 호텔의 층 수, 각 층의 방 수, 몇 번째 손님
    H, W, N = map(int, input().split())

    ##H,W만큼 돌고 다시 처음으로 돌아가니까 나머지, 몫으로 계산
    floor = N % H
    room = N // H + 1

    # N이 H의 배수일 때
    if floor == 0:
        room = N // H
        floor = H

    print(floor * 100 + room)
