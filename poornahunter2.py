nm=int(input())
lis=[int(x) for x in input().split()]
kk=sorted(lis)
kk.reverse()
for i in range(0,nm):
    print(kk[i],end="")
