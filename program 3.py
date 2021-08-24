#Write a function that checks whether an element occurs in a list.

a=[10,2,11,44,2,41,55]

num=int(input("Enter number to be searched:"))
if num in a:
    print("num is found ", num)
else :
    print("not found")