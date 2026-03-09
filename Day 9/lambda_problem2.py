##Wap to find the square of a number if it is even otherwise print cube of it.

result = lambda num:print(num*num) if num%2==0 else print(num**3)
result(int(input('Enter the number : ')))