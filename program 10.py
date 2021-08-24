#Write a function that combines two lists by alternatingly taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].
lista=["a","b","c"]
listb=[1,2,3]
listc=[]
for i in range (0,len(lista)):
    listc.append(lista[i])
    listc.append(listb[i])
    print(listc)
    
