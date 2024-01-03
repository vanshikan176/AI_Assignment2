#!/usr/bin/env python
# coding: utf-8

# In[4]:


n=int(input("Enter no of elements in Set 1: "))
s1=set()
s2=set()
x=0
while x<n:
    e=int(input("Enter element of Set 1: "))
    s1.add(e)
    x=x+1  
m=int(input("Enter no of elements in Set 2: "))
x=0
while x<m:
    e=int(input("Enter element of Set 2: "))
    s2.add(e)
    x=x+1
uni_set = s1.union(s2)
inter_set = s1.intersection(s2)
diff_set = s1.difference(s2)
symdiff_set = s1.symmetric_difference(s2)
print("Union of Set 1 and Set 2 is ",uni_set)
print("Intersection of Set 1 and Set 2 is ",inter_set)
print("Difference of Set 1 and Set 2 is ",diff_set)
print("Symmetric difference of Set 1 and Set 2 is ",symdiff_set)


# In[ ]:




