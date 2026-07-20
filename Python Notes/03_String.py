string = "Word" #A string is a data type which is surrounded by Quotation marks 

print(string[1:2]) #You can slice a string [start:end]

print(f"A string conatins a {string}") #You can format variables into a string by putting "f" before the first quotation and using curly brackets with the variable

# You change the case of a string 
print(string.upper()) # .upper() makes it fully Upper case

print(string.lower()) # .lower() makes it fully lower case

print(string.title()) # .title() makes the first letters of a word upper case

print(string.capitalize())# .capitalize() makes the first letter of a string upper case

print(string.casefold())# .casefold()

print(string.swapcase())# .swapcase() switches the case upper if lower and vice versa
