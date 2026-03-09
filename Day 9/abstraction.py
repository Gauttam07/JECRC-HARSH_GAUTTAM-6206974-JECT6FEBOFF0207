'''
Abstraction: 
    Hiding the internal implementation and showing only functionality
    
Abstract method:
    If a method/function consists of only declarartion not definition then it will be called as "Abstract Method"


Abstract Class:
    If a class consists of at least one abstract method, it will be called as "Abstract class"


Concrete Class:
    It consists of zero(0) abstract method.  


abc: Module
ABC: Abstract Base Class 

    '''


from abc import ABC,abstractmethod

class ATM(ABC):
    def generate_pin(self):
        pass

    @abstractmethod
    def forget_pin(self):
        pass

    @abstractmethod
    def check_bal(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass


class SBI_ATM(ATM):
    def generate_pin(self):
        print('It is used to generate ATM pin!')

    def forget_pin(self):
        print('Not remmenber the pin! Then forget now!')

    def check_bal(self):
        print('No balance is there in your account :)')

    def deposit(self):
        print('Save your money by giving it to me')

    def withdraw(self):
        print('Do not withdraw the monet please! Please!')

obj=SBI_ATM()

obj.generate_pin()
obj.forget_pin()
obj.check_bal()
obj.deposit()
obj.withdraw()
# obj=ATM()

