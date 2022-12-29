//곱셈
#include <stdio.h>

int main()
{
	//나눗셈 시, int 변수의 나머지가 버려지는 원리 이용.
	
	int L1, L2;
	scanf("%d", &L1);
	scanf("%d", &L2);

	//L1의 'n의 자리'를 구분해서 변수화
	int L1_1 = (L1/100); //L1의 백의 자리
	int L1_2 = (L1/10) - (L1_1*10);//십의 자리
	int L1_3 = L1 - (L1_1*100) - (L1_2*10);//일의 자리

	//L2의 'n의 자리'를 구분해서 변수화
	int L2_1 = (L2 / 100); //의 백의 자리
	int L2_2 = (L2 / 10) - (L2_1 * 10);//십의 자리
	int L2_3 = L2 - (L2_1 * 100) - (L2_2 * 10);//일의 자리

	int L3 = L1 * L2_3;
	int L4 = L1 * L2_2;
	int L5 = L1 * L2_1;

	int L6 = L1 * L2;

	printf("%d\n%d\n%d\n%d", L3,L4,L5,L6);

	return 0;
}