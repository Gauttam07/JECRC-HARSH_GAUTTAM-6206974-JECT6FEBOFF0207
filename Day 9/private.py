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

class Temp:
    __a=100

    def __status(self):
        print('Class name is Temp!')
    def get(self):
        print(self.__a)
    def set(self,new_val):
        self.__a=new_val


obj=Temp()
# print(obj.__a)
# obj.__status()


print('Accesing method')


## Accessing
print(obj._Temp__a)
print(Temp._Temp__a)
obj._Temp__status()

print('Updation method')


##Updation
obj._Temp__a='0123456789'
print(obj._Temp__a)


def new_method():
    print('Method updated')


obj._Temp__status=new_method
obj._Temp__status()

print()
print('Get and set method')
print()

##Get and set method

obj.get()
obj.set(1)
obj.get()
print(obj._Temp__a)

print()
print('By using @property decorator')
print()
## By using @property decorator

class Temp1:

    __c=19

    @property
    def get(self):
        print(self.__c)

    @get.setter
    def set(self,new_val):
        self.__c=new_val

obj1=Temp1()
obj1.get
obj1.set=10000
obj.get
print(obj1._Temp1__c)
