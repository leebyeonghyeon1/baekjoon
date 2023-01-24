#입력: 첫째 줄에 단어 S가 주어진다. 
S=input()
#입력 조건: 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.
# if 1<=int(len(S))<=100 and S.islower() and S.isdecimal() :

#문제:  각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램

#a~z범위 문자를 각각 해당하는 정수로 list화
alphabet=list(range(ord('a'),ord('z')+1))
#각각의 알파벳이 인덱스에 맞는 값을 갖도록 할당
for x in alphabet:
    print(S.find(chr(x)),end=" ") #출력