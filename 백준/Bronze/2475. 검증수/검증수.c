#include <stdio.h>

int main()
{
	int N[5]; //고유번호
	int total=0,testNum; // 각 숫자를 제곱한 수들의 합, 검증수

	for (int i = 0; i < 5; i++) scanf("%d", &N[i]); //입력
	for (int j = 0; j < 5; j++) {
		if (N[j] >= 0 && N[j] <= 9) { //고유번호는 일의 자리 자연수
			N[j] = N[j] * N[j];
			total += N[j];
		}
		else return 0;
	}
			testNum = total % 10;
			printf("%d", testNum);
		
}