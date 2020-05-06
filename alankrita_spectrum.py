#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Accept 2 int nos from user and return their product and if the product is greater than 1000,then return their sum.
x=int(input("enter the 1st no"))
y=int(input("enter the 2nd no"))
if (x*y)>1000:
    print(x+y)
else:
    print(x*y)


# In[2]:


#Accept n no from user and calculate the sum of all no between 1 and n including n.
def myfunc(n):
    result=0
    i=0
    while i<=n:
          result=result+i
          i+=1
    return result
n=int(input("enter the no:"))
sum=myfunc(n)
print("sum of digits from 1 to n is:",sum)


# In[3]:


#Given a no count the total no of digits in a no
x=int(input("enter a no"))
print(len(str(abs(x))))


# In[4]:


#Accept a string from the user and display only those characters which are present at an even index no.
mystrng=str(input("enter a string"))
for index,ctr in enumerate(mystrng):
    if index%2==0:
        print(index)
        print(ctr)
        print("\n")


# In[6]:


#Write a python program to print all the prime no in given interval and also check is a given input no is prime or not.
def myfunc(n1,n2):
    a=[]
    for i in range(n1,n2+1):
        for j in range(2,i-1):
            if (i%j==0):
                break
        else:
            a.append(i)
    return(a)
num1=int(input("enter the starting point:"))
num2=int(input("enter the ending point:"))
primeno=myfunc(num1,num2)
print("prime nos are:",primeno)
num=int(input("enter a no:"))
if(num==1):
    print("it is a prime no.")
else:
    for i in range(2,num-1):
        if(num%i==0):
            print("it is not a prime no:")
            break
    else:
        print("it is a prime no")


# In[9]:


#Write a python program to print the fibonacci series and also check if a given input no is fibonacci no or not. 
def fibonacci_series(n1,n2,n3):
    a=[n1,n2]
    count=n3
    while(count>2):
        sum=n1+n2
        n1=n2
        n2=sum
        count-=1
        a.append(sum)
    return(a)
num1=int(input("enter the 1st no:"))
num2=int(input("enter the 2nd no:"))
num3=int(input("enter upto how many terms:"))
final_series=fibonacci_series(num1,num2,num3)
print("the final fibonacci series is:",final_series)
import math
def check_perfect_square(x):
    s=int(math.sqrt(x))
    return s*s==x
def check_fibonacci_no(n):
    r1=check_perfect_square(5*n*n+4)
    r2=check_perfect_square(5*n*n-4)
    return r1 or r2
num=int(input("enter the no to be checked:"))
if (check_fibonacci_no(num)==True):
    print(num,"is a fibonnacci no")
else:
    print(num,"is not a fibonacci no")


# In[ ]:




