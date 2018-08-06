n=int(input())
lis=[int(x) for x in input().split()]
s = sorted(lis)
for x in range(n):
    print(s[x],end=' ')
