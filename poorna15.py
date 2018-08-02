a, b = map(int, input().split())
for i in range(a,b):
	if(i%2!=0 and i!=a and i!=b):
		print(i.split())
