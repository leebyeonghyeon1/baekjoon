Sugar = int(input())
Bag=0

if 3 <= Sugar <= 5000:
    pass

while Sugar >= 0:
    if Sugar % 5 == 0: # 5로 나눈 나머지가 0인 경우
        Bag += Sugar // 5 # 5로 나눈 몫 출력
        print(Bag)
        break

    # 설탕이 5의 배수가 될때까지, 3kg씩 담은 봉지 추가
    Sugar -= 3 
    Bag += 1
else:
    print(-1)
