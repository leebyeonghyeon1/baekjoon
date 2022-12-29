//1330 두 수 비교하기
#include <stdio.h>

int main()
{
	int a,b;
	scanf("%d %d",&a,&b );
	if ((a,b) >= -10000 && (a,b) <= 10000)
	{
		if (a > b)printf(">");
		else if (a < b)printf("<");
		else printf("==");
	}
	
	return 0;
}