//归并排序

public class Main {
    //recursive
    private static int binarySearch(int a[], int x){
        int left, right, mid;
        left = 0; right = a.length - 1;
        while(left <= right){
            mid = (right - left) / 2 + left; //直接使用（right + left）/ 2 可能会溢出
            if(a[mid] > x){
                right = mid - 1 ;
            }else if(a[mid] < x){
                left = mid + 1;
            }else{
                return mid;
            }
        }
        return -1;
    }

    //nonrecursive
    private static int binarySearchI(int a[], int left ,int right, int x){
        int mid;
        if(left <= right){
            mid = (right - left) / 2 + left;
            if(a[mid] == x){
                return mid;
            }else if(a[mid] > x){
                return binarySearchI(a, left, mid-1, x);
            }else{
                return binarySearchI(a, mid+1, right, x);
            }
        }else{
            return -1;
        }
    }

    public static void main(String[] args) {
        int a[] = {2, 5, 7, 9, 11, 22, 49};
        System.out.println(binarySearch(a, 222));
        System.out.println(binarySearch(a, 2));
        System.out.println(binarySearch(a, 49));
        System.out.println(binarySearchI(a, 0, 6, 222));
        System.out.println(binarySearchI(a, 0, 6, 2));
        System.out.println(binarySearchI(a, 0, 6, 49));
    }
}
