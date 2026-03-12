'''
lambda(Anonymous function):
    1) Lambda is a keyword, which is used to create anonymous functions.
    2) for calling lambda fun, we can store the address of lambda inside the variable. By invoking variable name, we can call the function
'''

#lambda args: <exp>
result = lambda a,b: a + b
print(result)
print(result(3, 4))

(lambda a,b: print(a+b))(int(input('First num: ')), int(input('Sec num:')))
