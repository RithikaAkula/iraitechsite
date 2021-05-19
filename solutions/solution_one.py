def perform_compute_1(x, n):

    result = (1 - pow(1/x,n))/(x-1)

    return result


def nth_term(x, n):
    if n==0:
        return 1
    
    elif n>0:
        return (1/x * nth_term(x, n-1))

def compute(x, n):
    # Recursive approach
    
    if n==0:
        return 0
    
    return nth_term(x,n)+compute(x, n-1)

'''

# Driver Code

print("The given expression is reduced to '(1 - 1/x^n) / (x - 1)'")
input_one = int(input("Enter value of x: "))
input_two = int(input("Enter value of n: "))

if isinstance(input_one,int) and isinstance(input_two,int):
    
    answer = perform_compute_1(input_one,input_two)
else:
    
    answer="Enter valid integers."

print(answer)

'''