import pickle
#dumps()
#loads()

'''
1) JSON
2) pickle
'''

file = open('temp1.txt', 'ab+')
data = {
    'fullname': 'GeetShrimali',
    'userid': '1212',
    'password': '***'
}
# print(f'Original data: {data}')
# print(f'Type ofOriginal data: {type(data)}')
# print()

enc_data = pickle.dumps(data)
file.write(enc_data)

file.seek(0)

enc_data = file.read()
print(type(enc_data))

ori_data = pickle.loads(enc_data)
print(ori_data, type(ori_data))
# print(f'enc data: {enc_data}')
# print(f'Type of enc data: {type(enc_data)}')
# print()

# dec_data = json.loads(enc_data)
# print(f'dec data: {dec_data}')
# print(f'Type of dec data: {type(dec_data)}')

file.close()
