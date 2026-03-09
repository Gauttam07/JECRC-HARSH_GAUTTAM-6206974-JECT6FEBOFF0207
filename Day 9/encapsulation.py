'''
Encapsulation:
    1.It is use to provide security to the data (data means variables/prop & methods presednt inside a class)


How to provide security to the data?
   TO provide security, we have to use access specifiers.
      1.public,
      2.Protected,(soft barrier)
      3.Private,

Access Specifier
    It described who can access the class members(properties & methods).

'''


## Example For public access specifier
class Temp:
    a,b,*c,d='Hello'

    def greeting(self):
        print('Good Afternoon user :)')
# print(Temp.a)

class c2(Temp):
    pass

print(c2.a)




## Protected Access Specifier

class Temp:
    __a=10
    _b='I Love Python !'

obj=Temp()
print(obj._b)## single _ is soft barrier it can easily access(Protected)
# print(obj.__a)## double _ is private it cant access


## Private

class Temp1:
    __a=100

    def __status(self):
        print('Class name is Temp!')


obj=Temp1()
# print(obj.__a)
# obj.__status()

'''
access Private
  1. By using syntax,
  2.get & set method 
  3.by using @property decorator(setter)
  '''

## By using Syntx 
'''
obj_name/class_name._CN_prop_name/__method_name(Accessing)
obj_name/class_name._CN__MemberName=NewValue(Modifying)
'''

print(obj._Temp1__a)
print(Temp1._Temp1__a)
obj._Temp1__status()


    