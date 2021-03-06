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
    stack<int> st; //������ ��ġ�� �����ϴ� ����, ���� ���� ���Ͽ� ������������ �����Ѵ�. 
    st.push(0);
    
	for (int i = 1; i < n; i++) 
	{ 
        if (st.empty() == 1) //ó���� ���� �� ���� 
		{
		   st.push(i);
        }
        while (st.empty() != 1 && a[st.top()] < a[i]) //��ū���� ������ ��ū������ ���� ���� ��� ��ȯ(��ū�� ������ �� ��ȯ) 
		{
		    s[st.top()] = a[i];
            st.pop();
		}
        st.push(i); 
		//���ÿ� ������������ ����� 
	}
    while (st.empty() != 1) //���ÿ� ���� ������ ��ū���� �߰� ���� 
	{
        s[st.top()] = -1;
        st.pop();
    }
    for (int i = 0; i < n; i++) {
        printf("%d ", s[i]);
    }
    return 0;
}

