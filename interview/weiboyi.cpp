/*input 8 digit number and return the chinese name of it
** Input:1000
** Output:一千
*/
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
using namespace std;

string unit[] = {"", "十", "百", "千"};
string name[] = {"零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十"};

vector<string> getReading(int n){
    vector<string> ret;
    string s;
    int digit, i=0;
    bool flag = false; //if last digit is 0

    while(n > 0){
        digit = n % 10;
        s = name[digit];
        if(digit == 0){
            if(flag == false && i!=0){
                ret.push_back("零");
            }else{}
            flag = true;
        }else{
            ret.push_back(s + unit[i]);
            flag = false;
        }
        n /= 10;
        i++;
    }
    return ret;
}

int main()
{
    int n;
    vector<string> ret;
    cin>>n;
    ret = getReading(n/10000);
    if(n/10000 > 0){
        for(int i=ret.size()-1 ; i>=0 ; i--){
            cout<<ret[i];
        }
    }
    cout<<"万";
    ret = getReading(n % 10000);
    for(int i=ret.size()-1 ; i>=0 ; i--){
        cout<<ret[i];
    }

}
