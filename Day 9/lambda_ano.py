'''
lambda(Anonymous Function):
   1.Lambda is a keyword. Which is used to create anonymous functions.
   2. For calling the lambda function, we can store the address of lambda inside a variable. By invoking the var_name, we can call the function.
'''
'''

var_name=lambda args:<exp>
var_name(args)## Calling the lambda function
'''


## lambda args:<exp>
result=lambda a,b:a+b

print (result)
print(result(1,2))

(lambda a,b:print(a+b))(int(input('First Num: ')),int(input('Sec Num: ')))


