/* 计算 最长回文字串 */
#include<iostream>
#include<string>

using namespace std;

int main(){
    string s;
    int ret = 0, maxL = -1;
    cin>>s;
    int len = s.length();
    if(len < 1){cout<<"";return 0;}
    if(len == 1){cout<<s;return 0;}
    for(int i=1 ; i<s.length() ;i++){
        if(i%2 == 0){ //i is in the middle
            for(int j=1 ; j<=i&&j<s.length()-i ; j++){
                if(s[i-j] == s[i+j]){ret+=2;}
            }
            ret += 1;
            if(ret > maxL){maxL = ret;}
            ret = 0;
        }else{ //i-1 i is in the middle
            if(s[i] == s[i-1]){
                for(int j=1 ; j<=i-1&&j<s.length()-i ; j++){
                    if(s[i-1-j] == s[i+j]){ret+=2;}
                }
                ret += 2;
                if(ret > maxL){maxL = ret;}
                ret = 0;
            }
        }
    }
    cout<<maxL<<endl;
    return 0;
}
