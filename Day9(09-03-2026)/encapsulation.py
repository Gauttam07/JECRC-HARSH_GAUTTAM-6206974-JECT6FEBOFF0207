'''
1) it is used to provide security to the data(data means var/prop or methods present inside class)

How to provide security to data?
To provide security, we have to use access specifiers.
    1) public
    2)protected(soft barrier '_')
    3)private

Access Specifier:
    It describes who can access the class members(prop/methods)
'''

                                                # Example of public access specifier
                                                # class Temp:
                                                #     a,b,*c,d = 'HELLO'

                                                #     def greeting(self):
                                                #         print('Good Afternoon User :)')

                                                # print(Temp.c)

#protected access specifier
                                                # class Temp:
                                                #     _a = 10
                                                #     __b = 'hehe'

                                                # obj = Temp()
                                                # print(obj._a)
                                                # print(obj.__b)   #will give error(private)


#private access specifier

                                        # class Temp:
                                        #     __a = 100

                                        #     def __status(self):
                                        #         print('Classs name is Temp!')

                                        #     def get(self):
                                        #         print(self.__a)
                                        #     def set(self, new_val):
                                        #         self.__a = new_val



                                        # obj = Temp()

#get and set method
                                        # obj.get()
                                        # obj.set(1)
                                        # obj.get()
# print(obj.__)
#obj.__status()

'''
1) using syntax
2) get and set method
3) by using @property decorator(setter)
'''
#By using syntax
'''
obj_name/class_name._CN__prop_name/__method_name (Accessing)

obj_name/class_name._CN___MemberName = NewValue (Modifying)
'''

                                    # print(obj._Temp__a)
                                    # print(Temp._Temp__a)
                                    # obj._Temp__status()

                                    # def new_method():
                                    #     print('Method got changed')

                                    # obj._Temp__a = '0123456789'
                                    # print(obj._Temp__a)
                                    # obj._Temp__status = new_method
                                    # obj._Temp__status()



#Using @property decorator

class Temp():
    __a = 10

    @property
    def get(self):
        print(self.__a)

    @get.setter
    def set(self, new_val):
        self.__a = new_val

obj = Temp()
obj.get
obj.set = 10000
obj.get