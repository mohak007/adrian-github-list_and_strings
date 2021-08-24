#Write a function that merges two sorted lists into a new sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6]. You can do this quicker than concatenating them followed by a sort.
lista=[1,4,6]
listb=[2,3,5]
lista.sort()
listb.sort()
listc=lista +listb
listc.sort()
print(listc)