#include<stdio.h>
#include<conio.h>

int main()
{
	int arr[] = {10,7,15,3};
	int k,temp,i,j,t,flg=1;
	
	printf("enter the number\n");
	scanf("%d",&k);
	
	for(i=0;i<4;i++)
	{
		temp=arr[i];
		for(j=i+1;j<4;j++)
		{
			t=temp+arr[j];
			if(t==k)
			{
				printf("%d + %d",temp,arr[j]);
				flg=0;
				break;
			}
		}
	}
	
	if(flg)
	{
		printf("null");
	}
}
