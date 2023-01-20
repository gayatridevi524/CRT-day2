num=input("enter the number:")
a=list(num) # ['1', '2', '3', '4', '5']
print(a)
b=list(map(int,a)) # convert each element to integer in a list
print(b)
i=0
c=[]
for i in b:
    c.append(i**2)
print(c)
