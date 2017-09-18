//reverse list
#include<iostream>
#include<bits/stdc++.h>
using namespace std;
struct Node{
	int v;
	Node* next;
	Node(){}
	Node(int v, Node* next = NULL):v(v), next(next){}
};
class linkedList{
private:
	int count;
	Node* head;
public:
	void insert(Node* n){
		n->next = head;
		head = n;
		count += 1;
	}
	void print(){
		Node* tmp = head;
		while(tmp != NULL){
			cout<<tmp->v<<" ";
			tmp = tmp->next;
		}
		cout<<endl;
	}
	void reverse(){
		Node* pre = head;
		Node* cur = head->next;
		while(cur!= NULL){
			Node* ne = cur->next;
			cur->next = pre;
			pre = cur;
			cur = ne;
		}
		head->next = NULL;
		head = pre;
	}
	linkedList(Node* h=NULL){
		head = h;
		if(h != NULL){
			count = 1;
		}else{
			count = 0;
		}
	}
};

int main(){
	Node* head = new Node(-1);
	linkedList list = linkedList(head);
	for(int i=0 ; i<10 ; i++){
		list.insert(new Node(i));
	}
	list.print();
	list.reverse();
	list.print();
}