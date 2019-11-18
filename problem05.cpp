#include<stdio.h>
#include<conio.h>

int main()
{
	int arr[] = {1,2,1,3,2};
	int temp=0,i;
	
	for(i=0;i<5;i++)
	{
		temp=temp^arr[i];	
	}	
	
	printf("unpaired number = %d",temp);
}
