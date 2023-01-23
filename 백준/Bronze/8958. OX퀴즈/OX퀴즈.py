repeat = int(input())
for i in range(repeat):
    str = list(input())
    total = 0
    C = 1 #연속 합
    for i in str:
        if i == 'O':
            total += C
            C += 1
        else:
            C = 1
            
    print(total)