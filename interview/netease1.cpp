/*
输出描述:

输出一个整数,表示n个学生列队可以获得的最大的疯狂值。

如样例所示: 
当队列排列顺序是: 25-10-40-5-25, 身高差绝对值的总和为15+30+35+20=100。
这是最大的疯狂值了。

输入例子1:

5
5 10 25 40 25

输出例子1:

100
 */

/*思路就是找出用将大数和小数挨在一起 */
#include<iostream>
#include<algorithm>
using namespace std;

int getAbs(int a){
	return a > 0 ? a : - a;
}
int main(){
	int n;
	cin>>n;
	int * a = new int[n];
	for(int i=0 ; i<n ; i++){cin>>a[i];}

	sort(a, a+n);

	if(n <= 1){return 0;}
	if(n == 2){cout<<getAbs(a[1]-a[0])<<endl;return 0;}
	int i = 1, j = n-1;
	int left = a[0];
	int right = a[n-1];
	int sum1 = right - left;
	
	int flag = 0;
	int t1, t2;
	while(i<j){
		if(flag == 0){
			t1 = getAbs(a[i]-left); t2 = getAbs(a[i]-right);
			if(t1 > t2){
				left = a[i];
				sum1 += t1;
			}else{
				right = a[i];
				sum1 += t2;
			}
			j--;flag=1;
		}else{
			t1 = getAbs(a[j]-left); t2 = getAbs(a[j]-right);
			if(t1 > t2){
				left = a[j];
				sum1 += t1;
			}else{
				right = a[j];
				sum1 += t2;
			}
			i++;flag=0;
		}
	}
	i = 0, j = n-2;
	left = a[0];
	right = a[n-1];
	int sum2 = right - left;
	flag = 1;
	while(i<j){
		if(flag == 0){
			t1 = getAbs(a[i]-left); t2 = getAbs(a[i]-right);
			if(t1 > t2){
				left = a[i];
				sum2 += t1;
			}else{
				right = a[i];
				sum2 += t2;
			}
			j--;flag=1;
		}else{
			t1 = getAbs(a[j]-left); t2 = getAbs(a[j]-right);
			if(t1 > t2){
				left = a[j];
				sum2 += t1;
			}else{
				right = a[j];
				sum2 += t2;
			}
			i++;flag=0;
		}
	}
	cout<<max(sum1, sum2)<<endl;
}
