#!/usr/bin/env python
# coding: utf-8

# In[3]:


n = int(input("Enter the number of elements: "))
list1 = []
for i in range(n):
    element = int(input("Enter element {i + 1}: "))
    list1.append(element)
for i in range(n):
    if list1[i]>0:
        print(list1[i])

