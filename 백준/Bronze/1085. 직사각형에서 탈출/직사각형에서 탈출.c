#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	
	int x, y;
	int w, h;
	int d_x, d_y, min_d; //dist'X, dist'Y, min'Val'OfDist'

	scanf("%d %d %d %d", &x, &y, &w, &h);

	d_x = (w - x) < x ? w - x : x; //x는 0,w와 비교해서 더 차이가 적게 나는 쪽으로
	d_y = (h - y) < y ? h - y : y; //y는 0,h와 비교해서 더 차이가 적게 나는 쪽으로
	min_d = d_x < d_y ? d_x : d_y; //가장 작은 값 찾기
	printf("%d", min_d);

	return 0;
}