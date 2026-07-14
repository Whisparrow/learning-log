print("Hello World!")
# print("Welcome to Python programming.")
# print("Hello World!", "Welcome to Python programming.")
# print(230)
# print(3.14)
# print(230 + 3.14)
# a=2.78
# b=3.14
# print( 2*(a+b) )

# name="Aster"
# age=30
# print("Name:",name)
# print("Age:",age)
# print(type(name))
# print(type(age))
# print(type(a))
# print(type("230"))
# print("230")
# print("230+340")
# print(230+340)
# print(type("230"))
# print(type(230))
# witness= False
# print(witness)
# print(type(witness))
# witness_number= None
# print(witness_number)
# print(type(witness_number))

# ##types of operators
# #arithmatic operators
# z = 25
# cz = 5
# you = (z+cz)
# print(you)
# print(z+cz)
# print(z-cz)
# print(z*cz)
# print(z/cz)
# print(z%cz)
# print(z**cz)

# ##Relational / comparison operators
# print(z==cz) #false
# print(z!=cz) #true
# print(z>cz) #true
# print(z<cz)  #false
# print(z>=cz) #true
# print(z<=cz) #false

# #assignment operators
# num = 10
# num += 10
# print ("num :", num)
# num -= 5
# print (num)
# num *=2
# print (num)
# num **=2
# print (num)


# ##Logical operator @and, or, not
# print (not False) #True
# print (not True) #False
# g = 85
# h = 89.1
# print (not (g<h)) #Flase
# val1 = True
# val2 = True
# print ("and operator :", val1 and val2)
# print ("or operator :", val1 or val2)
# val3 = True
# val4 = False
# print ("and operator :", val3 and val4)
# print ("or operator :", val3 or val4)
# val5 = False
# val6 = False
# print ("and operator :", val5 and val6)
# print ("or operator :", val5 or val6)

# print("and operator :", (g==h) and (g<h))
# print("or operator :", (g==h) or (g<h))

# sum = g + h
# print(sum)
# print(type(sum))


# ##type casting
# # int(value)
# # float(value)

# ##Practice Question
# x = 90
# y = 80
# if x >= y:
# 	print(True)
# else:
# 	print(False)
# ___________________________________________________________________________________________________________________
# ___________________________________________________________________________________________________________________

# Ask user for their name
# name = input("whats ur name?").strip().title()

# Remove whitespace from str
# name = name.strip()

# Capitalize name
# name = name.capitalize()
# name = name.title()

#remove whitespace from str and capitalize usr's name
# name = name.strip().title()

#Split user's name into first name and last name
# first, last = name.split(" ")

#say hello to user
# print("hello," + name )
# print("hello,", name)
# print(f"Hello,{first}")
# print("hello,")
# print(name)
# print("hello,", end="" )
# print(name)


# x = float(input("what's x?"))
# y = float(input("what's y?"))
# z = round(x+y)
# z =round(x/y)
# print(f"{z:,}")


# def hello(to):
#     print("hellow,", to)

# name = input("whats your name !?")
# hello(name)


def main():
    x = int(input("what's x?"))
    print ("x squared is", square(x))

def square(n):
    return (n*n)

main()
