money = int(input())
last_money = 1000 - money

a = last_money//500
last_money = last_money - a*500
b = last_money//100
last_money = last_money - b*100
c = last_money//50
last_money = last_money - c*50
d = last_money//10
last_money = last_money - d*10
e = last_money//5
last_money = last_money - e*5
f = last_money//1
last_money = last_money - f*1

print(a+b+c+d+e+f)