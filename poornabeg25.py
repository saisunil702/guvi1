num=int(input())
lis=[int(y) for y in input().split()]
s=sorted(lis)
if num%2==0:
    x=(num-1)//2
    y=x+1
    z=(s[x]+s[y])/2
    print(z)
else:
    x=num//2
    print(s[x])





