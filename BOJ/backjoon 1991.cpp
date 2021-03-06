#include <bits/stdc++.h>
#include <stdlib.h>

typedef struct TreeNode {
	int data;
	struct TreeNode *left, *right;
} TreeNode;
TreeNode n[27];

//���� ��ȸ
void inorder(TreeNode *root) {
	if(root != NULL) {
		inorder(root->left);//���� ����Ʈ�� ��ȸ
		printf("%d",root->data);
		inorder(root->right);//������ ����Ʈ�� ��ȸ 
	}
} 

//���� ��ȸ
void preorder(TreeNode *root) {
	if (root != NULL) {
		printf("%d",root->data);//��� �湮
		preorder(root->left);//���� ����Ʈ�� ��ȸ 
		preorder(root->right);//�����ʼ���Ʈ�� ��ȸ 
	}
}

//���� ��ȸ
void postorder(TreeNode *root) {
	if(root != NULL) {
		postorder(root->left);//���ʼ���Ʈ�� ��ȸ
		postorder(root->right);//������ ����Ʈ�� ��ȸ
		printf("%d",root->data);//��� �湮 
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
