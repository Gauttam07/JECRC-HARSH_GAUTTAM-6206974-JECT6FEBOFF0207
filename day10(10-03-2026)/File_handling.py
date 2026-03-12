                                                                        #File Handling

'''file is a type of container in which we ccan contain or store some data'''

'''By using extension name, we can identify what type of data is there inside of it
eg: .py, .mp4, .html, .mp3, .jpg, .jpeg, etc.
'''

'''Before handling any file, taking permission is very much important'''

# open():
#     open('filename.txt'/'absolute_path', mode)

#close():
#   var_name.close()

'''
here , total 3 different modes are present,
1)write (w)
2)read (r)
3)append (a)'''

'''
Write mode:
    1)only write (w)
    2)write + read (w+)
    3)write binary (wb)
    4)write & read binary (wb+)
'''

'''
read mode:
    1)only read (r)
    2)read + write (r+)
    3)read binary (rb)
    4)read & write binary (rb+)
'''

'''
read mode:
    1)only append (a)
    2)append + read  (a+)
    3)append binary (ab)
    4)append & read binary (ab+)
'''

'''
For write operation,
    1)write(str_data): Single line of data
    2)writelines([ line1, line2, ..., line n]): Multiple line of data
'''

#NOTE:
'''
1) In this, if the file is not present, it will create one, then perform write operation
2) If the file is already present, then it will override the prev data with the new one
'''