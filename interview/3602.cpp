/*
	split()
*/
#include<iostream>
#include<bits/stdc++.h>
using namespace std;

vector<string> splitC(string s, string t){
	vector<string> ret;
	int len = t.length();
	int n = s.length();
	string tmp1="", tmp2;
	int i;
	for(i=0 ; i<n-len+1 ; i++){
		tmp2 = s.substr(i, len);
		if(tmp2.compare(t) == 0){
			//cout<<"tmp1: "<<tmp1<<endl;
			ret.push_back(tmp1);
			i+=(len-1);
			tmp1 = "";
		}else{
			tmp1 += s[i];
		}
	} //tmp1 = ""; //error
	for(int j=i; j<n ; j++){
		tmp1+=s[j];
	}
	if(tmp1 != ""){ret.push_back(tmp1);}
	return ret;
}
int main(){
	vector<string> s;
	s = splitC("1,2", ",");
	cout<<"size: "<<s.size()<<endl;
	for(int i=0;i<s.size();i++){
		cout<<s[i]<<" ";
	}
	cout<<endl;
	return 0;
}
