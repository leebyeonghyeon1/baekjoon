#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define t_max 1000000
#define input_max 1000
#define input_min 1

int main() {
	int a,b,t,sum;
	scanf("%d", &t);
	if (t > t_max) return 0;
	for(int i=1; i<=t;i++){
		scanf("%d %d", &a, &b);
		sum = a + b;
		if ((a>=input_min)&&(a<=input_max)&&(b>=input_min)&&(b<=input_max)) printf("%d\n", sum);
	}
	return 0;
}