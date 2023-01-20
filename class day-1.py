a=5
print(type(a))
b="hello"
print(type(b))
c=10.0
print(type(c))
#list mutable(can be modified)
lis=[1,3.4,"hello",[1,2,3]]
print(type(lis))
lis2=[1]
print(type(lis2))
#tuple immutable(cannot be modified)
abc=(1,2,3,4,5)
print(type(abc))
#tuple with single element
xyz=(1,)
print(type(xyz))
"""tuple with single element like (1) will be treated as integer"""
#set
"""set-it doesn't allow duplicate elements and can be printed in any random order"""
s={'a','b','c','a','b','c'}
print(s)
print(1 and 0)
print(1 or 1)
print(23 and 7)
print(74 and 31)
print(type(bin(74)))
"""a=int(input("enter a number:"))
b=int(input("enter b number:"))
sum_of_numbers= a+b
print(sum_of_numbers)
sub_of_numbers= a-b
print(sub_of_numbers)
mul_of_numbers= a*b
print(mul_of_numbers)
float_division= a/b
print(float_division)
integer_division= a//b
print(integer_division)
modulo_of_numbers = a%b
print(modulo_of_numbers)
print(a>b)
print(a<b)"""
print(1 & 7) # bitwise and
print(1 | 7) # bitwise or
# membership operator--> in,not in returns True or False
l=[1,2,3,4,5,6,78,7]
print(1 in l)
print(8 not in l)
print(76 in l)
# identity operator-->is,is not
a=10.0
print(a is None) # None means Null
print(a is not None)
# Ternary operator
# (condition) ? True part : False part
list_1=[1,2,3,[4,5,6]]
list_1.append("hello")
print(list_1)
list_1.pop(0) # removes the element with specified index in braces
list_1.pop() # removes the last element
list_1.remove(3)# removes the specific value defined with in braces
list_1.insert(0,10) # inserts element at particular index
print(list_1)
list_2=[1,10.0,["hello",2,'A']]
print(list_2)
list_2.extend(list_1)# adds all the elements of list 1 to list 2
print(list_2)
print(list_1)
res=list_2.count(10) # counts how many times the element is there in list
print(res)
list_1=list_2.copy()
print(list_1)
print(list_2)
list_new=list_2
list_new[1]=100
print(list_new)
list_1.reverse()
print(list_1)
my_list=[10,4,1,3.8]
my_list.sort()
print(my_list)
my_list.sort(reverse=True)
print(my_list)
b=sorted(my_list)
print("my_list is",my_list)
print("b is",b)
# type conversion
a=int('2') # string to int explicit conversion
b=1
c=a+b
print(c)
p="mr X is " # int to string conversion
q=str(36)
r=" years old"
print(p+q+r)
a=list('12345') # ['1', '2', '3', '4', '5']
print(a)
b=list(map(int,a)) # convert each element to integer in a list
print(b)
