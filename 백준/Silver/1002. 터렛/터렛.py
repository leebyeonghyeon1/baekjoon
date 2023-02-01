import math

T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if d == 0 and r1 == r2:  # 동심원(중심 일치), 반지름이 같을 때. 즉, 합동
        print(-1)
    elif abs(r1-r2) < d < (r1+r2):  # 두 점에서 만날 때
        print(2)
    elif abs(r1-r2) == d or r1+r2 == d:  # 내접, 외접일 때
        print(1)
    else:
        print(0)  # 만나지 않을 때
