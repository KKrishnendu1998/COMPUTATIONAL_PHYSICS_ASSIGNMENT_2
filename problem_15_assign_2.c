/***Problem 15 : C code for solving a initial value problem using step size h=0.2 and tabulate the error and error bound at each step ***/

#include<stdio.h>
#include<stdlib.h>
#include<math.h>

float func(float y,float t)   //defining the function that returns derivative 
{
return y-t*t+1;
}
int main()
{
int N;                  //variable declaration
float t,a,b,y,h,yt,err,eb;    //variable declaration
a=0.0;      //starting value
b=2.0;      //end value
h=0.2;      //step size
t=a;        //initializing the value of t
y=0.5;      //initializing the value of y
printf("\n    t\t\t   y\t\ttrue solution\t error\t       error bound\n");

while(t<(b+h))

{

yt=pow((t+1),2)-0.5*exp(t);      //true solution

err=fabs(y-yt);              //error calculation

eb=fabs(0.1*(0.5*exp(2)-2)*(exp(t)-1));    //calculation of error bound

printf("%f\t%f\t   %f\t%f\t%f\n",t,y,yt,err,eb);    //printing the result

y=y+h*func(y,t);   //finding the next value of y

t=t+h;    //updating the value of y

}

}
