/* given array A, B, with size m,n, 
*find the median of all number of two array, 
*and the complexity should be O(logn)
*/

#include<iostream>
using namespace std;

int findMedian_logn(int vec1[], int n1, int vec2[], int n2)
{
    int m1 = (n1-1) / 2, m2 = (n2-1) / 2;
    if(n1 == 1)
    {//递归结束条件
        if(n2 == 1)
            return vec1[0] < vec2[0] ? vec1[0] : vec2[0];
        if(n2 % 2 == 0)
        {
            if(vec1[0] >= vec2[m2+1])
                return vec2[m2+1];
            else if(vec1[0] <= vec2[m2])
                return vec2[m2];
            else return vec1[0];
        }
        else//取下中位数
        {
            if(vec1[0] >= vec2[m2])
                return vec2[m2];
            //else if(vec1[0] <= vec2[m2-1])
            //    return vec2[m2-1];
            else return vec1[0];
        }
    }
    else if(n2 == 1)
    {//递归结束条件
        if(n1 % 2 == 0)
        {
            if(vec2[0] >= vec1[m1+1])
                return vec1[m1+1];
            else if(vec2[0] <= vec1[m1])
                return vec1[m1];
            else return vec2[0];
        }
        else//取下中位数
        {
            if(vec2[0] >= vec1[m1])
                return vec1[m1];
            //else if(vec2[0] <= vec1[m1-1])
            //    return vec1[m1-1];
            else return vec2[0];
        }
    }
    else
    {
        int cutLen = n1/2 > n2/2 ? n2/2 : n1/2;//注意每次减去短数组的一半，如果数组长度n是奇数，一半是指n-1/2
        if(vec1[m1] == vec2[m2])return vec1[m1];
        else if(vec1[m1] < vec2[m2])
            return findMedian_logn(&vec1[cutLen], n1-cutLen, vec2, n2-cutLen);
        else
            return findMedian_logn(vec1, n1-cutLen, &vec2[cutLen], n2-cutLen);
    }
}

 //找到两个有序数组中第k小的数,k>=1
	int findKthSmallest(int vec1[], int n1, int vec2[], int n2, int k)
	{
		//边界条件处理
		if(n1 == 0)return vec2[k-1];
		else if(n2 == 0)return vec1[k-1];
		if(k == 1)return vec1[0] < vec2[0] ? vec1[0] : vec2[0];

		int idx1 = n1*1.0 / (n1 + n2) * (k - 1);
		int idx2 = k - idx1 - 2;

		if(vec1[idx1] == vec2[idx2])
		 return vec1[idx1];
		else if(vec1[idx1] < vec2[idx2])
		 return findKthSmallest(&vec1[idx1+1], n1-idx1-1, vec2, idx2+1, k-idx1-1);//kth turns to k-indx1-1th, after removing indx1 + 1 elements
		else
		 return findKthSmallest(vec1, idx1+1, &vec2[idx2+1], n2-idx2-1, k-idx2-1);//kth turns to k-indx2-1th, after removing indx2 + 1 elements
	}

int main(){
	int a[] = {2,3,5};
	int b[] = {4,6,7,8};
	int c[] = {1,2,3,3};
	int d[] = {5,6,7,8};
	cout<<findMedian_logn(a, 3, b, 4)<<endl;
	cout<<findKthSmallest(a, 3, b, 4, (3+4)/2 +1 )<<endl;
	cout<<findMedian_logn(c, 4, d, 4)<<endl;
	cout<<findKthSmallest(c, 4, d, 4, (4+4)/2 -1 )<<endl;
}