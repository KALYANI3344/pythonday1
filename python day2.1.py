
"""{logical operators are used to perform logical operators they are logical and ,or,not"""

a=13
b=45
c= a>=34 and b<=50
print(c)


d=67
e=89
f=d!=67 or e==89
print(f)

a=20
print(not(a))

"""
bitwise operators are used to petrform binary operations they are:
bitwise and(&):if both the bit are "1"it returns 1
bitwise or(|):if one the bit is "1" it returns 1
bitwise xor(^):if one of the bit is "1"returns 1
and if both the bits are "1" it returns "0"
"""
a = 5
b = 9
c =a&b
print(c)


d = 15
e = 13
f =d|e
print(f)

g = 12
h = 14
i =g^h
print(i)

"""membership operators are used to check the values in a sequence
and returns the boolean values 
they o[perators are "in","not in"       
"""

x = ["apple","banana"]
print("apple" in x)
print("pp" not in x)
print("banana" not in x)
print("dragon" in x)


"""
identity operators are used to compare the values
and return the boolean values..
the operators are "is","is not"
"""
x = [1,2,3]
y=[4,5,6]
z=x
print(x is y)#f
print(x is z)#t
print(y is z)#f
print(x is not y)#t
print(y is not z)#t

 

