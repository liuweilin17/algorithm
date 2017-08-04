/* 求两个字符串最小编辑距离*/

#include<iostream>
#include<string>
using namespace std;

//recursive way
int strDistance1(string a, int startA, int endA, string b, int startB, int endB){

	if(startA > endA){
		if(startB <= endB){
			return endB - startB + 1;
		}else{
			return 0;
		}
	}

	if(startB > endB){
		if(startA <= endA){
			return endA - startA + 1;
		}else{
			return 0;
		}
	}

	if(a[startA] == b[startB]){
		return strDistance1(a, startA + 1, endA, b, startB + 1, endB);
	}else{
		//delete first character of A OR add first character of A to B
		int len1 = strDistance1(a, startA + 1, endA, b, startB, endB);

		//delete first character of B OR add fist character of B to A;
		int len2 = strDistance1(a, startA, endA, b, startB + 1, endB);

		//change first character of B to first character of A OR change first character of A to first character of B
		int len3 = strDistance1(a, startA + 1, endA, b, startB + 1, endB);

		return (min(min(len1, len2), len3)) + 1;
	}

}

//nonrecursive way, by dynamic programming
/*Edit[i][j] represents the steps from a[0...i-1] to b[0...j-1]
**Edit[i][j] = Edit[i-1][j-1], if a[i-1] == b[j-1]
**Edit[i][j] = min(Edit[i-1][j-1], Edit[i-1][j], Edit[i][j-1]) + 1, if a[i-1] != b[j-1]
*/

int strDistance2(string a, string b){
	int aLen = a.size();
	int bLen = b.size();
	int Edit[aLen + 1][bLen + 1];
	for(int i=0 ; i<=aLen ; i++){
		Edit[i][0] = i;
	}
	for(int i=0 ; i<=bLen ; i++){
		Edit[0][i] = i;
	}
	for(int i=1; i<=aLen ; i++){
		for(int j=1; j<=bLen ; j++){
			if(a[i-1] == b[j-1])
				Edit[i][j] = Edit[i-1][j-1];
			else
				Edit[i][j] = min(Edit[i-1][j-1], min(Edit[i-1][j],Edit[i][j-1])) + 1;
		}
	}
	return Edit[aLen][bLen];
}
int main(){
	string a = "aebcd";
	string b = "abcd";
	cout<<strDistance1(a, 0, a.size()-1, b, 0, b.length()-1)<<endl;//size() or length are both OK!!!!!
	cout<<strDistance2(a, b)<<endl;//size() or length are both OK!!!!!
}