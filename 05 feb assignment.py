#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q1. Explain Class and Object with respect to Object-Oriented Programming. Give a suitable example.


# In Python, a class is like a blueprint or a template that you can use to create objects with similar characteristics and behaviors. Imagine a class as a cookie cutter, and each object created from the class as a cookie. The cookie cutter determines the shape and characteristics of the cookie, just like how the class determines the attributes and methods of the objects created from it.
# 
# For example, let's say you want to create objects called "Fruit" that have a color and a flavor. You can define a class called "Fruit" that has two attributes: color and flavor. You can also define methods for the class, such as a get_color method that returns the color of the fruit.

# In[5]:


class fruits:
    def __init__(self,colour,flavour):
            self.colour =colour
            self.flavour=flavour
            
    def get_color(self):
        return self.colour
    
    
    def get_flavor(self):
        return self.flavour
    
    
apple =fruits("red","sweet")
orange =fruits("orange","citrus")
mangoes =fruits("yelloiesh","very_Sweet")

print("The apple is", apple.get_color(), "and tastes", apple.get_flavor())
print("The orange is", orange.get_color(), "and tastes", orange.get_flavor())
print("The mangoes is", mangoes.get_color(), "and tastes", mangoes.get_flavor())


# In[1]:


class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
            
    def get_balance(self):
        return self.balance
    

# Create a bank account object
account = BankAccount("123456", "Alice", 1000)

# Make some deposits and withdrawals
account.deposit(500)
account.withdraw(200)
account.withdraw(1500)

# Check the balance
print("Current balance:", account.get_balance())


# In[ ]:


# Q2. Name the four pillars of OOPs.


# # The four pillars of Object-Oriented Programming (OOPs) are:
# 
# Encapsulation: It is the technique of wrapping data and code that operates on the data into a single unit. This unit is called a class, and it provides the interface through which objects interact with the outside world. Encapsulation provides data hiding, which means that the internal details of an object are hidden from the outside world and can only be accessed through methods provided by the object.
# 
# Inheritance: It is the process by which one class acquires the properties and behaviors of another class. The class that is being inherited from is called the parent or base class, and the class that inherits is called the child or derived class. Inheritance allows the creation of a hierarchical classification of objects, and it enables the reusability of code.
# 
# Polymorphism: It is the ability of objects to take on many forms. In OOPs, polymorphism allows objects of different classes to be treated as if they were objects of a common superclass. Polymorphism enables the use of a single interface to represent different behaviors.
# 
# Abstraction: It is the process of hiding complex details and presenting only the essential features of an object. Abstraction allows the creation of abstract classes and interfaces, which provide a high-level view of objects and their behaviors, without getting into the specifics of their implementation. Abstraction allows the developer to focus on the essential aspects of an object and ignore the rest.

# In[6]:


#Q3. Explain why the __init__() function is used. Give a suitable example.


# In Python, the __init__() function is a special method that is used to initialize an object's attributes when it is created. It is automatically called when an object of a class is instantiated, and it takes the self parameter, which refers to the object being created, and any additional parameters required for initialization

# In[ ]:


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("Hi, my name is", self.name, "and I am", self.age, "years old.")

person1 = Person("John", 25)
person2 = Person("Sarah", 30)

person1.introduce()
person2.introduce()


# In[ ]:


get_ipython().set_next_input('Q4. Why self is used in OOPs');get_ipython().run_line_magic('pinfo', 'OOPs')


# n Object-Oriented Programming (OOPs), the self parameter is used to refer to the current object being manipulated. It is a reference to the instance of the class that the method is being called on.
# 
# When a method is called on an object, Python automatically passes the object as the first parameter to the method. By convention, this parameter is named self, although any other valid identifier can be used.

# Q5. What is inheritance? Give an example for each type of inheritance.

# Inheritance is a mechanism in Object-Oriented Programming (OOP) that allows a class to inherit the properties (methods and attributes) of another class. The class that is being inherited from is called the parent class, while the class that inherits is called the child class.
# 
# There are four types of inheritance in Python:
# 
# Single Inheritance
# Multiple Inheritance
# Multi-Level Inheritance
# Hierarchical Inheritance

# In[ ]:




