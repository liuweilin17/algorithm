/*find if there is circle in link list*/
#include <iostream>

using namespace std;

struct Node{
	int data;
	Node* next;
	Node(int d):data(d), next(NULL){}
	Node(Node* n):data(n->data), next(n->next){}
};

class linkedList{
	private:
		int size;
		Node* head;
	public:
		void insert(Node* n){
			n->next = head;
			head = n;
			size++;
		}
		Node* getHead(){return head;}
		int getSize(){return size;}
		void print(){
			Node* tmp = head;
			while(tmp){
				cout<<tmp->data<<" ";
				tmp = tmp->next;
			}
		}
		linkedList(int d){
			size = 1;
			Node* n = new Node(d);
			head = n;
		}
		linkedList(){
			size = 0;
			head = NULL;
		}
		~linkedList(){
			delete[] head;
		}
};

int find_circle(Node* head){
	Node* fastPointer = NULL;
	Node* slowPointer = NULL;
	if(head == NULL){
		return -1;
	}
	while(fastPointer != NULL && fastPointer->next != NULL){
		fastPointer = fastPointer->next->next;
		slowPointer = slowPointer->next;
		if(fastPointer == slowPointer){
			return 1;
		}
	}
	return 0;
}
int main(){
	linkedList* l = new linkedList(1);
	for(int i=2 ; i<10 ; i++){
		l->insert(new Node(i));
	}
	l->print();
}
