#include <stdio.h>
//n의 배수 : y를 n으로 나눴을 때 나머지가 0.
int main(void)
{
	int y; //year
	int c1,c2; //cond'
	scanf("%d", &y);
	if (1 == (y >= 1 && y <= 4000)) { //입력 값이 범위 내인지 확인 
		c1 = (0 == (y % 4)) && (0 != (y % 100));
		c2 = (0 == (y % 400));
		if (c1 || c2) printf("1"); //c1, c2 중 하나 만족
		else printf("0");//범위가 아니라면 프로그램 종료
	}
	else return 0;
}
