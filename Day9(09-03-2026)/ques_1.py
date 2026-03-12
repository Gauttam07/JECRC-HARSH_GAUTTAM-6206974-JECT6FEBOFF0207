#WAP to find sq of a number if it was even.
                                            # num =  int(input('Enter num: '))
                                            # if num%2 == 0:
                                            #     print(num ** 2)

                                            #lambda num: print(num ** 2) if num%2 == 0 else None

                                            #(lambda num: print(num**2) if num%2 == 0 else None)(int(input()))

#WAP to find the sq of a number if it is even otherwise print cube of it

                                            # result = lambda num: print(num ** 2) if num%2 == 0 else print(num ** 3)
                                            # result(int(input('enter num')))

#Check wether a num is pos, neg, or zero

                                            # num = int(input())
                                            # if num > 0:
                                            #     print('POS')
                                            # elif num < 0:
                                            #     print('NEG')
                                            # else:
                                            #     print('ZERO')


x = lambda num: print('POS') if num > 0 else print('NEG') if num < 0 else print('ZERO')
x(int(input('num: ')))