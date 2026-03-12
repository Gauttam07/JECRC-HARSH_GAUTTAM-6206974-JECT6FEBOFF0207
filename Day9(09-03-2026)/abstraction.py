'''
Abstraction:
    Hiding the implementation and showing only function to the end user.

Abstract method:
    If a method or a function consist of only declaration, not definition. Then it will be called as abstract method

Abstract class:
    If a class consists of atleast one abstract method, then it will be called as 'Abstract class'

Concrete class:
    It consists of zero(0) abstract method

abc: Module
ABC: Abstract Base Class    
'''

from abc import ABC, abstractmethod

class ATM(ABC):          #abstract class
    @abstractmethod
    def gen_pin(self):
        pass

    @abstractmethod
    def forget_pin(self):
        pass

    @abstractmethod
    def check_bal(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

class SBI_ATM(ATM):
    def gen_pin(self):
        print('It is used to generate ATM pin!')

    def forget_pin(self):
        print('Not able to remember the pin! Then forget now!')

    def check_bal(self):
        print('No balance is there in your account!')

    def deposit(self):
        print('Save yout money by giving ir to me!')

    def withdraw(self):
        print('Do not withdraw the money! Please!')

obj = SBI_ATM()

obj.gen_pin()
obj.forget_pin()
obj.check_bal()
obj.deposit()
obj.withdraw()