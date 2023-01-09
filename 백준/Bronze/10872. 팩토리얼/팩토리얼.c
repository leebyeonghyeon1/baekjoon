#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#define Maximum 12

int factorial(int n) {
	n= (n > 1) ? n * factorial(n - 1) : 1;
	return n;
}

int main() {
	int n;
	scanf("%d", &n);
	if(n<=Maximum) printf("%d\n", factorial(n));
	else return 0;
}