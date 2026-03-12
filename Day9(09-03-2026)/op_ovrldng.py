'''
it is a phenomenon of making the operators to work on user defined data types by invoking magic methods'''

'''
magic method/dundar: It is a special type of method in which double underscores will be there at the start and end of meethod's name'''

'''
eg:
__add__
__sub__
__mul__
__floordiv__
__truediv__
__mod__

if we dont use overloading then:
        for using operators inside user-defined data types we have to use operator overloading
'''

'''
Syntax:
    class Classname:
        def __init__(self, val)
            self.val = val
            
        def __add__(self, ano_object):
            return self.val + ano_obj.val
            
    obj1 = Classname(val1)
    obj2 = Classname(val2)
    print(obj1 + obj2)
'''


'''
-- Operator Overloading: It is a phenomenon of making the operator to work on user-define data types by invoking  respective magic methods.

-- Magic Mehtod/Dundar: It is a special type of methods in which double underscore will be there at the starting & ending of the method's name.

-- Example:
1. __add__,
2. __sub__,
3. __mul__,
4. __floordiv__,
5. __truediv__,
6, __mod__,

-- If we don't use operator overloading then what will happen?
   For using the operators inside user-define data types we ahve to use operator overloading.

-- Syntax:
   class ClassName:
        def __init__(self,val):
            self.val=val

        def __add__(self,ano_obj):
            return self.val + ano_obj.val

    obj1=ClassName(val1)
    obj2=ClassName(val2)

    print(obj1 + obj 2)  ## obj1.a+__add__(obj2)      
                     
'''

class MyDT:
    def __init__(self,val):
        self.val=val

    def __str__(self):
        return str(self.val)
    
    def __add__(self,*ano_obj):
        # sum=self.val
        # for i in args:
        #     sum+=i.val
        # return sum   
        sum = self.val
        for i in ano_obj:
            sum += i.val
        return MyDT(sum) 

    
    
    def __sub__(self, *ano_obj):
        sub = self.val
        for i in ano_obj:
            sub -= i.val
        return MyDT(sub) 

    
    def __mul__(self,*ano_obj):
        #return self.val * ano_obj.val
        mul = self.val
        for i in ano_obj:
            mul *= i.val
        return MyDT(mul) 
    
    def __floordiv__(self, ano_obj):
        return self.val//ano_obj.val
    
    def __truediv__(self, ano_obj):
        return self.val / ano_obj.val
    
    def __mod__(self, ano_obj):
        return self.val % ano_obj.val



# print(MyDT.add(MyDT(123),MyDT(3),MyDT(5)))      
# print(MyDT(123) - MyDT(200))
print(MyDT(10) + MyDT(20) + MyDT(30))
print(MyDT(50) - MyDT(20) - MyDT(10))
print(MyDT(50) * MyDT(20) * MyDT(10))
# print(MyDT(10) * MyDT(20))