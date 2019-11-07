#include<stdio.h>
#include<conio.h>

int main()
{
	char a[30];
	int c,i;
	
	printf("enter the message\n");
	gets(a);
	
	for(i=0;i<30;i++)
	{
		c=a[i];
		if(c>96 && c<122)
		{
			c=c-96;
			printf("%d ",c);
		}
	}
}
