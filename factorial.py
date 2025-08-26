n = int(input("Enter your number: "))
fact = 1

for i in range(1, n+1):
	fact = fact * i

print(f"The factorial of {n} is : ", fact)
   


def factorial(n):
    if n < 0:
        return -1
    elif n < 2:
        return 1
    else:
        return n * factorial(n - 1)
    
def factorial_iterative(n):
    if n < 0:
        return -1
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
            
print(factorial(6))    
print(factorial_iterative(6))   



