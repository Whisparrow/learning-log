# ##loops in python
# print("hello")
# count=0
# while count<=5 :
#     print("hellow World")
#     count=count+1

# print(count)

# i=2
# while i<=4 :
#     print("Monkey D. Luffy")
#     i+=1
    
# y=1
# while y<=100 :
#     print(y)
#     y=y+1

# y=1
# while y>0 :
#     print(y)
#     y=y+1          ##infinite loop

"""
##e.x: print number 1 to 100
x=1
while x<=100 :
    print(x)
    x = x + 1
----------------------------------------------------
## e.x: print number 100 to 1
y = 100
while y<=1 :
    print(y)
    y = y-1
----------------------------------------------------
#e.xprint the multiplication table of a number n
n = int(input("enter your no: "))
z = 1
while z <= 10:
    print( n*z)
    z = z + 1
-----------------------------------------------------
## e.x: print the elements of the following list using a loop
#[1,4,9,16,25,36,49,64,81,100]
list1 = [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx < len(list1) :
    print (list1[idx])
    idx = idx + 1

##e.x: Search for a number x in this touple using loop
# (1,4,9,16,25,36,49,64,81,100)

x = input("search:")                       |
tup= (1,4,9,16,25,36,49,64,81,100)         |
i = 0 # initialization                     |    ## wrong
while i < len(tup(i)) :                    |
    if (tup[i]== x):                       |
        print(i)
    else:(print(False))
    i=i+1
__________________________________________________________________
x =
## Lectures' solution:
tup= (1,4,9,16,25,36,49,64,81,100)  
x = 36
i = 0
while i< len(tup):
    if(tup[i] == x):
        print("FUND INDEX AT:", i)
    else:
        print("finding...")
    i += 1
___________________________________________________________________
"""

# # Break & Continue 

# i = 0
# while i <= 5 :
#     print (i)
#     if (i==3):
#         break
#     i = i+1
# i = 0 
# while i <= 5:
#     if(i == 3):
#         i += 1
#         continue
#     print(i)
#     i += 1  # will be skipped


# # FOR LOOPS : LOOP ARE USED FOR SEQUENTIAL TRAVERSAL
# num = [1,2,34,5,67]
# for int in num:
#     print (int)

# f = ("w","f", "o")
# for k in f:
#     print(k)
# else:
#     print("END")

# str ="aster"
# for alph in str:
#     if(alph == "e"):
#         print("e Found")
#         break
#     print(alph)
# else:
#     print(":)")

"""
____________________________________________________________________
e.x: print the elements of the following list using a loop
[1,4,9,16,25,36,49,64,81,100]

list= [1,4,9,16,25,36,49,64,81,100]
for num in list:
    print(num)
__________________________________________________________________

e.x: Search for a number x in this touple using loop:
[1,4,9,16,25,36,49,64,81,100]

Qx = (1,4,9,16,25,36,49,64,81,100)
for Qt in Qx:
    if (Qt == 49):
        print ("49 = Found")
    print(Qt)
_______________________________________________________________________

# Lecture Solution:
nums = (1,4,9,16,25,36,49,64,81,100)
x = 49 

idx = 0
for elements in nums:
    if(elements == x):
        print("number Found at idx:", idx)
    idx = idx + 1
________________________________________________________________________
"""

# #Range()
# for i in range(5):  #range(stop)
#     print(i)

# for f in range(2,7): #range(start, stop)
#     print(f)

# for k in range(2,10,2): # range(start, stop, step)
#     print(k)

# #e.g:
# for j in range(1,100,2): 
#     print(j)

"""
___________________________________________________________________________
e.x: print numbers from 1 to 100
for k in range(1,101):
    print(k)

e.x: print number from 100 to 1
for k in range(100,0,-1):
    print (k)

e.x: Print the multiplication table of number n
n = int(input("enter your number: "))
for f in range(0,11):
    print(f*n)
____________________________________________________________________________
"""
# ##Pass statement
# for i in range(5):
#     pass
# print("shit")

"""
______________________________________________________________________
e.x: WAP to find the sum of first n numbers using while loops
n = int(input("Your End Number:"))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1
print(sum)
________________________________________________________________________
e.x: WAP to find a factorial of first n numbers.

n = int(input())
fac = 1
for k in range(1,n+1):
    fac *= k
print(fac)
________________________________________________________________________
"""
