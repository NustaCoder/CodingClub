#include<stdio.h>
#include<conio.h>

int main()
{
	char a[30];
	int flg=0,c;
	int arr[26];
	int i;
	
	for(i=0;i<26;i++)
	{
		arr[i]=0;
	}
	
	printf("enter the string");
	scanf("%s",a);
	
	for(i=0;i<20;i++)
	{
		c=a[i];
		c=c-97;
		arr[c]++;
		if(arr[c]==2)
		{
			printf("%c",(c+97));
			flg=0;
			break;
		}
		flg++;
	}
	if(flg>1)
	{
		printf("null");
	}
	
}
