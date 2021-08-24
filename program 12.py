#Write a function that rotates a list by k elements. For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2]. Try solving this without creating a copy of the list. How many swap or move operations do you need?
list=[1,2,3,4,5,6]
t=int(input("enter the number"))
if t==0:
        print(f"list will be rotated by {t} times , means list remains same " )
for i in range(t):
        temp=list[0]
        list.pop(0)
        list.append(temp)
print(list)

