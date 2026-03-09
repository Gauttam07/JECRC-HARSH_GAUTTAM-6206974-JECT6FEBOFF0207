##WAP to find the square of a number if it is even.

num=int(input('enter a number: '))
if num%2==0:
    print(num**2)

result=lambda num:print(num**2)if num%2==0 else print('Do nothing and eat 5 star')
result(13)

## we cant use loop in lambda but by using map
