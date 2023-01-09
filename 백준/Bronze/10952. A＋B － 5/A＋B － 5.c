#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define max 10
#define min 0
int main() {
	int a,b,sum; 
	while (1) {
		scanf("%d %d", &a, &b);
		sum = a + b;
		if ((a>min)&&(a<max)&&(b>min)&&(b<max)) printf("%d\n", sum);
		else break;
	}
	return 0;
}