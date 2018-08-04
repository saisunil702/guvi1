n=input()
user=list(map(int,input().split()))
temp=0
for num in range(len(user)):
    if (num==user[num]):
        print(num,end=" ")
        temp+=1
if (temp==0):
    print('-1')
