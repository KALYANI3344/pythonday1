#Number--which tells about the number datatypes divided into three types
"""
integer--which holds all the positive and negative whole numbers i.e 0 to n and o to -n 
integer can be represented as int()
"""
a=123
print(a)
print(type(a))
print(id(a))


a1=-90
print(a1)
print(type(a1))
print(id(a1))

"""
Float--which holds all the decimal or fractional which i.e 0 to n.n and -n.n
it can be represented as float()
"""

b=89.456
print(b)
print(type(b))
print(id(b))

b1=-78.67
print(b1)
print(type(b1))
print(id(b1)) 

"""Complex--which holds all the complex numbers i.e a+bj where a and b are real numbers and j is imaginary number
it can be represented as complex() 
"""
c=78+67j
print(c)
print(type(c))
print(id(c))

c1=-78+67j
print(c1)
print(type(c1))
print(id(c1))
"""
#sequence datatypes are divided into 3 types
1.strinG #" "HELLO"
2.list   #"[]"
3.tuple  #()
"""

"""
string ---it is a collection of \group of characters
it can be enclose using the single quotes or double quotes
"""
a="ists"
print(a)
print(type(a))
print(id(a))

"""
list---it is acollection of items \values\elements
syntax:list name=[val1,val2,.....,valn]
in order to acess the element individually we use indexing
indexing always starts with "0"and ends with "1"
syntax:to access the element
"""
mylist=[23,56,56+76j ,"Hello"]
print(mylist)
print(type(mylist))
print(id(mylist))
print(mylist[1])

"""
tuple---it is acollection of items\values\elements
syntax:tuplename=(val1,val2,.....,valn)
"""
mytuple=(12,23.67,"hi",[1,2,3])
print(mytuple)
print(type(mytuple))
print(id(mytuple))

"""
giving a list within list is called sublist
giving a tuple within tuple is called subtuple
"""
"""#boolean datatype 
boolean means check the condition they are divided in two ways
1.True
2.False
"""

a= True 
print(a)
print(type(a))

b=False
print(b)
print(type(b))

"""
set---it is a collection of value\items\element
syntax:setname={val1,val2,.....,valn}
a set can accept the list...
"""

myset={12,23,34,56+78j,"HI",[1,2,3],(45,"Hello"),(12,34,56),True}
print(myset)
print(type(myset))

"""
dictionary:it is acollection of key value pairs
syntax:dictionary name={key1:val1,key2:val2,.....,key n:val n}
"""
mydict={1:"branch":"EcE",location:"RJY"}
print(mydict)
print(type(mydict))

























