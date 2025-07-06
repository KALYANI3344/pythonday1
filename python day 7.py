#list predefind methods
"""
1.Append/extend
2.mutabilin/continue
3.indexing/remove/pop/insert
"""
"""
#slicing: string is used to retrive the elements from
one particular range to another particular range.s^3(start:stop:skip)
"""

mylist=[1,2,3,4,5,6,7,8,9]
print(mylist)
print(mylist[0:6:2])

mylist=[2,5,6,7,8,9,10]
print(mylist[0:7:3])

mylist=[45,46,78,90,56,34,78,90,34,65,89]
print(mylist[0:8:4])

mulist=["hello",12,34,56,89,90,456+5j,4555,789]
print(mylist[2:6:2])

"""
list is a collection/group of items/values/elements
they can be enclosed in square brackets[]seperated by commas(,)
list method:append/extend/count/mutability/index/remove/pop/insert
syntax:listname.methodname()
"""
#append:this method is used to add the elements at the end 
list=["Edinburgh","scotland","london"]
print(list)
print(list.append("bhrihingam"))
print(list)

#extend:this method is used to add the elements at the end
#as a sublist
list.extend(["paris","malta","aus"])
print(list)

#count:this method is used to count the number of repeated element in a list
flower=["rose","lilly","lotus","rose","lilly","lotus"]
flower.count("rose")
print(flower)




