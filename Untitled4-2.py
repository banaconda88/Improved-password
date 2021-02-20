#!/usr/bin/env python
# coding: utf-8

# In[2]:


b = input("What would you like to set your password as?")
a = input("What is your password?")
n = 0
while a != b:
    print("This password is incorrect.")
    a = input("What is your password?")
    n = n + 1
else:
    print("Correct.")
    print("You got your password wrong", n ,"times.")

