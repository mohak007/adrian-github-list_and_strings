#Write a function that takes a number and returns a list of its digits. So for 2342 it should return [2,3,4,2].
num=2342
def func(num):
    c=str(num)
    list=[]
    for i in range(len(c)):
        list.append(int(c[i]))
    return (list)
a=func(num)
print(a)