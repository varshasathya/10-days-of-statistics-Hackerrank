"""
Objective 
In this challenge, we practice calculating the interquartile range. 
Recommended to complete the Quartiles challenge before attempting this problem.

Sample Input:
6
6 12 8 10 20 16
5 4 3 2 1 5

Sample Output:
9.0 """

n=int(input())
x=[int(num) for num in input().split()]
f=[int (nums) for nums in input().split()]
s=[]
for i in range(n):
    s+=[x[i]]*f[i]
s.sort()
m=len(s)//2
def median(r):
    mid=len(r)//2
    if(len(r)%2==0):
        return (r[mid-1] + r[mid]) / 2
    else:
        return r[mid]
if (len(s) % 2 == 0):   
    Q1 = median(s[:m])
    Q3 = median(s[m:])
else:
    Q1 = median(s[:m])
    Q3 = median(s[m+1:])

iq=Q3-Q1
print(round(float(iq),1))
