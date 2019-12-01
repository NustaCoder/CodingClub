#include<stdio.h>
#include<conio.h>

int main()
{
	int n;
	printf("enter the no of elements...!!!");
	scanf("%d",&n);
	int arr[n];
	int i,temp,flag=0;
	printf("enter the elements");
	
	for(i=0;i<n;i++)
	{
		scanf("%d",&arr[i]);
	}
	for(i=0;i<n-1;i++)
	{
		temp = arr[i] - arr[i+1];
		if(temp != 1 && temp != -1)
		{
			flag = 1;
			break;
		}
	}
	if(flag)
	{
		printf("no");
	}
	else
	{
		printf("yes");
	}
	
	
}
