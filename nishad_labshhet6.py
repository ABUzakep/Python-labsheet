#!/usr/bin/env python
# coding: utf-8
1. Create a dictionary student to store the rollnumber and name of students in a class.
 Accept name and roll number of students and add it to the dictionary. 
# In[ ]:


stud={}
n=input("enter name")
r=input("enter roll")
stud["name"]=n
stud["roll"]=r
print(stud)

 How will you store details of two students with same name? 
# In[3]:


stud={}
n=input("enter name")
r=input("enter name")
stud["name"]=n
stud["name"]=r
print(stud)

 Can the keys in dictionary be duplicated? 

# In[ ]:


#no
stud={}
n=input("enter name")
r=input("enter name")
stud["name"]=n
stud["name"]=r
print(stud)

#  Use for loop to iterate over items of dictionary and print it. 

# In[25]:


stud={'name': 'nisha', 'name2': 'nishad',"batch":"bca"}
for key,value in stud.items():
    print(key,value)

Search for an item in dictionary and print it. 
# In[61]:


stud={"name":"nisha","name2":"nishad","batch":"bca"}
k=input("enter the values")
f=False
for key,value in stud.items():
    if key==k or value==k:
        f=True
        break;
if f==True:
    print("yes")
else:
    print("not")


# In[ ]:


Sort items of a dictionary based on key and print it

2. Create a dictionary to store months of a year. Accept a month from the user and display its
name from the dictionary. Perform operations like delete and edit dictionary items. 
# In[69]:


stud={"name":"nisha","name2":"nishad","batch":"bca"}
j=sorted(stud.items())
print(j)
print(sorted(stud,reverse=True))
print(sorted(stud.items()))
print(dict(sorted(stud.items()))) 

3. Write a Python program to get the maximum and minimum values of a dictionary. 

# In[ ]:


dict = {"Hi":1,"Helo":2,"Whats up":3}
smal = dict["Hi"]
lar = 0
for i in dict:
    if dict[i] > lar:
        lar = dict[i]
    if dict[i] < smal:
        smal = dict[i]
print(lar)
print(smal)

4. Write a Python script to generate and print a dictionary that contains a number (between 1
and n) in the form (x, x*x).
Sample Dictionary (n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25} 
# In[ ]:


n = int(input())
d = {}
for i in range(1,n+1):
    d[i] = i**2
print(d)

5. Given two lists L1=[1,2,3,4,5], L2=[“one”,”two”,three”,”four”,”five”], create a dictionary with
items from L1 as keys and items of L2 as values. 
# In[ ]:


l1 = [1,2,3,4,5]
l2 = ["one","two","three","four","five"]
d = {}
for i in range(0,len(l1)):
    d[l1[i]] = l2[i]
print(d)

6. Given a list of keys, write a program to remove those keys from a dictionary. 

# In[ ]:


mon = {1:"Jan",2:"Feb",3:"Mar",4:"Apr",5:"May",6:"June",7:"July",8:"August",9:"Sept",10:"Oct",11:"Nov",12:"Dec"}
l = list(map(int,input().split()))
for i in l:
    mon.pop(i,None)
print(mon)


# In[ ]:


7. Given a dictionary contains book name as key and price as Value. Write a program to print
the most expensive book.


# In[ ]:


d = {"book":100, "cheap book":50,"expensive book":1000}
lar = 0
for i in d:
    if d[i]>lar:
        lar = d[i]
print(lar)

8. Write a Python program to print the nth Fibonacci number using recursion. Use a dictionary
to store the numbers generated to avoid repetitive computation during recursion. 

# In[ ]:


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

print(recur_fibo(6))


# In[ ]:


9. Given a paragraph, write a python program to find out the word that occurs in the paragraph
maximum number of times. 


# In[ ]:


str = "something something entho entho oru paragraph ayo? arku ariyam"
l = list(str.split(" "))
cha = 0
ans = ""
for i in l:
    if l.count(i) > cha:
        cha = l.count(i)
        ans = i
print(ans)


# In[ ]:


10. Read a text file and find the frequency of occurrence of each word in the file content.
Do pre-processing of the file content. Pre-processing involves, converting text to lower case,
removing punctuations, removing stop-words and tokenising (creating a list of words). Once
a list of words is created, find out the frequency of words and store it in a dictionary. Sort
the dictionary in descending order based on frequency of words.


# In[70]:


str = "hkdshgfv 8 j jgfdgj34987&$9bdkgbk bfkodhjkd kk" 
#prepocessing
str = str.lower()
punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
for i in str:
    if i in punc:
        str = str.replace(i,"")
l = list(str.split(" "))
l2 = []
d = {}
for i in l:
    if i not in l2:
        l2.append(i)
        d[i] = l.count(i)
print(d)


# In[ ]:




