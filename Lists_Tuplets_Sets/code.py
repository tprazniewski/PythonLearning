# list keep the order of elements
l = ["Tom", "Marcus", "Bartek"] 
# tupple can't remove and ann elements to a tupple. Keep the order of elements
t = ("Tom", "Marcus", "Bartek")
# set, can't have two indentical elements. Order is not waranteed
s = {"Tom", "Marcus", "Bartek"}


l.remove("Tom")
print(l)

s.add("Smith")
print(s)