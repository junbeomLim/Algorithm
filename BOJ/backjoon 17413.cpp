#include <bits/stdc++.h>
#include <string>
#include <stack>
#include <algorithm>

using namespace std;
 
int main()
{
    string s; //시간 초과를 막기 위해 string 사용, 문자열 저장 공간
    
    stack<char> st;
    int state = 0;  // 상태 변수, 이전 상태가 < 이었다면 1, > 이었다면 0
    
	getline(cin, s); //시간 초과를 막기 위해 사용, 문자열 받음

//스택에는 뒤집혀질 문자열 저장    
	for (int i = 0; i < s.size(); i++)
	{    
        
        if (s[i] == '>')
		{
            printf(">");
            state = 0;
        }
        else if (s[i] == '<')
		{
            while (!st.empty()) // 이전까지의 문자 거꾸로 출력
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
    	else if (state == 1) //태그 부분 그대로 출력
		{
			printf("%c", s[i]);
		}
        else  //스택에 거꾸로 뒤집을 문자 저장
        {
        	st.push(s[i]);
        }
	}
	while (!st.empty()) //마지막 남은 문자열 뒤집어서 출력
	{
        printf("%c", st.top());
        st.pop();
    }
    printf(" ");
}

