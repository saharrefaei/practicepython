#     Consider a list of words(strings). Write a Python script that generates a list of tuples where the first element of the tuple is the word in the list and the second element is its length.

#     Use list comprehension if possible.

# Sample List: words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']

# Expected Result: [('Python', 6), ('Java', 4), ('C++', 3), ('Golang', 6), ('Solidity', 8), ('Bash', 4)]

# words = ['Python', 'Java', 'C++', 'Golang', 'Solidity', 'Bash']
# lisch =[(i , len(i)) for i in words]
# print(lisch)

# ______________________________________________

# Write a Python program that accepts as input a sequence of words separated by one or more whitespaces and prints out the same words with the letters in reversed order. Do not use list comprehension.
# string = "I love cat and dogs"

# reversedString = list() 
# reversedString = string.split(" ")
# rev = list()
# for items in reversedString :
#     rev =' '.join(items[::-1])
#     print(rev)


# ______________________________________________

# Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

# words = list()
# words = input("enter the color")
# wordsList = list()
# wordsList = words.split("-")
# print(sorted(wordsList))

# ______________________________________________

# Write a program that prompts the user for a long string containing multiple words separated by whitespaces and prints back the same string with the words in backward order.

# str = "my name is laxmi"
# revresestr=str.split(" ")
# print(revresestr[::-1])

# ______________________________________________

# Write a Python script that finds all numbers that are divisible by 7 but are not a multiple of 5, between 1500 and 3200 (both included).
# numbers = input("enter").split("-")
# num=list()
# for i in numbers :
#     intnum = int(i)
#     if intnum % 7 == 0 and intnum % 5 != 0 :
#        num.append(intnum)

# print(num)

# ______________________________________________

    # Write a Python script that validates an email address by writing "Valid email!" or "Invalid email!".

    # If the email is not valid the script should display why it's not valid.

    # We consider a valid email address if:

    #     it has at least 6 characters but no more than 16.

    #     it contains both . and @

    #     it does not contain any of the following characters:'[]{}()$*'
# email = list()
# email = input("enter email addres : ")
# invalidChar = ["[" , ']' , "*"]
# emailLength = len(email)

# for char1 in email:
#     for invalid1 in invalidChar:
#         if char1 == invalid1 :
#             print("Invalid character found:", char1)
#             break
                 
#         if emailLength < 6  or emailLength > 16 :
#             print(" the length of email is incorrect")
#             break
        
#         else : 
#             print("valid email")
#             break
     
            
     # ______________________________________________
# Consider the following 2 Lists: names = ["Dan", "John", "Diana"] and phones = [11111, 2222, 3333].

# Create a set that contains the elements of the 2 lists in pairs.
   
# names = ["Dan", "John", "Diana"] 
# phones = [11111, 2222, 3333]

# newchar =dict(zip(names,phones))
# print(newchar)

     # ______________________________________________
# Consider this dictionary. Print a sorted view of the dictionary by the third field of its values, in reverse order.

# employees = {'John': ('London', 4000, 28), 'Maria': ('Zagreb', 3800, 40), 'Diana': ('NYC', 3500, 31)}
# view = sorted(employees.items() , key=lambda x:x[1] , reverse=True)
# print(view)

     # ______________________________________________


# def tree(height):
#     firstline = height * 2 - 1
#     while firstline > 0:
#         print("*" * firstline)
#         firstline -= 2

# tree(5)


# ------------------------------------------

import sys

stdout = sys.stdout

with open ("C:\\movie\\python\\practice\\pythonP\\contries.cs" , 'a') as X :
     sys.stdout = X
     print("the result")
     stdout = sys.stdout