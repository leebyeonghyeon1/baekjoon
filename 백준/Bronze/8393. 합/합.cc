//8393 합
#include <stdio.h>

int main()
{
	int n;
	int sum = 0;
	scanf("%d", &n);
	if (n >= 1 && n <= 10000)
	{
		//for 문에서, i==n이라고 하면 X. 증가하니까 부등호로 표시
		for (int i = 1; i <= n; i++)
		{
			sum += i;
		}
	}
	printf("%d", sum);
	return 0;
}