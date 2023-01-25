#입력: 첫째 줄에 시험 본 과목의 개수 N이 주어진다. 
N=int(input())
#이 값은 1000보다 작거나 같다. 
if N<=1000: pass
#둘째 줄에 세준이의 현재 성적이 주어진다. 
score_list = list(map(int, input().split()))
#이 값은 100보다 작거나 같은 음이 아닌 정수이고, 적어도 하나의 값은 0보다 크다.
for i in range(N):
    if 0<=score_list[i]<=100:pass
if sum(score_list)>0 : pass
#문제: 
M=max(score_list) #최고점
#모든 점수를 점수/M*100으로
new_score_list=[float(int(score)/int(M)*100) for score in score_list]
#새로운 평균
avg=sum(new_score_list)/N
#출력:
print(avg)