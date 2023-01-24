#입력: 첫 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 10)가 주어진다.
T=int(input())
if 1 <= T <= 10 : pass

firstLetter=[]
lastLetter=[]
# 문자열은 알파벳 A~Z 대문자로 이루어지며 알파벳 사이에 공백은 없으며 문자열의 길이는 1000보다 작다. 
for _ in range(T):
    #  각 테스트 케이스는 한 줄에 하나의 문자열이 주어진다.
    string = input()
    #문자열은 알파벳 A~Z 대문자로 이루어짐
    if string.isupper()==True : pass
    #문자열의 길이는 1000보다 작다.
    if len(string)<1000: pass
    firstLetter.append(string[0])
    lastLetter.append(string[-1])

#출력: 각 테스트 케이스에 대해서 주어진 문자열의 첫 글자와 마지막 글자를 연속하여 출력한다.
for i in range(T):
    print(firstLetter[i] + lastLetter[i])