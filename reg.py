# Use of Methacharacter 
import re

txt = "The rain in Spain"
x = re.search("The", txt)   #Search : Returns a Match object if there is a match anywhere in the string and 
# also print the first element #
print(x) 
print()

x2 = re.findall("The", txt)    #findall-It prints the all element #
print(x2)
print()


# []= This symbol is "A set of character" #
#Search:
x3 = re.search("[a-m]", txt)
print(x3)
print()

x4 = re.search("[A-m]", txt)
print(x4)
print()


# Findall:
x3 = re.findall("[a-m]", txt)
print(x3)
print()

x4 = re.findall("[A-m]", txt)
print(x4)
print()






