#include <bits/stdc++.h>
#include <stdlib.h>

typedef struct TreeNode {
	int data;
	struct TreeNode *left, *right;
} TreeNode;
TreeNode n[27];

//중위 순회
void inorder(TreeNode *root) {
	if(root != NULL) {
		inorder(root->left);//왼쪽 서브트리 순회
		printf("%d",root->data);
		inorder(root->right);//오른쪽 서브트리 순회 
	}
} 

//전위 순회
void preorder(TreeNode *root) {
	if (root != NULL) {
		printf("%d",root->data);//노드 방문
		preorder(root->left);//왼쪽 서브트리 순회 
		preorder(root->right);//오른쪽서브트리 순회 
	}
}

//후위 순회
void postorder(TreeNode *root) {
	if(root != NULL) {
		postorder(root->left);//왼쪽서브트리 순회
		postorder(root->right);//오른쪽 서브트리 순회
		printf("%d",root->data);//노드 방문 
	} 
} 

int N;
int name;
int le;
int ri;

int main()
{
	scanf(" %d", &N);
	for(int i = 0; i < N; i++)
	{
		scanf(" %d %d %d",&name,&le,&ri);
		n[name-1].data = name;
		if(le != -1) {
			n[name-1].left = &n[le-1];
		}
		else {
			n[name-1].left = NULL;
		}
		
		if(ri != -1) {
			n[name-1].right = &n[ri-1];
		}
		else {
			n[name-1].right = NULL;
		}
		
	}
	TreeNode *root = &n[0];
	
	preorder(root);
	printf("\n");
	inorder(root);
	printf("\n");
	postorder(root);
}
