#include<stdio.h>
#include<conio.h>

int findPrime(int a);

int main()
{
	int num,temp,i,ch1=0,ch2=0;
	printf("enter the number...!\n");
	scanf("%d",&num);
	if(num<4)
	{
		printf("\nno output");
		ch1 = 1;
		ch2 = 1;
	}
	else{
		for(i=2;i<num;i++)
		{
			temp = num - i;
			ch1 = findPrime(temp);
			ch2 = findPrime(i);
			if(ch1 == 1 && ch2 == 1)
			{
				printf("\n%d = %d + %d",num,temp,i);
				break;
			}
		}
	}
	if(ch1 == 0 || ch2 == 0)
	{
		printf("\nno output");
	}
}

int findPrime(int a)
{
	int i,temp;
	if(a==2)
		{
			temp=1;
			return temp;
		}
	for(i=2;i<a;i++)
	{
		if(a%i==0)
		{
			temp = 0;
			break;
		}
		else if(i==a-1)
		{
			temp = 1;
		}
	}
	return temp;
}
