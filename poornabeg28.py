number1=int(input())
number2=[int(x) for x in input().split()]
for y in range(number1):
  print(number2[y],y,sep=' ',end="\n")
