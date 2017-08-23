#include<iostream>
using namespace std;
int binarySearch(int* a, int n, int target){
    int left = 0, right = n-1, mid;
    while(left <= right){
        mid = (right - left) / 2 + left;
        if(a[mid] > target){
            right = mid - 1;
        }else if(a[mid] < target){
            left = mid + 1;
        }else{
            return mid;
        }
    }
    return -1;
}
int main(){
    int a[] = {1,2};
    int b[] = {1,2,3};
    int c[] = {1};
    cout<<binarySearch(a, 2, 0)<<endl;
    cout<<binarySearch(a, 2, 1)<<endl;
    cout<<binarySearch(a, 2, 2)<<endl;
    cout<<binarySearch(a, 2, 3)<<endl;

    cout<<binarySearch(b, 3, 0)<<endl;
    cout<<binarySearch(b, 3, 1)<<endl;
    cout<<binarySearch(b, 3, 2)<<endl;
    cout<<binarySearch(b, 3, 3)<<endl;
    cout<<binarySearch(b, 3, 4)<<endl;

    cout<<binarySearch(c, 1, 0)<<endl;
    cout<<binarySearch(c, 1, 1)<<endl;
    cout<<binarySearch(c, 1, 2)<<endl;
    return 0;
}
