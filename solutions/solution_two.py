def nth_term(value) :
    nth = 0
 
    if (value % 2 == 1) :
        nth = (value * value) + 1
    else :
        nth = (value * value) - 1
 
    return nth


'''

# Driver Code

print(nth_term(9))

'''
