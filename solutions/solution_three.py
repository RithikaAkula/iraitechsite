def perform_compute_2(x, y, a, b):
    
    result = pow(x/y,a+b)

    return result

'''

# Driver Code

print("The given expression is reduced to '(x / y) ^ (a + b)'")
input_one = int(input("Enter value of x: "))
input_two = int(input("Enter value of y: "))
input_three = int(input("Enter value of a: "))
input_four = int(input("Enter value of b: "))

if isinstance(input_one,int) and isinstance(input_two,int) and isinstance(input_three,int) and isinstance(input_four,int):
    
    answer = perform_compute_2(input_one, input_two, input_three, input_four)
else:
    
    answer="Enter valid integers."

print(answer)

'''
