#include<stdio.h>
int main(){

int a,b;

printf("ENter two numbers :");
scanf("%d\n%d",&a,&b);

printf("Before swapping two numbers a=%d  b=%d",a,b);

a=a+b;
b=a-b;
a=a-b;

printf("\nAfter swapping two numbers a=%d  b=%d",a,b);
}