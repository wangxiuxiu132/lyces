a=[20,96,2,15,3]
for i in range(len(a)-1):
	for j in range(len(a)-1-i):
		if a[j]>a[j+1]:
			a[j],a[j+1]=a[j+1],a[j]
print(a)
