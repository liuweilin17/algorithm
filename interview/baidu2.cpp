/* devide stones with different weights into two parts, and make the difference between two parts smallest*/

#include<iostream>
#include<cstring>
using namespace std;

int main(){
	int * W, n, sum=0;
	int weight;
	cin>>n;
	W = new int[n];
	for(int i=0 ; i<n; i++){
		cin>>W[i];
		sum+=W[i];
	}
	//cout<<f[n][weight]<<endl;

	weight = sum/2;

	int f[n+1][weight+1];
	for(int i=0 ; i<=n ; i++){
		for(int j=0 ; j<=weight ; j++){
			f[i][j] = 0;
		}
	}

	for(int i=1 ; i<=n; i++){//stone number
		for(int j=0 ; j<=weight ; j++){//weight of stone
			if(j>=W[i-1])
				f[i][j] = max(f[i-1][j], f[i-1][j-W[i-1]] + W[i-1]);
			else
				f[i][j] = f[i-1][j];
		}
	}
	cout<<f[n][weight]<<endl;
}