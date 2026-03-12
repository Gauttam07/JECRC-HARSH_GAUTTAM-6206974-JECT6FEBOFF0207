file = open('jecrc.txt', 'a+')

#file.write('JECRC FOUNDATION*')

# file.writelines([
#     '\ngood\n'
#     'better\n'
#     'best'
# ])

file.seek(0)
print(file.read())
file.close()