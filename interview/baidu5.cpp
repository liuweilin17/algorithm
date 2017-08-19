/*top k*/
#include<bits/stdc++.h>
#include<iostream>
using namespace std;
vector<int> getTopK(int* a, int start, int end_, int k){
    int i = start, j = end_;
    int x = a[start];
    vector<int> b;
    cout<<"start:"<<start<<"end:"<<end_<<endl;
    if(i == j){//notice
        cout<<"i==j "<<i<<"a[0]"<<a[0]<<endl;
        for(int t=0 ; t<k ; t++){
                b.push_back(a[t]);
        }
        return b;
    }
    if(i < j){
        while(i<j){
            while(i<j && a[j] <= x){j--;}
            if(i<j){a[i++] = a[j];}
            while(i<j && a[i] >= x){i++;}
            if(i<j){a[j--] = a[i];}
        }
        a[i] = x;
        if(i < k-1){return getTopK(a, i+1, end_, k);}
        else if(i > k-1){return getTopK(a, start, i-1, k);}
        else{
            cout<<"i==k "<<k<<endl;
            for(int t=0 ; t<k ; t++){
                b.push_back(a[t]);
            }
            return b;
        }
    }
}
int main(){
    int a[] = {3,2,1,6,5,4};
    vector<int> b = getTopK(a, 0, 5, 5);
    cout<<"result"<<endl;
    for(int i=0 ; i<b.size() ;i++){
        cout<<b[i]<<" ";
    }
    cout<<endl;
}
