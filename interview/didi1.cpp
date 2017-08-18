/* 一串首尾相连的珠子(m个)，有N种颜色(N<=10)，
设计一个算法，取出其中一段，要求包含所有N中颜色，并使长度最短。
并分析时间复杂度与空间复杂度。*/

#include<iostream>
using namespace std;

int findMin(int *a, int m, int* b, int n){
	int i=0, j=0;
	int cn = 0;
	int minLen = m;
	int left = 0;
	int right = 0;
	while(j <= m){
		if(cn == n){
				while(cn == n){
					b[a[i]]--;
					if(b[a[i]]==0){
						cn--;
						if(minLen > j-i){minLen = j-i;left=i;right=j-1;}
					}else{i++;}
				}
		}else{
			if(b[a[j]] == 0){cn++;b[a[j]]++;}
			else{
				b[a[j]]++;
			}
			j++;
		}
	}
	cout<<"left:"<<left<<"right:"<<right<<endl;
	return minLen;
}
int main(){
	int a[] = {2,1,0,3,1,2,1,0,1,2,1};  
    int c[] = {0,0,0,0};
    cout<<findMin(a, 11, c, 4)<<endl;
}
