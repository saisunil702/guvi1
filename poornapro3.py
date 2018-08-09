string,num=map(int,input().split())
lis=list(str(string))
temp=num
while temp>0:
    temp=temp-1
    del(lis[temp])
print("".join(lis))
