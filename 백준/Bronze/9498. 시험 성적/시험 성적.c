//9498 시험성적
//score의 범위: 'score>=점수' 로 해야한다.
//만약 '<=점수' 로 하면, 3을 넣어도 "아 90보다 작으니까 A!" 이래버린다. 

#include <stdio.h>

int main()
{
	int score;
	char grade;
	scanf("%d",&score);

	if (score <= 100 && score >= 0) {
		if (score >= 90) grade = 'A';
		else if (score >= 80) grade = 'B';
		else if (score >= 70) grade = 'C';
		else if (score >= 60) grade = 'D';
		else grade = 'F';
	}
	else return 0;
	printf("%c", grade);
}