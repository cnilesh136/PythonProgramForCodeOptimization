tac={}
code=input("Enter the 3 address code : ").split()
exp1=[]
exp2=[]

for i in code:
    x,y=i.split("=")
    exp1.append(x)
    exp2.append(y)
    tac[x]=y
print("=====================================")
print("Intermediate Code:")
for k,v in tac.items():
    print(k,"=",v)
for k in exp1:
    delet=1
    for ex in exp2:
        if k in ex or tac[k] in exp1:
            delet=0
    if delet==1:
        del tac[k]
print("=====================================")
print("After Dead Code Elimination:")
for k,v in tac.items():
    print(k,"=",v)

same={}
for k1,v1 in tac.items():
    for k2,v2 in tac.items():
        if v1==v2 and k1!=k2 and (k1 not in same and k2 not in same):
            #print("same found!!"
            same[k1]=k2
for k,v in same.items():
    del tac[k]

optimizeTAC={}
for k,v in tac.items():
    s1=v
    for s in s1:
        if s in same:
            v=v.replace(s,same[s])
    optimizeTAC[k]=v

print("=====================================")
print("After Common Expression Elimination:")
for k,v in optimizeTAC.items():
    print(k,"=",v)
print("=====================================")
print("OPTIMIZED CODE:")
for k,v in optimizeTAC.items():
    print(k,"=",v)
print("=====================================")
