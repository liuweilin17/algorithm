//heap sort
#include<iostream>
#include<bits/stdc++.h>
using namespace std;
void modify(int* a, int i, int n){
    int j = 2*i + 1;
    int x = a[i];
    while(j<n){
        if(a[j] > a[j+1]){j++;}
        if(a[j] > x){break;}//notice
        a[i] = a[j];
        i = j;
        j = 2*i + 1;
    }
    a[i] = x;
}
void mergeCreate(int* a, int n){
    for(int i=(n/2)-1;i>=0;i--){
        modify(a, i, n);
    }
}
vector<int> mergeSort(int*a, int n){
    vector<int> ret;ret.push_back(a[0]);
    for(int i=n-1 ; i>0 ; i--){
        a[0] = a[i];
        modify(a, 0, i);
        ret.push_back(a[0]);
    }
    return ret;
}
int main(){
    int a[] = {53,17,78,9,45,65,87,23};
    mergeCreate(a, 5);
    for(int i=0 ; i<5 ; i++){
        printf("%d ", a[i]);
    }
    printf("\n");
    vector<int> v = mergeSort(a, 5);
    for(int i=0 ; i<v.size() ; i++){printf("%d ", v[i]);}
}
