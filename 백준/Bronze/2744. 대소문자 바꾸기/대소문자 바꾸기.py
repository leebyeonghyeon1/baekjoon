#입력: 영어 소문자와 대문자로 이루어진 단어
word=input()
answer=""
#문제: 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력
for x in word:
    #소문자면, 대문자로 변경
    if x.islower():
        answer+=x.upper()
    else:
        answer+=x.lower()

#조건: 단어의 길이는 최대 100
if len(word)<=100:pass
#출력
print(answer)