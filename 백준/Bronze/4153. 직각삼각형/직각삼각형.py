# variable
hypotenuse = 0  # 빗변
hyp = hypotenuse


while True:
    leg = list(map(int, input().split())) #변

    if sum(leg) == 0:
        quit()

    hyp = max(leg)  # 가장 큰 수를 빗변으로 할당
    leg.remove(hyp)

    if hyp**2 == leg[0] ** 2 + leg[1] ** 2:
        print("right")
    else:
        print("wrong")
