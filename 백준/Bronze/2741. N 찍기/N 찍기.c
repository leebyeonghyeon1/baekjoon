#include <stdio.h>

int main()
{
	unsigned int N; //자연수 N
	
	scanf("%u", &N);
	if (N <= 100000) {
		for (int i = 1; i < N; i++) printf("%d\n", i);
	}
	else return 0;
	printf("%u", N); //마지막은 \n이 없게끔.

}