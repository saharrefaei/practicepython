# Write a Python script that extracts the MAC address (b4:6d:83:77:85:f3) from the string.
# `my_str = 'wlo1 Link encap:Ethernet HWaddr b4:6d:83:77:85:f3'
# print(my_str[32::])`
# ___________________________________________________

#Display the following strings literally:
# It displayed: "You've got an error!"
# my_str2="\"You've got an error!\""

# print(my_str2)
# ___________________________________________________
    # Write a Python script to get a string made of the first and the last 2 chars from a given string entered by the user.
# my_str3=input("enter character 1")
# my_str4=input("enter character 2")

# print(my_str3 + my_str4)
# ___________________________________________________

# my_str4=input("enter string")
# char = my_str4[0]
# replace = my_str4.replace(char , '%')
# print(replace)

# ___________________________________________________

# n = int(input('Enter the nth index char to remove:'))
# my_str = input('Enter the string to change:')

# change = my_str.replace(my_str[n] , 'X')
# print(change)

n = 12384756982
n_comma = f'{n:,}'

print(n_comma)
