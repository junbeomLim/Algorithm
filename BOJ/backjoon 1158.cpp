#include <iostream>
#include <queue>
 
using namespace std;
 
int main() {
    int N, K;
    queue<int> q;
 
    scanf(" %d %d", &N, &K);
 
    for (int i = 1; i <= N; i++)
    {
        q.push(i);
    }
 
    printf("<");
    while (q.size()) 
	{
        if (q.size() == 1)
		{
            printf("%d>",q.front());
			q.pop();
            break;
        }
        
        for (int i = 1; i < K; i++)
		{
            q.push(q.front());
            q.pop();
        }
        printf("%d, ",q.front());
        q.pop();
    }
    return 0;
}
