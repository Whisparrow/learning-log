# ## List & Tuples
# marks = [94.6, 85, 65, 30.5, 100]
# print (marks)
# print (type(marks))
# print (marks[0])
# print (marks[4])
# print (len(marks))

# # A List can contain multiple types of data
# student1 = ["Jon Doe", 17, 100, "Neverland"]
# print (student1)

# # we can change value of the list as well here is an example

# print (student1[0])
# student1[0] = "jne Doe"
# print (student1)


# # list slicing : list[starting_indx : ending_index]
# print (marks[ 1:4 ])
# print (marks[-5:-1])


"""
list = [2, 1, 3]

list.append(4) #adds one element at the end [2, 1, 3, 4]

list.sort() #sorts in ascending order [1, 2, 3]

list.sort(reverse=True) #sorts in descending order [3, 2, 1]

list.reverse() #reverses list [3, 1, 2]

list.insert(idx, el) #insert element at index

list.pop(idx) #removes element at idx

"""
# marks.append(93)
# print (marks)

# marks.sort(reverse=True)
# # marks.sort()
# print (marks)

# # Its also possible to sort a list containing strings. How !? A - Z wise
# fruits = ["melon", "cherry", "apple", "tomato"]
# fruits.append("mango")
# fruits.sort()
# print (fruits)

# Alph = [ "e", "h", "g", "o", "a", "x", "z" ]
# # Alph.sort(reverse=True)
# Alph.reverse()
# print(Alph)


# Alph.insert(5, "q")
# print(Alph)


# Alph.pop(6)
# print (Alph)


### Touples In Python
# A built-in data type that lets us create immutable sequence of value

# tup = (2, 1, 3, 5, 9, 1)
# print(tup)
# print(len(tup))
# print(type(tup))
# print((tup[0]), (tup[1]))

# stdnt = ("Jon Doe", 17, 100, "Neverland")
# print ((stdnt[0:3]), (tup[1:3]))

"""
Tuple Methods

tup = (2, 1, 3, 1)

tup.index(el) #returns index of first occurrence tup.index(1) is 1
tup.count(el) #counts total occurrences tup.count(1) is 2

"""

# print(tup.index(3))
# print(tup.count(1))

"""
___________________________________________________________________________________

## e.x: WAP to ask the user to enter names of their 3 fav movies & store them in a list
a = input("mov1: ")
b = input("mov2: ")
c = input("mov3: ")
fav = [ a,b,c ]
print ("This is the list: ", fav )

OR

movies = []
mov = input("enter 1st movie: ")
movies.append (mov)
mov = input("enter 2nd movie: ")
movies.append (mov)
mov = input("enter 3rd movie: ")
movies.append (mov)

print ("This is the list: ", movies )

________________________________________________________________________________________

## e.x : WAP to check if a list contain a palindrome of elements
list = [1, 2, 1]
listii = [1,6,5]
list1 = list.copy()
list2 = listii.copy()
list.reverse()
listii.reverse()
print (list)
print (list1)
print(listii)
print(list2)

if (list == list1):
    print(True, "palindrome")
else:
    print(False, " not palindrome")

if (listii == list2):
    print(True, "palindrome")
else:
    print(False, " not palindrome")
__________________________________________________________________________________________


## e.x: WAP to count the number of students with the "A" grade in the follwing:
["C", "D", "A", "А", "В", "B", "A"] & store the values in a list & sort them from "A" to "D"

Grade = ["C", "D", "A", "A", "B", "B", "A"]
print (Grade.count("A"))
Grade.sort()
print(Grade)

______________________________________________________________________________________________
"""

#__________________________________________________________________________________________________________________________________________________________________________
#__________________________________________________________________________________________________________________________________________________________________________



# try:
#     x = int(input("whats x? "))
#     print (f"x is {x}")
# except ValueError:
#     print("x is not an integer")


# try:
#     x = int(input("whats x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():
#     while True:
#         try:
#             return int(input("whats x? "))
#         except ValueError:
#             print("x is not an integer")



# def get_int():
#     while True:
#         try:
#             x = int(input("whats x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             break
#     return x

# def get_int():
#     while True:
#         try:
#             x = int(input("whats x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return x

# while True:
#     try:
#         x = int(input("whats x? "))
#         break
#     except ValueError:
#         print("x is not an integer")

# print(f"x is {x}")

# main()


def main():
    x = get_int("Whats x? : ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("x is not an integer")

main()
