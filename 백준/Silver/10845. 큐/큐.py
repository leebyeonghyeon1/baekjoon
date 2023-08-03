import sys
# ! 시간 초과: input() => sys.stdin.readline()을 쓰기
N = int(sys.stdin.readline())  # N: 명령의 수
items_queue = []
for _ in range(N):  # N번 반복하는 입력 실행
    cmd = sys.stdin.readline().split()
    com = cmd[0]  # com: 명령
    num = None  # num: 처리할 정수

    # 명령 처리
    if len(cmd) == 2:
        num = int(cmd[1])  # num: 처리할 정수

    if com == "push":
        items_queue.append(num)
    elif com == "pop":
        print(items_queue.pop(0) if items_queue else -1)
    elif com == "size":
        print(len(items_queue))
    elif com == "empty":
        print(int(not items_queue))
    elif com == "back":
        print(items_queue[-1] if items_queue else -1)
    elif com == "front":
        print(items_queue[0] if items_queue else -1)
