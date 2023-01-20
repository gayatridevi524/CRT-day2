# set operations
"""s1={1,2,7,4}
s2={5,6,7,8}
res1=s1.intersection(s2)
print(res1)
res2=s1.union(s2)
print(res2)
res3=s1.difference(s2)
print(res3)
res4=s2.difference(s1)
print(res4)
# conditional statements
num=int(input("enter the number:"))
if num%2==0:
    print("given number is even")
else:
    print("given number is odd")
num=int(input("enter the number:"))
if num==0:
    print("invalid")
elif num<=7:
    if num==1:
        print("monday")
    if num==2:
        print("tuesday")
    if num==3:
        print("wednesday")
    if num==4:
        print("thursday")
    if num==5:
        print("friday")
    if num==6:
        print("saturday")
    if num==7:
        print("sunday")
else:
    print("funday")
num=int(input("enter the number:"))
if (num>0 and num<20):
    if(num%2==0):
        print("weird number")
    else:
        print("normal number")
elif(num>=20 and num<30):
    print("normal number")
elif(num>=30):
    if(num%2!=0):
        print("normal number")
    else:
        print("weird number")
else:
    print("invalid number")
dic={
    "roll_number1":{"name":"student1","class":3},
    "roll_number2":{"name":"student2","class":3},
    "roll_number3":{"name":"student3","class":3}
}
print(dic['roll_number1'])"""
d={}
d.update({'key1':'value1'})
d.update({'key1':'value2'})
d.update({2:'value3'})
print(d)
print(d[2])


