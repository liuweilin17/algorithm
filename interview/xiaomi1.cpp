//common father node of tow nodes
//not finish yet!!!!!!!!!!!!!!
#include<iostream>
#include<bits/stdc++.h>
using namespace std;
struct Node{
	int v;
	Node* left;
	Node* right;
	Node(){}
	Node(int v, Node* left = NULL, Node* right = NULL):v(v),left(left),right(right){}
};

Node* findCommonFather(Node* root, Node* n1, Node* n2){
	if(root==NULL){return NULL;}
	if(root==n1 || root==n2){return root;}
	Node* t1 = findCommonFather(root->left, n1, n2);
	Node* t2 = findCommonFather(root->right, n1,n2);
	if(t1 != NULL && t2 != NULL){return root;}
	return t1==NULL ? t2 : t1;
}
int main(){
	Node* n1 = new Node(1);
	Node* n2 = new Node(2);
	Node* n3 = new Node(3);
	Node* n4 = new Node(4);
	Node* n5 = new Node(5);
	Node* n6 = new Node(6);
	Node* n7 = new Node(7);
	Node* n8 = new Node(8);
	n1->left = n2;
	n1->right = n3;
	n2->left = n4;
	n2->right = n5;
	n3->left = n6;
	n4->left = n7;
	n4->right = n8;
	Node* ret = findCommonFather(n1, n7, n5);
	cout<<ret->v<<endl;
}