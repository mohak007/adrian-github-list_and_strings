#Write a function that computes the running total of a list.
a=[10,2,11,44,2,41,55]
sum=0
for i in range(0,len(a)):
    sum=sum+a[i]
print(f"sum is {sum} ")