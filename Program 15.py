#Write functions that add, subtract, and multiply two numbers in their digit-list representation (and return a new digit list). If you’re ambitious you can implement Karatsuba multiplication. Try different bases. What is the best base if you care about speed? If you couldn’t completely solve the prime number exercise above due to the lack of large numbers in your language, you can now use your own library for this task.
list=[1,2]
def add(list):
    for i in range(10):
        c=list[i]+list[i+1]
        list.append(c)
    return list

def subtract(sublist):
    for i in range(10):
        c=sublist[i+1] - sublist[i]

        sublist.append(c)
    return sublist
def multiply(mullist):
    for i in range(len(mullist)):
        c=mullist[i] * mullist[i+1]
        mullist.append(c)
    return mullist
a=add(list)
print(a)
sublist = [2, 3]

b=subtract(sublist)

print(b)
mullist=[1,3]
d=multiply(mullist)
print(d)