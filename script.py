def add(a,b):
	return a+b
def divistion(a,b):
	if b==0:
		raise ValueError("Zero division is not allowed")
	return a/b

print(add(30,10))
print(divistion(100,0))