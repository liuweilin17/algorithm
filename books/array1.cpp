/*最长递增子序列*/

#include<iostream>
using namespace std;
int LIS(int* a, int len){//O(n2)
	int* lis_arr = new int[len];//notice:lis_arr[i]代表以a[i]为结尾的递增子序列的长度
	for(int i=0 ; i<len ; i++){
		lis_arr[i] = 1;
		for(int j=0 ; j<i ; j++){
			if(a[i] > a[j] && lis_arr[i] < lis_arr[j] + 1){
				lis_arr[i] = lis_arr[j] + 1;
			}
		}
	}
	int max=-1;
	for(int i=0 ; i<len ; i++){
		if(lis_arr[i] > max){max = lis_arr[i];}
	}
	return max;
}
int main(){
	int a[] = {1,-1,2,-3,4,-5,6,-7};
	cout<<LIS(a, 7)<<endl;
	return 0;
}
