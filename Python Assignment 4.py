#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#question 1


a= int(input("enter your marks="))
if a<0 or a>100:
   print("error")
elif a<25:
    print("Grade is E")
elif 25<=a<45:
    print ("Grade is E")
elif 45<=a<50:
    print("Grade is D")
elif 50<=a<60:
    print ("Grade is C")
elif 60<=a<80:
    print("Grade is B")
elif 80<=a:
    print("Grade is A")


# In[ ]:


# question 2


a = int(input("enter the year="))
if a<0:
    print("error")
elif (a%100==0 and a%400==0):
    print("It can be a leap year")
elif (a%100==0):
    print("It is not be a leap year")
elif (a%4==0):
    print("It is a leap year")
else :
    print("It is not a leap year")


# In[ ]:


# question 3


import random
import math

count=0
while count<10:
    count =count+1
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    guess= int(input("what is" + str(num1) + "x"+ str(num2) +"="))
    ans = int(num1*num2)
    correct = guess == ans
    if (guess== ans):
        print ("correct")
    else:
        print("wrong, the answer is " + str(ans) + ",")


# In[ ]:


# question 4


for i in range (200):
    if i %5 == 2:
        if i%6 == 3:
            if i%7 == 2:
                print(i)

