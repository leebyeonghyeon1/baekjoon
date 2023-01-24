#입력#
#첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다.
word=input().upper()
max=0
#조건#
#주어지는 단어의 길이는 1,000,000을 넘지 않는다.

#가장 많이 사용된 알파벳 찾기
# 1. 입력된 알파벳들의 집합 생성
s=set(word)
# 2. 입력된 알파벳을 꺼내서  몇 번 나왔는지 세기
for alphabet in s:
    tmp=word.count(alphabet)
# 3. 가장 높은 빈도의 알파벳의 수를 max에 저장하고, 더 높은 빈도 수 찾으면 max를 새로 갱신
    if max<tmp :
        max=tmp
        result=alphabet #알파벳 저장
#가장 많이 사용된 알파벳이 여러 개 일 때, ?로 나타내게 함.
    elif max==tmp:
        result="?"
#출력#
#이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력
print(result)