"""
name = input("Enter your name:")
print("Welcome", name)
age = input("Enter your age:")
print("okay! you are", age)
age1 = float(input("Enter your age:"))
print(type(age1))
"""

# a = float(input("number 1:"))
# b = float(input("numper 2:"))
# sum = ( a+b )
# print ( sum )
# print ("here is your avarage:", sum/2 ) 
# if a >= b :
#     print (True)
# else:
#     print (False)


# x = float(input(" input the size of a side of a square:"))
# print("cool!", "here is the area:",x**2 )

#_______________________________________________________________________________________________________________________________________________________________
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# x = float(input("whats x?"))
# y = float(input("whats y?"))

# if x < y:
#     print("nop1")
# elif x>y:
#     print("nop2")
# elc;if x==y:
#     print("nop3")

# if  x<y or x>y:
# if x != y:
#     print("x is not equal to y")
# else:
#     print("x is equal to y")


# x = float(input("Your Score:"))
# if x> 100:
#     raise ValueError ("in your dreams bitch")
# elif 90 <= x <= 100:
#     print("grade: A")
# elif 80 <= x < 90:
#     print ("grade: B")
# else:
#     print("grade: F")

# x = float(input("Number:"))
# if  x%2 ==0:
#     print ("EVEN")
# else:
#     print("ODD")

# def main():
#     x = float(input("Number:"))
#     if is_even(x):
#         print("even")
#     else:
#         print("ODD")

# def is_even(n):
#     # return True if n%2 == 0 else False
#     if n % 2 == 0:
#         return True
#     else:
#         return False


# main()

# def is_even(n):
#     if n % 2 == 0:
#         print ("EVEN")
#     else:
#         print("ODD")


# is_even(float(input("Number:")))



name = input("whats your name!?")
match name:
    case"Harry":
        print("Go Home")
    case"Harry"|"Hermione"|"Ron":
        print("Go Home")
    case _:
        print("stay")
