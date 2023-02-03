N = []
rev_N = []

while 1:
    N = list(map(int, str(input())))  # 각 자리별로 리스트에 저장
    if [0] == N:
        break
    for i in N[::-1]:
        rev_N.append(i)
    ans = 'yes' if N == rev_N else 'no'
    print(ans)

    N = []
    rev_N = []
