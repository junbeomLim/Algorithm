#include <cstdio>
#include <iostream>
#include <queue>

using namespace std;

int Visit[1001];
int adjacencyMatrix[1001][1001];
int N, M, V;

queue<int> q;

void bfs(int start)
{
	Visit[start] = 0;
	q.push(start);
	
	while(!q.empty()) {
		start = q.front();
		cout << start << " ";
		q.pop();

		for(int i = 1; i <= N; i++) {	
			if(!Visit[i] || !adjacencyMatrix[start][i]) {
				continue;
			}
			q.push(i);
			Visit[i] = 0;
		}
	}
}

void Dfs(int cur)
{
	Visit[cur] = true;
	cout << cur << " ";	
	for(int i = 1; i <= N; i++) {
		if(Visit[i] || !adjacencyMatrix[cur][i]) 
			continue;
		Dfs(i);
	}
}

int main()
{
	cin >> N >> M >> V;

	for(int i = 0; i < M; i++) {
		int nodeFirst, nodeSecond;
		cin >> nodeFirst >> nodeSecond;

		adjacencyMatrix[nodeFirst][nodeSecond] = 1;
		adjacencyMatrix[nodeSecond][nodeFirst] = 1;
	}
	
	Dfs(V);
	printf("\n");
	bfs(V);
}
