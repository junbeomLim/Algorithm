#include <bits/stdc++.h>
#include <string>
#include <stack>
#include <algorithm>

using namespace std;
 
int main()
{
    string s; //�ð� �ʰ��� ���� ���� string ���, ���ڿ� ���� ����
    
    stack<char> st;
    int state = 0;  // ���� ����, ���� ���°� < �̾��ٸ� 1, > �̾��ٸ� 0
    
	getline(cin, s); //�ð� �ʰ��� ���� ���� ���, ���ڿ� ����

//���ÿ��� �������� ���ڿ� ����    
	for (int i = 0; i < s.size(); i++)
	{    
        
        if (s[i] == '>')
		{
            printf(">");
            state = 0;
        }
        else if (s[i] == '<')
		{
            while (!st.empty()) // ���������� ���� �Ųٷ� ���
			{
                printf("%c", st.top());
                st.pop();
            }
            printf("<");
            state = 1;
        }
        else if (s[i] == ' ' || s[i] == '\n') // state = 0;
		{
            while (!st.empty()) 
			{
                printf("%c", st.top());
                st.pop();
            }
            printf(" ");
        }
    	else if (state == 1) //�±� �κ� �״�� ���
		{
			printf("%c", s[i]);
		}
        else  //���ÿ� �Ųٷ� ������ ���� ����
        {
        	st.push(s[i]);
        }
	}
	while (!st.empty()) //������ ���� ���ڿ� ����� ���
	{
        printf("%c", st.top());
        st.pop();
    }
    printf(" ");
}

