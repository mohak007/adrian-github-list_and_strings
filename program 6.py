#Write a function that tests whether a string is a palindrome.
str=input("enter the string:")
txt = str[::-1]

if txt==str:
    print("pallidrome found", str)
else :
    print("not found")