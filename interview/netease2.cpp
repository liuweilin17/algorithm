/*判断完全二叉数*/
/*按照层次遍历的方法，判断是否有空洞即可*/

#include<iostream>
using namespace std;
bool isComplete(Node* head){
	if(head==NULL){return true;}
	queue<Node*> q;
	Node* tmp;
	int flag = 0;
	q.push(head);
	while(!q.empty()){
		tmp = q.front();
		q.pop();
		if(flag == 1 && tmp != NULL){return false;}
		if(!tmp->left){q.push(tmp->left);}
		else{flag = 1;}
		if(!tmp->right){q.push(tmp->right);}
		else{flag = 1;}
	}
	return true;
}
int main(){
	return 0;
}
