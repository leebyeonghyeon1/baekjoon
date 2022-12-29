//
#include <stdio.h>
#include <time.h> //time함수 쓰기위한 headerfile

int main(void)
{
	time_t currentTime; //자료형 time_t를 사용하는 변수
	currentTime = time(NULL);//time함수로 지금까지의 '초' 호출

	struct tm *timeInfo; //시간단위가 있는 struct tm을 가리키는 포인터
	timeInfo = localtime(&currentTime); //localtime으로 time함수의 값을 제대로 포맷팅 이후, 포인터로 tm의 구조체로 포맷팅 값 넘겨줌. 


	printf("%d", timeInfo->tm_year + 1900);// +1900필요
	printf("-%d", timeInfo->tm_mon+1);// +1필요
	printf("-%d", timeInfo->tm_mday);//month로부터 며칠? 이니까 그냥 며칠.
	
	return 0;
}
