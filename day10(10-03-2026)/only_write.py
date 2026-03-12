file = open('temp.txt', 'w+')
#file.write('Hello')
file.writelines([
    'first line\n',
    'second line\n',
    'third line\n',
    'fourth line\n',
    'fifth line\n',
    'sixth line'
])
file.seek(0) #to make python interpreter to point at a specific index, we use seek(index)
print(file.read())

file.close()