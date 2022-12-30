#include <stdio.h>

int main()
{
	unsigned int N; //자연수 N

	scanf("%u", &N);
	if (N <= 100000) {
		for (int i = 0; i < N-1; i++) {
			printf("%d\n", N-i);
			
		}
	}
	else return 0;
	printf("1"); //마지막은 \n이 없게끔.

}