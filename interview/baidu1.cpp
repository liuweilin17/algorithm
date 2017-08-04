/*atoi*/

#include<iostream>
using namespace std;

int atoi(string s){
	int len = s.size();
	int ret = 0; int t=1;
    bool minus = false;

	for(int i=len-1 ; i>=0 ; i--){
		if(s[i] == '-' && i == 0){
			ret = -ret;
		}else if(s[i] == '.'){
			ret = 0;
			t = 1;
		}else if(s[i] >= '0' && s[i] <= '9'){
			ret+=(s[i] - '0')*t;
			t*=10;
		}else{
			ret = -1;
			break;
		}
	}
	return ret;
}
int main(){
	string arr[5] = {"123", "12.3", "-23.3", "2e", "12-23"};

	for(int i=0 ; i<5 ; i++){
		cout<<atoi(arr[i])<<" ";
	}
}