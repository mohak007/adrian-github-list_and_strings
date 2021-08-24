#Write three functions that compute the sum of the numbers in a list: using a for-loop, a while-loop and recursion. (Subject to availability of these constructs in your language of choice.)
a=[2,4,5,1,5,2]
count = 0
sum=0
while count< len(a):
    for i in range(0,len(a)):
        sum = sum + a[i]
        print(f"sum is {sum} ")
        count=count+1


