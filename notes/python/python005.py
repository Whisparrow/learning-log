# #Dictionary in python
# #Dictionary are used to store date in key:value pair
# #they are unodered, muttable & don't allow duplicates

# info = {
#     "key": "value",
#     "name": "coco",
#     "age": 35,
#     "adult": True,
#     "marks": 94.4
# }

# null = {}
# print(null)

# null["name"]="coco"
# print(null)


# print (info)
# print (type(info))
# print(info["name"])
# print(info["age"])
# info["name"]="Doraemon"
# info["friend"]="Nobita"
# print(info)

# # Nested Dictionary
# students = {
#     "name":"Souradip Mondal",
#     "subjects":{
#         "PHY":99,
#         "CHEM":99.99,
#         "MATH": 100.99,
#     },
#     "age":12
# }
# print(students)
# print(students["subjects"])
# print(students["subjects"]["PHY"])
# print(type(students))


# ## Dictionary Methods

# # myDict.keys() #returns all keys
# # myDict.values() #returns all values
# # myDict.items() #returns all (key, vall) pairs as tuples
# # myDict.get("key"") #returns the key according to value
# # myDict.update(newDict) #inserts the specified items to the dictionary

# print(info.keys(), students.keys())
# print((list(info.keys())), (list(students.keys())))
# print (len(students))

# k = info.values()
# print(k)
# l = info.items()
# print(l)
# p = students["subjects"]
# print (p)
# m = (students["subjects"]).get("PHY")
# print(m)
# students.update({"city":"kolkata"})
# print(students)


# ## Sets in Python
# ## set is a collection of items of the unordered items. set must be unique & MUTABLE
# set1={1,2,3,"hello","world"}
# print(set1)
# print(type(set1))

# ##Set Method
# #set.add() #add an elements
# #set.remove() #removes an particular item
# #set.clear() #empties the set
# #set.pop() #removes a random value

# set2 = set()
# print(len(set2))
# set2.add(500)
# set2.add("sunflower")
# set2.add(100)
# set2.add("dandolions")
# print(set2)
# print(len(set2))
# #set2.clear()
# set2.pop()
# print(set2)

# #union method and inersection method
# print(set1.union(set2))
# print(set1.intersection(set2))


"""
-----------------------------------------------------------------------------------------------------
##e.x: Store following word meanings in a python dictionary:
#table: "a piece of furniture", "list of facts & figures"
#cat: "a small animal"

dictionary={}
dictionary["table"] = "a piece of furniture", "list of facts & figures"
dictionary["cat"]= "a small animal"
print(dictionary)
-----------------------------------------------------------------------------------------------------


##e.x: You are given a list of subjects for students. Assume one classroom is required for 1 subject.
How many classrooms are needed by all students.
"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"

set = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(len(set))
------------------------------------------------------------------------------------------------------

##e.x: WAP to enter marks of 3 subjects from the user and store them in a dictionary.
# Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

marks={}
marks["math"] = input("Score of Math:")
marks["chem"] = input("Score of Chem:")
marks["phy"] =input("score of Phy: ")
print("Here is score set: ", marks)
------------------------------------------------------------------------------------------------------
"""
# ##e.x:Figure out a way to store 9 & 9.0 as separate values in the set.
# # (You can take help of built-in data types)
# a=set()
# a.add(("int",9))
# a.add(("float",9.0))
# print(a)

# import random
# # coin = random.choice (["heads", "tails"])
# # print (coin)
# dice = random.choice ([1,2,3,4,5,6])
# print (dice)


# from random import choice
# coin = choice (["heads", "tails"])
# print (coin)

# import random
# num = random.randint(1,10)
# print(num)

# cards = [ "jack", "heart", "queen", "king"]
# random.shuffle(cards)
# # print(cards)
# for cards in cards:
#     print(cards)



import statistics
average = statistics.mean([100,90,80,60,56,89,90])
print(f"average is {average}")
