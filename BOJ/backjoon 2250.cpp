#include <iostream>
#include <algorithm>

using namespace std;
const int MAX = 10001;
const int INF = 987654321;

int N;
int idx;
int Node[MAX]; 
int low[MAX];
int high[MAX];
pair<int, int> tree[MAX];

//중위 순회
void DFS(int val, int cnt)
{
        //왼쪽 트리 
        if (tree[val].first > 0)
			DFS(tree[val].first, cnt + 1);
        //노드 방문 
        low[cnt] = min(low[cnt], idx);
        high[cnt] = max(high[cnt], idx++);
        //오른쪽 트리 
        if (tree[val].second > 0)
			DFS(tree[val].second, cnt + 1);
}

int main(void)
{
	cin >> N;
	
	for (int i = 0; i < MAX; i++)
		low[i] = INF;
	         
	for (int i = 0; i < N; i++)
	{
		int NO, left, right;
		cin >> NO >> left >> right;
		Node[NO]++;
		
		if (left != -1)
			Node[left]++;
		     
		tree[NO].first = left;
		if (right != -1)
			 Node[right]++;
		
		tree[NO].second = right;
	}
	//루트 찾기
	int root;
	
	for (int i = 1; i <= N; i++)
	    if (Node[i] == 1)
	        root = i;
	
	idx = 1;
	DFS(root, 1);
	//최대 길이
	int we = high[1] - low[1] + 1;
	
	int he = 1;
	
	for (int i = 2; i <= N; i++)
	{
		int temp = high[i] - low[i] + 1;
	    if (temp > we)
	    {
		    we = temp;
	        he = i;
	    }
	}
	cout << he << " " << we << "\n";
	return 0;
}

