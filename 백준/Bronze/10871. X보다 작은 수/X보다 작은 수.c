#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define max 10000
#define min 1

int main(){
	int N, X;
	int input;
	scanf("%d %d", &N, &X);
	if ((N <= max) && (X <= max) && (N >= 1) && (N >= 1)) {
		for (int i = 0;i < N;i++) {
			scanf("%d", &input);
			if (X > input) printf("%d ", input);
		}
	}
	return 0;

}