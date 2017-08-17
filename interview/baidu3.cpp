#include <iostream>
#include <vector>

using namespace std;
void findMaxK_(int* a, vector<int>& b, int left, int right, int k){
    int i = left, j = right;
    int x = a[i];
    if(left < right){
        while(i < j){
            while(i < j && a[j] >= x){j--;}
            if(i < j){a[i++] = a[j];}
            while(i < j && a[i] <= x){i++;}
            if(i < j){a[j--] = a[i];}
        }
        a[i] = x;
        if(k > right - i){
            for(int t=i+1 ; t<=right ; t++){b.push_back(a[t]);}
            findMaxK_(a, b, left, i, k - (right - i));//notice i
        }else if(k < right - i){
            findMaxK_(a, b, i+1, right, k);
        }else{
            for(int t=i+1 ; t<=right ; t++){b.push_back(a[t]);}
        }
    }
}

//method 1 : on the basis of quick sort
vector<int> findMaxK1(int* a, int len, int k){
    vector<int> b;
    if(k <= 0){
        return b;
    }
    if(k >= len){
        for(int i=0 ; i<len ; i++){b.push_back(a[i]);}
    }else{
        findMaxK_(a, b, 0, len-1, k);
    }
    return b;
}

//method 2 : 维护一个个数为k的最小堆
/*[notice]
假如有N个节点，那么高度为H=logN，最后一层每个父节点最多只需要下调1次，倒数第二层最多只需要下调2次，顶点最多需要下调H次，
而最后一层父节点共有2^(H-1)个,倒数第二层公有2^(H-2),顶点只有1(2^0)个，所以总共的时间复杂度为s = 1 * 2^(H-1) + 2 * 2^(H-2) + ... + (H-1) * 2^1 + H * 2^0
将H代入后s= 2N - 2 - log2(N)，近似的时间复杂度就是O(N)。 
*/
void MinHeapFixDown(int a[],int i,int n){//从节点i开始，向下调整，n为向下最后一个节点的标号加1
    int j,tmp;
    tmp = a[i];
    j = 2 * i + 1;
    while(j<n){
        if(j+1 < n && a[j+1]<a[j]){
            j++;
        }
        if(a[j]>tmp){
            break;
        }
        a[i] = a[j];
        i = j;
        j = 2 * i + 1;
    }
    a[i] = tmp;
}

void MakeMinHeap(int a[],int n){//建立一个最小堆,建堆的复杂度是O(n)(notice)
    for(int i=n/2-1;i>=0;i--){
        MinHeapFixDown(a,i,n);
    }
}
void MinheapsortTodescendarray(int a[],int n){ //堆排序
    for(int i=n-1;i>0;i--){
        int tmp = a[0];
        a[0] = a[i];
        a[i] = tmp;
        MinHeapFixDown(a,0,i);
    }
}


int main()
{
    cout << "Hello world!" << endl;
    int a[] = {3,2,1,6,5,4};
    vector<int> b;
    b = findMaxK1(a, 6, 0);
    cout<<b.size()<<endl;
    cout<<"a: ";
    for(int i=0 ; i<6 ; i++){
        cout<<a[i]<<" ";
    }
    cout<<endl;
    cout<<"b: ";
    for(int i=0 ; i<b.size() ; i++){
        cout<<b[i]<<" ";
    }
    cout<<endl;
    MakeMinHeap(a, 6);
    for(int i=0 ; i<6 ; i++){
        cout<<a[i]<<" ";
    }
    return 0;
}
