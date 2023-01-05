#include <stdio.h>
#define _CRT_SECURE_NO_WARNINGS
#define size 9
int main()
{
	int n[size] = { 0, }, max = 0, index; // 입력받을 숫자, 최대값, 최대값 위치

	for (int i = 0; i < size; i++) { //입력: 자연수 9개
		scanf("%d", &n[i]);

		//if (n[i] >= 100) return 0; //100 이상 입력 시 종료
		//else if (n[i] <= 0) return 0; //0이하 입력 시 종료
		//if (i >= 1) {
		//	for (int j = 0; j < i; j++) {
		//		if (n[i] == n[j]) return 0;
		//	}
		//}//중복 입력 시 종료

		if (max < n[i]) {
			max = n[i]; //최대값 찾기
			index = i+1; //최대값위치 찾기
		}
	}
	printf("%d\n%d", max, index); //출력
	return 0;
}