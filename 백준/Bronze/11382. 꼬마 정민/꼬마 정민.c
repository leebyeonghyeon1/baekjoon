#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	double A, B, C, result;
	scanf("%lf %lf %lf", &A, &B, &C);
	result = A + B + C;
	if ((A >= 1) && (B >= 1) && (C >= 1))  printf("%.lf", result);
	else return 0;
}