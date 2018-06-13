"""
Objective 
In the previous challenge, we calculated a mean. In this challenge, we practice calculating a weighted mean. 

Sample Input:
5
10 40 30 50 20
1 2 3 4 5

Sample Output:
32.0 """

n=int(input())
a=[int(x) for x in input().split()]
b=[int(y) for y in input().split()]
s=sum([a*b for a,b in zip(a,b)])
print(round((s/sum(b)),1))
