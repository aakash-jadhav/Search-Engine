//c program to find factors of a number
#include<stdio.h>
#include<stdlib.h>
void main(int argc,char *argv[])
{
	if(argc<=1)
	{
	printf("Enter Arguments");
	exit(0);
	}
	int n=atoi(argv[1]);
	for(int j=1;j<n;j++)
		{
			if(n%j==0)
			printf("%d ",j);
		}
}