/*树的先序遍历*/

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

void preOrder(Node* root){
    stack<Node*> s;
    s.push(root);Node* cur;
    while(!s.empty()){
        cur = s.top();
        printf("%d ", cur->v);
        s.pop();
        if(cur->right){s.push(cur->right);}
        if(cur->left){s.push(cur->left);}
    }
}

void inOrder(Node* root){
    stack<Node*> s;
    Node* cur = root;
    while(!s.empty() || cur != NULL){
        while(cur!= NULL){
            s.push(cur);
            cur = cur->left;
        }
        cur = s.top();
        printf("%d ", cur->v);
        s.pop();
        cur = cur->right;
    }
}

void postOrder(Node* root){
    stack<Node*> s;
    Node* cur = root;
    Node* visited;
    while(!s.empty() || cur != NULL){
        while(cur!= NULL){
            s.push(cur);
            cur = cur->left;
        }
        cur = s.top();
        if(cur->right == NULL || cur->right == visited){
            printf("%d ", cur->v);
            s.pop();
            visited = cur;
            cur = NULL;//notice
        }else{//notice
            cur = cur->right;
        }
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
    preOrder(n1);
    printf("\n");
    inOrder(n1);
    printf("\n");
    postOrder(n1);
    printf("\n");
}