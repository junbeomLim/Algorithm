#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int a[1000001];
int s[1000001]; 
 
int main()
{
    int n; 
	scanf("%d", &n);
    
    for (int i = 0; i < n; i++) 
	{
        scanf("%d", &a[i]);
    }
    stack<int> st; //수열의 위치를 저장하는 스택, 수열 값을 비교하여 내림차순으로 정렬한다. 
    st.push(0);
    
	for (int i = 1; i < n; i++) 
	{ 
        if (st.empty() == 1) //처음에 비교할 값 저장 
		{
		   st.push(i);
        }
        while (st.empty() != 1 && a[st.top()] < a[i]) //오큰수를 나오면 오큰수보다 작은 수들 모두 반환(오큰수 이전의 수 반환) 
		{
		    s[st.top()] = a[i];
            st.pop();
		}
        st.push(i); 
		//스택에 내림차순으로 저장됨 
	}
    while (st.empty() != 1) //스택에 남은 수들은 오큰수를 발견 못함 
	{
        s[st.top()] = -1;
        st.pop();
    }
    for (int i = 0; i < n; i++) {
        printf("%d ", s[i]);
    }
    return 0;
}

