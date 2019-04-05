import matplotlib.pyplot as plt
import numpy as np
fp=open("3.txt","r")
data=[]
data1=[]
for i in fp.readlines():
    print(float(i))
    data.append(float(i))
for i in range(1,len(data)):
    data1.append(float(data[i]))
#data.remove(data[len(data)-1])
data=data[:-1]
plt.scatter(data,data1)
plt.show()
m1=min(data)
m2=max(data)
print ("max="+str(m1))
print ("max="+str(m2))
n=8
h=(m2-m1)/n
intervals=[]
cnt=[0]*n
i=0
x1=m1
while(i<n):
    intervals.append(x1)
    x1=x1+h
    i=i+1
print(intervals)
x1=m1
x2=x1+h
i=0
low=m1
up=m1+h
while(i<n):
    if(i==n-2):
        for j in range(0,len(data)):
            if(data[j]>intervals[i]):
                cnt[i]=cnt[i]+1
        i=i+1
    else:
        for j in range(0,len(data)):
            if(data[j]>=low and data[j]<up):
                cnt[i]=cnt[i]+1
        low=up
        up=low+h
        i=i+1
print(cnt)
print(sum(cnt))
plt.bar(intervals,cnt,color='green',width=0.5)
plt.show()

