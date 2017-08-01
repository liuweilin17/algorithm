/*
find the kth max num
*/

#include<iostream>
using namespace std;

//the quick sort is used to compare with findkthmax
void quickSort(int* a, int left, int right){
    int i, j;
    i = left;
    j = right;
    int x = a[i];
    if(left < right){
        while(i < j){
            while(i < j && a[j] >= x)
                j--;
            if(i<j)
                a[i++] = a[j];
            while(i < j && a[i] < x)
                i++;
            if(i<j)
                a[j--] = a[i];
        }
        a[i] = x;
        quickSort(a, left, i-1);
        quickSort(a, i+1, right);
    }
}

//find the min-k number, which is also n-k+1 max number
int findKthMax(int* a, int left, int right, int k){
    int i,j,x;
    i = left;
    j = right;
    x = a[i];
    if(i < j){
        while(i < j && a[j] > x){
            j--;
        }
        if(i < j){
            a[i++] = a[j];
        }
        while(i < j && a[i] < x){
            i++;
        }
        if(i < j){
            a[j--] = a[i];
        }
        a[i] = x;
        if(i == k){
            return x;
        }else if(i > k){
            return findKthMax(a, left, i-1, k);
        }else{
            return findKthMax(a, i+1, right, k);
        }
    }
}
int main(){
    cout<<"hh"<<endl;
    int a[] = {3,2,1,5,4};
    cout<<findKthMax(a, 0, 4, 4);
}
