#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
	int a,b;
	while(scanf("%d %d", &a, &b)!=EOF)//출력 초과 해결 방법: 파일 끝에 도달할 때까지 while 실행 (End of File=-1)
		printf("%d\n", a + b);
	
}