/*
求到所有叶子节点的所有路径中，和最大的，和以及路径
*/

#include<iostream>
#include<bits/stdc++.h>
using namespace std;

struct Node{
	int v;
	Node* left;
	Node* right;
	Node(){}
	Node(int v, Node* l, Node* r):v(v),left(l),right(r){}
};
int maxV;
vector<Node*> maxPath;

//递归实现
void getMax1(Node* root, int sum, vector<Node*> path){
	if(root!=NULL){
		sum+=root->v;
		path.push_back(root);
		if(root->left == NULL && root->right == NULL){//到叶子节点
			printf("sum: %d ", sum);
			for(int i=0 ; i<path.size() ; i++){printf("%d ", path[i]->v);}
			printf("\n");
			if(sum > maxV){maxV = sum; maxPath = path;}
		}else{
			getMax1(root->left, sum, path);
			getMax1(root->right, sum, path);
		}
	}
}

//非递归实现
void getMax2(Node* root, int sum, vector<Node*> path){
	stack<Node*> s; Node* cur;
	s.push(root);
	map<Node*, bool> visited;
	while(!s.empty()){
		cur = s.top();
		
		//前序遍历增加的部分
		sum += cur->v;
		path.push_back(cur);
		if(cur->left == NULL && cur->right == NULL){//到叶子节点
			printf("sum: %d ", sum);
			if(sum > maxV){maxV = sum;maxPath = path;}
			for(int i=0;i<path.size();i++){
				printf("%d ", path[i]->v);
			}
			printf("\n");
			//到叶子节点以后，自底向上判断每个节点的左右孩子是否都已经被路径覆盖到，如果左右孩子都被覆盖到，那个就将当前点从路径中删除，同时将sum值减去节点的值
			for(int j=path.size()-1; j>=0 ;j--){
				if ( (path[j]->left == NULL || visited.find(path[j]->left) != visited.end()) && 
					(path[j]->right == NULL || visited.find(path[j]->right) != visited.end()) ){
					visited[path[j]]=true;
					sum -= path[j]->v;
					path.pop_back();
				}
			}
		}
		//前序遍历增加的部分		

		s.pop();
		if(cur->right){s.push(cur->right);}
		if(cur->left){s.push(cur->left);}
	}
}
int main(){
	Node* n5 = new Node(5, NULL, NULL);
	Node* n6 = new Node(6, NULL, NULL);
	Node* n4 = new Node(4, NULL, NULL);
	Node* n3 = new Node(3, n5, n6);
	Node* n2 = new Node(2, NULL, n4);
	Node* n1 = new Node(1, n2, n3);
	
	vector<Node*> v;
	getMax1(n1, 0, v);
	printf("maxV:%d\n", maxV);
	for(int i=0 ;i<maxPath.size();i++){
		printf("%d ", maxPath[i]->v);
	}
	printf("\n");
	maxV = -1;
	getMax1(n1, 0, v);
	printf("maxV:%d\n", maxV);
	for(int i=0 ;i<maxPath.size();i++){
		printf("%d ", maxPath[i]->v);
	}
}
