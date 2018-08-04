num=int(input())
lis=[int(x) for x in input().split()]
for i in range(0,num):
a=lis[i]
while(a==i):
print(a,end="")
else:
print("-1)"
