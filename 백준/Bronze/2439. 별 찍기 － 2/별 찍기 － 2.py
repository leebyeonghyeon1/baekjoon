a=int(input())

if 1<=a<=100:pass #조건

for i in range(1,a+1): #받은 정수만큼 반복
    print(" "*(a-i) + "*"*i) 