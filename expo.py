import matplotlib.pyplot as plt
import numpy as np
import math as mt
data=[]
intervals=[]
observed=[]
def intervals_cal(data,intervals,lam,p):
	i=p
	intervals.append(0)
	while(i<1):
		a=(-1/lam)*mt.log(1-i)
		intervals.append(a)
		i=i+p
	#print (intervals)
	#print (len(intervals))
def observed_cal(data,observed,intervals):
	n=len(intervals)
	i=0
	observed=[0]
	observed=observed*n
	print(len(observed))
	for i in range(1,len(intervals)):
		for j in range(0,len(data)):
			if(data[j]>=intervals[i-1] and data[j]<intervals[i]):
				observed[i-1]=observed[i-1]+1
	for j in range(0,len(data)):
		if(data[j]>=intervals[n-1]):
			observed[n-1]=observed[n-1]+1
	print(sum(observed))
	return observed
def chi(observed,e,n):
	chisq=[]
#	chisq=chisq*n
	for i in range(0,n):
		ch=pow(observed[i]-e,2)/e
		chisq.append(ch)
	return chisq
	
fp=open("jerry_bank_data.txt","r")
data=[]
chi_sq=[]
for i in fp.readlines():
	data.append(float(i))
print (data)
total_data=len(data)
#n=total_data/5
n=8
m1=min(data)
m2=max(data)
mean=sum(data)/total_data
lam=1/mean
p=(total_data/n)/total_data;
e=total_data*p

print("probability",p)
print("expected",e)
print ("mean",mean)
print ("lam",lam)
print ("min",m1)
print ("max",m2)
#print(data)
intervals_cal(data,intervals,lam,p)
print (intervals)
#print (len(intervals))
observed=observed_cal(data,observed,intervals)
print ("observed",observed)
chi_s=chi(observed,e,n)
print ("chi_square",chi_s)
print(sum(chi_s))
