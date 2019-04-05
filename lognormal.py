
#this is logarithmic distribution goodness of fit test

import math
def assign2():
    lines=[]
    ob=[]
    with open("data.txt") as f:
        for line in f:
            line=line.strip()
            lines.append(float(line))
    ln_xi=[]
    for i in range(0,len(lines)):
        ln_xi.append(math.log(lines[i]))
    mu=sum(ln_xi)/len(lines)
    sigma_sq=0
    for i in range(0,len(ln_xi)):
        sigma_sq=sigma_sq+((ln_xi[i]-mu)*(ln_xi[i]-mu))/len(lines)
    print (mu)
    print (sigma_sq)
    m1=min(lines)
    m2=max(lines)
    print ("min"+str(m1))
    print ("max"+str(m2))
    k=11
    size=(m2-m1)/k
    i=m1
    while(i<=m2):
        ob.append(i)
        i=i+size
    print (ob)
    trap=[]
    #x=[(ob[i]-ob[i-1])/100 for i in range(1,len(ob))]
    h=(ob[1]-ob[0])/100
   # print h
    i=0
    j=1
    observerd=[]
    low=m1
    up=m1+size
    cnt=[0]*k
    while(i<k):
        if(i==k-1):
            for j in range(0,len(lines)):
                if(lines[j]>ob[i]):
                    cnt[i]=cnt[i]+1
            i=i+1
        else:
            for j in range(0,len(lines)):
                if(lines[j]>=low and lines[j]<up):
                    cnt[i]=cnt[i]+1
            low=up
            up=low+size
            i=i+1
    print ("frequency with intervals")
    print (cnt)
    i=0
    j=1
    while(i<len(ob)-1):
        tot=0
        x1=ob[i]+h
        while(x1<ob[j]):
            f_x1=fun(x1,mu,sigma_sq)
            tot=tot+f_x1
            x1=x1+h
        trap.append(tot)
        i=i+1
        j=j+1
    print ("trap")
    print (trap)
    f_of_x_int=[fun(ob[i],mu,sigma_sq)+fun(ob[i-1],mu,sigma_sq) for i in range(1,len(ob))]
    print ("f_of_x")
    print (f_of_x_int)
    #print x
    i=0
    expec=[]
    
    while(i<k-1):
        tot=0
        #print f_of_x_int[i]
        #print trap[i]
        tot=(h/2)*(f_of_x_int[i]+(2*(trap[i])))
        expec.append(tot)
        i=i+1
    print (expec)
    print (sum(expec))
    final=[]
    for i in range(0,len(expec)):
        t=expec[i]*99
        final.append(t)
    print ("final",final)
    print (sum(final))
    ans=0
    print ("cnt",sum(cnt))
    for i in range(0,len(final)):
        ans=ans+math.pow((cnt[i]-final[i]),2)/final[i]
    print("ans",ans)
def fun(x,mu,sigma_sq):
    p=1/math.sqrt((2*math.pi)*sigma_sq)
    q=math.exp(-pow((math.log(x)-mu),2)/2*sigma_sq)
    r=(1/x)*p*q
    return r
assign2()   
    
    
        
    
    
