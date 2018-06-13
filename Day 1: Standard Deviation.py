"""
Objective:
In this challenge, we practice calculating standard deviation. 

Sample Input
5
10 40 30 50 20

Sample Output
14.1 """

n=int(input())
a=[int(i) for i in input().split()]
mean=sum(a)/n
v=0
for i in a:
    b=(i-mean) ** 2
    v+=b
    
sd= (v/n)**0.5
print(round(float(sd),1))
