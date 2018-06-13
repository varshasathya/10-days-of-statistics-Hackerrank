"""
Objective 
In this challenge, we practice calculating quartiles.

Sample Input:
9
3 7 8 5 12 14 21 13 18

Sample Output:
6
12
16 """

n = int(input())
a = sorted([int(i) for i in input().split()])
m = len(a) // 2 

def median(m_nu):
    
    mid = len(m_nu) // 2  
    if (len(m_nu) % 2 == 0):  
        return (m_nu[mid-1] + m_nu[mid]) / 2
    else:
        return m_nu[mid]
if (len(a) % 2 == 0):    
    Q1 = median(a[:m])
    Q3 = median(a[m:])
else:
    
    Q1 = median(a[:m])
    Q3 = median(a[m+1:])

print(int(Q1))
print(int(median(a)))
print(int(Q3))
