#List: A list is a collection of items in a particular order. 
bicycles = ['trek', 'cannondale', 'redline', 'specialised']
print(bicycles)
#
print(bicycles[0])
print(bicycles[0].title())
print(bicycles[2].upper())

print(bicycles[1] + "  " + bicycles[3])
#
print(bicycles[-1])
print(bicycles[-1]+" "+bicycles[-2]+" "+bicycles[-3]+" "+bicycles[-4])
#
print(bicycles[-4]+" "+bicycles[0])
##print(bicycles[-4]+" "+bicycles[-5])    #ERROR: IndexError: list index out of range