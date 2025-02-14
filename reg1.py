import re
# txt = "That will be 59 dollars"
txt = "That will be $%^ dollars"  

#Find all digit characters:

x = re.findall("\d", txt) #[]-Empty list return 
print(x)   #[]-Empty list return # $%^-It is not allowd so thats Return None

x1 = re.search("\d", txt)
print(x1) #$%^-It is not allowd so thats Return None#