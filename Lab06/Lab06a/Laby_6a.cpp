|f(x)|<10^-5 f(x)=2x^3-4x^2+3x-6
#include"iostream"
#include"stdio.h"
#include"math.h"
#define null 0
double fx(double); //f(x)函数
void main()
{
double xa(null),xb(null),xc(null);
do
{
printf("请输入一个范围x0 x1：");
std::cin>>xa>>xb; //输入xa xb的值
printf("%f %f",xa,xb);
}
while(fx(xa)*fx(xb)>=0); //判断输入范围内是否包含函数值0
do
{
if(fx((xc=(xa+xb)/2))*fx(xb)<0) //二分法判断函数值包含0的X取值区间
{
xa=xc;
}
else
{
xb=xc;
}
}
while(fx(xc)>pow(10.0,-5)||fx(xc)<-1*pow(10.0,-5));//判断x根是否在接近函数值0的精确范围内
printf("\n 得数为：%f",xc);
}
double fx(double x)
{
return(2.0*pow(x,3)-4.0*pow(x,2)+3*x-6.0);
}