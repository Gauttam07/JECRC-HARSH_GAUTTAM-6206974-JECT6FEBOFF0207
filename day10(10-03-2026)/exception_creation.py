'''
raise --> It is a keyword, which helps us to throw an error in between a program

Exception Creation,

1) Custom Exception, (raise)
2) User deffined, (raise)
3) Assertion Exception, (assert)
'''

'''
Custom Exception:
    1) we use pre-built Exception classes according to our requirement.
    
    raise ValueError('message')

    VaalueError: message
'''

                                                    # num = 16
                                                    # if num >= 18:
                                                    #     print('eligible for voting and driving')
                                                    # else:
                                                    #     raise KeyboardInterrupt('Age should be greater than or equal to 18!')


'''
--user-defined Exception

1)It is a type of exception in which we can create our own exception classes based based upon our own requirement.
We can also provide names to those classes according to user cases
'''

                                                    # class MyException(Exception):
                                                    #     pass

                                                    # n1, n2 = 10, 0
                                                    # if n2 == 0:
                                                    #     raise MyException('Second num cant be zero!')
                                                    # else:
                                                    #     print(n1 / n2)


'''
Assertion Exception

--Assertion exception can be created by using one keyword called 'Assert'.

assert <condition>. print(ERROR)
print(output)
'''

                                                    # s = input('Enter a string: ')
                                                    # assert s == s[::-1], print('It is not a palindromic string')
                                                    # print('It is a palindrome string')
