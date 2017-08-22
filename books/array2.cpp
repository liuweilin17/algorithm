/*子数组之和的最大值*/
#include<iostream>
using namespace std;

/*
one dimention:
start代表以当前元素开始但最后一个元素的子数组和的最大值。递推：start[i-1] = max(array[i-1] + start[i], array[i-1])
all代表当前元素到最后一个元素的子数组的最大值。递推：all[i-1] = max(start[i-1], all[i])
*/
int maxSum1(int* a, int n){
	if(n<1){return 0;}
	int start=a[n-1], all=a[n-1];
	for(int i=n-2 ; i>=0 ; i--){
		start = max(a[i], a[i]+start);
		all = max(start, all);
	}
	return all;
}

/*
two dimention:
start代表以当前列，i-j行和元素开始但最后一列，i-j行元素的子数组和的最大值。
all代表当前列，i-j行到最后一个列，i-j行的子数组的最大值。
*/
int* getArr(int** a, int i, int j, int m){
	int* ret = new int[m];
	for(int k=0 ; k<m ; k++){ret[k]=0;}
	for(int k = 0 ; k<m ; k++){
		for(int t = i ; t<=j ; t++){
			ret[k] += a[t][k];
		}
	}
	return ret;
}
int maxSum2(int** a, int n, int m){
	int start, all;
	int maxV = -100000;
	for(int i=0 ; i<n ; i++){
		for(int j=i ; j<n ; j++){
			int* tmp = getArr(a, i, j, m);
			start = tmp[m-1];
			all = tmp[m-1];
			for(int k=m-2; k>=0; k--){
				start = max(tmp[k], tmp[k] + start);
				all = max(start, all);
			}
			if(maxV < all){maxV = all;}
		}
	}
	return maxV;
}
int main(){
	int a[] = {-2,-6};
	cout<<maxSum1(a, 2)<<endl;
	
	int m=2,n=2;
	int **b = new int*[m];
	for(int i=0 ; i<m ; i++){
		b[i] = new int[n];
		for(int j = 0 ; j<n ; j++){
			b[i][j] = -i-j;
		}
	}
	for(int i=0 ; i<m ; i++){
		for(int j=0 ; j<n ; j++){
			cout<<b[i][j]<<" ";
		}
		cout<<endl;
	}
	cout<<maxSum2(b, m, n)<<endl;
	return 0;	
}
