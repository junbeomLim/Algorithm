#include <iostream>
#include <queue>
 
using namespace std;

int n;
int first = 0;
int second = 0;
 
int main() {
    queue<int> q;
 	q.push(0);
 	q.push(1);
 
    scanf(" %d", &n);
 	for(int i = 0; i <= n; i++)
 	{
 		first += q.front();
 		q.pop();
 		q.push(first);
	}
 	
 	printf("%d",first);
    return 0;
}
