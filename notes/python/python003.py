# # str is data type
# str1 = "good"
# print (str1)
# srt2 = "tos is a stiong. hshughg"
# print (srt2)
# str3 = "this is a string.\nwe are learning python"
# print (str3)
# sty4 = "this is a string.\twe are learning python"
# print (sty4)
# print (str1 + " " + srt2)
# print (len(str1))
# print (len(srt2))
# ch = srt2[4]
# print (ch)

# #slicing index
# ch2 = str1[1:3]
# ch3 = str1[1:]
# ch4 = str1[:2]
# ch5 = str1[-3:-1]
# print (ch2, ch3, ch4, ch5)

# change1 = (str1.endswith("od"))
# change2 = (str1.endswith("ol"))
# change3 = (str1.capitalize())
# change4 = (str1.replace("g", "c").replace("d", "l"))
# change5 = (str1.find("o"))
# change6 = (str3.count("i"))
# print (change1, change2, change3, change4, change5, change6 )

"""
e.x: Write a program to input user's name & print its length.

a = input("enter your name: ")
print (len(a))

"""

"""
e.x: Write a program to find the occurence of '$' in a string

b = "I wanna have billion $"
print (b.count("$"))

"""

# # conditional statement
# light = "shit"

# if(light == "red"):
#     print("STOP")
# elif(light == "orange"):
#     print("WAIT")
# elif(light == "green"):
#     print("go")
# else:
#     print ("ERROR")

# age = 24
# if(age>= 18):
#     print ("ELIGIBLE")
# else:
#     print("NOT ELIGIBLE")

"""
--------------------------------------
e.x: grade students based on marks
marks >= 90, grade = "A"
90 > marks >= 80, grade = "B"
80 > marks >= 70, grade = "C"
marks < 70 , grade = "D"
--------------------------------------
marks = 50
if(marks >= 90):
    print("Grade: A")
elif(90 > marks >= 80):
    print("Grade: B")
elif(80 > marks >= 70):
    print("Grade: C")
elif(marks < 70):
    print("Grade: D")

______________________________________________________

@claude
try:
    marks = int(input("Marks: "))
    if(marks >= -100 and marks <= 100):
        if(marks >= 90 and marks <= 100):
            print("Grade: A")
        elif(90 > marks and marks >= 80):
            print("Grade: B")
        elif(80 > marks and marks >= 70):
            print("Grade: C")
        else:
            print("Grade: D")
    else:
        print("ERROR")
except ValueError:
    print("Input numeric value only")
_____________________________________________________________

marks = int(input("Marks:" ))
try:
    marks = int(marks)
except ValueError:
    print("Input numaric value only")

if( marks >= -100 and marks <= 100):

if(marks >= 90 and marks <= 100):
    print("Grade: A")
elif(90 > marks and marks >= 80):
    print("Grade: B")
elif(80 > marks and marks >= 70):
    print("Grade: C")
else:
    print("Grade: D")
else:
    print("ERROR")

_________________________________________________________________________
"""

# ##Nesting
# k = 23
# if( k >= 18 ):
#     if( k >= 80 ):
#         print("nope")
#     print("OK")
# else:
#     print("no")

"""
_______________________________________________________________________

#e.x: WAP to check if the entered number by user is odd or even
a = int(input("Your Number:"))
if ( a % 2 == 0 ):
    print("even")
else:
    print("odd")

-------------------------------------------------------------------------

# WAP to find the gratest of 3 numbers enterd by the user.
x = int(input("num1:"))
y = int(input("num2:"))
z = int(input("num3:"))
if ( x > y and x > z ):
    print(x)
if (y > x and y > z ):
    print(y)
if (z > y and z > x):
    print(z)

_____________________________________________________________________________

#e.x: WAP to check if the entered number is a multiply of 7
w = int(input("Your Number: "))
if( w % 7 == 0 ):
    print("multiply of 7")
else:
    print("not multiply of 7")

_____________________________________________________________________________

"""
# __________________________________________________________________________________________________________________________________________________________________________________________________
# __________________________________________________________________________________________________________________________________________________________________________________________________



# i=0
# while i != 3:
#     print("meow")
#     i = i+1

# i = 3
# while i != 0:
#     print("meow")
#     i = i - 1


# for _ in range(10000000000000000000000000000000000000000000000000000000000000000000):
#     print("meow")


# print("meow"*3)
# print("meow\n"*3)
# print("meow\n"*3, end="")


# while True:
#     n = int(input("whats n!?"))
#     if n < 0:
#        continue
#     else:
#        break



# while True:
#     n = int(input("whats n!?"))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")



# def meow(n):
#     for _ in range(n):
#         print("meow")

# meow(10)
# meow(5000)


# def meow(n):
#     for _ in range(n):
#         print("meow")


# meow(90)

# def get_number():
#     while True:
#         n = int(input("how many times:"))
#         if n > 0:
#             return n

# def main():
#     number = get_number()
#     meow(number)


# def meow(n):
#     for _ in range(n):
#         print("meow")


# main()

# list = ["h","h1","r"]
# for x in list:
#     print(x)

# {} we use {} to create dictionary

# students = {
#     "H":"G",
#     "H1":"G",
#     "R":"G",
# }
# print(students)

# students = [
#     {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
#     {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
#     {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell terrier"},
#     {"name": "Draco", "house": "Slytherin", "patronus": None}
# ]

# for student in students:
#     print(students)
