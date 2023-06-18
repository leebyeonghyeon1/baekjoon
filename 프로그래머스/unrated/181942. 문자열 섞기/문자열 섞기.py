def solution(str1, str2):
    ansList = [] #번갈아 담을 문자열 리스트 생성
    for i in range(len(str1)):
        #str1,str2를 리스트화. 각각의 인덱스 담기
        ansList.append(list(str1)[i]) 
        ansList.append(list(str2)[i])

    answer = "".join(ansList) #리스트 인덱스를 구분문자 없는("구분문자") 하나의 문자열로 만들기
    
    return answer