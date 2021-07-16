numbers=(1,2,3,4,5,6,7,8,9)
count_even=1
count_odd=-1
for value in range(1,10):
	if(value%2==0):
		count_even=count_even+1
	else:
		count_odd=count_odd+1
print("Number of even numbers:",count_even)
print("Number of odd numbers:",count_odd)


