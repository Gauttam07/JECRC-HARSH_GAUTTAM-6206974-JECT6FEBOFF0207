'''
-- Operator Overloading: It is a phenomenon of makeing the operators to work on user-defined data types by invoing respective magicn methods.

--Magic Method/Dundar: It is a special type of methods in which double underscores will be there at the starting & ending of the method's name.

-- Example:
   1.__add__
   2.__sub__
   3.__mul__
   4.__floordiv__
   5.__truediv__
   6.__mod__

-- If we don't use operator overloading then what will happen?
    for using the operators inside user-defined data types we have to use operator overloading.

--Syntax:
    class ClassName:
       def __init__(self,val):
           self.val=val
        def __add__(self,ano_obj):
           return self.val+ano_obj.val

        
    obj1= ClassName(val1)
    obj2= ClassName(val2)

    print(obj1+obj2) ##obj1.__add__(obj2)

'''



class ClassName:
       def __init__(self,val):
           self.val=val
       def add(self,*args):
           sum=self.val;
           for i in args:
                sum+=i.val
           return sum
        #    return self.val+ano_obj.val
       
       def __str__(self):
            return str(self.val)
       
       def __add__(self,*args):
           sum=self.val;
           for i in args:
                sum+=i.val
           return ClassName(sum)
       
       def __sub__(self,ano_obj):
            return ClassName(self.val-ano_obj.val)
       def __mul__(self,ano_obj):
            return ClassName( self.val*ano_obj.val)
       def __truediv__(self,ano_obj):
            return self.val/ano_obj.val
       def __floordiv__(self,ano_obj):
            return self.val//ano_obj.val
       def __mod__(self,ano_obj):
            return self.val%ano_obj.val
       

        
obj1= ClassName(10)
obj2= ClassName(20)

# print(obj1+obj2) ##obj1.__add__(obj2)
# print(obj1.__add__(obj2))
# print(ClassName(15.5).__add__(ClassName(19.5)).__add__(ClassName(12)))
# print(ClassName.add(ClassName(10),ClassName(12),ClassName(13),ClassName(14)))
print(ClassName(10)+ClassName(20)+ClassName(30))
print(ClassName(15.5)-ClassName(19.5)-ClassName(12.55))
print(ClassName(15.5)*ClassName(19.5)*ClassName(55))
print(ClassName(15).__floordiv__(ClassName(5)))
print(ClassName(15.5).__truediv__(ClassName(19.5)))
print(ClassName(15.5).__mod__(ClassName(19.5)))