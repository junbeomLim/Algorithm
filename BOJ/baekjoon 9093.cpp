#include<stdio.h>
#include<stdlib.h>
#include<stack> 
#include<string.h>

using namespace std;

int main() 
{
	stack<char> s;
	char c[100];
	
	scanf("%[^\n]", c);
	
	int i = strlen(c); 
	s.push(*c);
	s.push(*c);	
	printf("%c",s.top());
	s.pop();
}
