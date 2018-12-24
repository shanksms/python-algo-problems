# Python program for Memoized version of nth Fibonacci number

# Function to calculate nth Fibonacci number
def fib(n, lookup):

	# Base case
	if n == 0 or n == 1 :
		lookup[n] = n

	# If the value is not calculated previously then calculate it
	if lookup[n] is None:
		lookup[n] = fib(n-1 , lookup) + fib(n-2 , lookup)

	# return the value corresponding to that value of n
	return lookup[n]
# end of function

def fib_method_2(n):
    lookup = [None] * (n+1)
    #0, 1, 1, 2, 3 oth number is 0
    if n is 0 or n is 1:
        return n

    lookup[0], lookup[1] = 0, 1
    for i in range(2, n + 1):
        lookup[i] = lookup[i - 1] + lookup[i - 2]
    return lookup[n]



# Driver program to test the above function
def test1():
	n = 34
	# Declaration of lookup table
	# Handles till n = 100
	lookup = [None]*(101)
	print ("Fibonacci Number is ", fib(n, lookup))
def test2():
    print(fib_method_2(500))

if __name__=="__main__":
	test2()

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
