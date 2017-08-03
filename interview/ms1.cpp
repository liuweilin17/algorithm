/*树的先序遍历

//pre order:root, left ,right
vector<int> preOrderTravel(TreeNode* root){
    vector<int> res;
    if(root == NULL){
        return res;
    }
    stack<TreeNode*> st;
    st.push(root);
    TreeNode* cur;
    while(!st.empty()){
        cur = st.top();
        res.push_back(cur->val);
        st.pop();
        if(cur->right)
            st.push(cur->right);
        if(cur->left)
            st.push(cur->left);
    }
    return res;
}

