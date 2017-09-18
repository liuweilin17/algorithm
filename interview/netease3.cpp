//find smallest element in a sorted array(may >>)

#include<iostream>
using namespace std;
int smallSearch(int* a, int n){
    int left = 0, right = n-1, mid;
    int ret;
    while(left <= right){
        mid = (right - left) / 2 + left;
        if(a[mid] > a[left]){
            left = mid + 1;
        }else if(a[mid] < a[left]){
            right = mid - 1;
        }else{
            ret = min(a[left], a[left+1]);
            break;
        }
    }
    return min(ret, a[0]);//�п�������ȫ�������飬���Ҫ��a[0]���ǽ���
    return -1;
}
int main(){
    int a[] = {4,5,1,2,3};
    int b[] = {1,2,3,4};

    cout<<smallSearch(a, 4)<<endl;
    cout<<smallSearch(b, 3)<<endl;
    return 0;
}
