#include<stdio.h>
#include<conio.h>

//this solution is in one pass
//you can also use the logic of sorting but you have to also assume positive value of the array element when comparing
//hint : don't change actual value of the array, make it's copy, convert it into positive value and compare, then change position of actual value 
int main()
{
	int arr_main[] = {-8,-5,-3,-1,4,2,6};
	int arr_clone[100],i,temp;
	
	for(i=0;i<100;i++)
	{
		arr_clone[i] = 0;
	}
	
	for(i=0;i<7;i++)
	{
		if(arr_main[i]<0)
		{
			temp = arr_main[i]*(-1);
		}
		else
		{
			temp = arr_main[i];
		}
		//if your array won't contain 0
		arr_clone[temp] = arr_main[i];
		//if contains 0 then take, arr_clone[temp] = arr_main[i];
	}
	
	for(i=0;i<100;i++)
	{
		if(arr_clone[i]!=0){
			printf("%d\t",arr_clone[i]);
		}
	}
}

