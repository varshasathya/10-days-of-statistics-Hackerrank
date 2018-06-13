
#Objective: 
#In this challenge, we practice calculating the mean, median, and mode. Check out the Tutorial tab for learning materials and an 
#instructional video!

#Sample Input:
10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060

#Sample Output:
43900.6
44627.5
4978


import numpy as np
from scipy import stats
n=int(input())
d=[int(x) for x in input().split()]
mean=sum(d)/n
print(mean)
med=np.median(d)
print(med)
mo=int(stats.mode(d)[0])
print(mo)
