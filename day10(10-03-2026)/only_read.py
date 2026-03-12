file = open('temp.txt', 'r')

#print(file.read())

#print(file.readline())

print(file.read())
file.seek(0)
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
file.seek(0)
print(file.readlines())

file.close()


'''
read(): display file content as it is
readline(): display single line of data at a time
readlines(): ddisplay list of data
'''

# file = open('notes.txt', 'r')

# print(file.read())

# file.close()