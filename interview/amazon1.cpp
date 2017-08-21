/* 判断平衡二叉树 */

#include<iostream>
using namespace std;

int getHeight(Node* n){
	int h;
	if(n == NULL){return 0;}
	if(n->left){h=getHeight(n->left)+1;}
	if(n->right){h=max(h, getHeight(n->right)+1);}
	return h;
}

bool isBalance(Node* n){
	if(n == NULL){return true;}
	int h1 = getHeight(n->left);
	int h2 = getHeight(n->right);
	if(h1-h2 > 1 || h1-h2<-1){return false;}
	else{
		return isBalance(n->left) && isBalance(n->right);
	}
}
int main(){
	return 0;
}

