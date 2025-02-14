import re

txt="Hello Python Module"

# # \A-Returns a match if the specified characters are at the beginning of the string
x=re.search("\AHello",txt)
print(x)
print()

x2=re.findall("\AHello",txt)
print(x2)


# \b- Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")  

txt1="Hello Python Module "
x3=re.search(r"\bHello",txt1)
print(x3)
print()

x5= re.search(r"Hello\b", txt1)
print(x5)
print()

x4=re.findall(r"\bHello",txt1)
print(x4)
print()

x6= re.findall(r"Hello\b", txt1)
print(x6)
print()


# ^-Starting symbol and $-Ends Symbol  and [.]= Any character expect ne line

txt = "hello planet menu hello"

x = re.search("he..o", txt)
print(x)

x = re.findall("^he..o", txt)
print(x)

x = re.search("lo$", txt)
print(x)

x = re.findall("lo$", txt)
print(x)


# * :Zero  or more occurence  and  + : Search one  or more  (any) characters:
x = re.search("he.*o", txt)
print(x)
print()

x = re.search("pl...*t", txt)
print(x)
print()

x = re.search("he.+o", txt)
print(x)
print()

x = re.findall("he.*o", txt)
print(x)
print()

x = re.findall("pl...*t", txt)
print(x)
print()

x = re.findall("he.+o", txt)
print(x)
print()



# # ? : Zero or one occurrences
text="Hello Python Regular Hello"
x=re.search("He..?o",text)
print(x)
print()

text="Hello Python Regular"
x=re.findall("He..?o",text)
print(x)
print()


txt = "hello planet"

# {} : Exactly the specified number of occurrences
x = re.findall("he.{2}o", txt)
print(x)
print()

x1=re.findall("pl.{3}t",txt)
print(x1)
print()

x1=re.search("pl.{3}t",txt)
print(x1)
print()

# | Either or 	"falls|stays" :- Check if the string contains either "falls" or "stays":	

text2="THe rain falls stays "
x2=re.search("falls|stays",text2)
print(x2)

text3="The python"

x3=re.search("falls|stays",text3)
print(x3)
print()

# x3=re.findall("falls|stays",text2)
# print(x3)

x4=re.findall("falls|stays",text3)
print(x4)



