## Check whether a num is postive or, negative or, zero.

# num=int(input())
# if num>0:
#     print('POS')
# elif num<0:
#     print('NEG')
# else:
#     print('ZERO')

## FOR LAMBDA
# if num>0:
#     print('POS')
# else:
#     if num<0:
#         print('NEG')
#     else:
#         print('Zero')

result=lambda num: print('POS') if num>0 else print('NEG') if num<0 else print('ZERO')
result(int(input('Enter the number to check: ')))

