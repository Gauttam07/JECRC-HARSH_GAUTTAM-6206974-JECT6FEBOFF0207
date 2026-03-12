'''Exception Handling Approaches:'''

'''
--> Specific Exception Handling
--> Generic Exception Handling
--> Default Exception Handling
'''

#Specific Exception Handling:
'''
If we are aaware of the error or exception, then we can go with 'specific'

try:
    problem
    statement
except errorname:
    resolution/
    solution code

-->
'''

                                                # n1, n2 = 21, 0
                                                # try:
                                                #     result = n1/n2
                                                #     print(result)
                                                # except ZeroDivisionError:
                                                #     print('Kindly refrain from using zero as second number!')

#Generic Exception Handling:
'''
It is a type of exception handling approach in which there is no need to pass any particular exception class name.
Instead of we can use parent 'exception' class called 'Exception' 
-- Using 'generic exception handling' we cant handle keyboard interruptions'''
                                                # try:
                                                #     a, b, c = 1, 2
                                                #    #except ValueError:
                                                # except Exception:
                                                #     print('for performing mvc, num. of variables should be equals to no of values!')
                                                    
                                                # try:    
                                                #     print(a, b, c)
                                                #    #except NameError:
                                                # except Exception:
                                                #     print('Identifier not in memory'

import time
try:
    while True:
        print(time.time())
except KeyboardInterrupt:
    print('Done!')


#Default Execution Handling
'''It is a type of exception handling in which we can handle all types of errors or exceptions except 'Syntax Error' '''

import time
try:
    while True:
        print(time.time())
except:
    print('Done!')
