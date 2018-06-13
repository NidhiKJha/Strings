# ask user for name

name = input(["what is your name"])

#ask user for age
age = input(["what is your age"])


#ask user for city
city= input(["where do u live "])

#ask user for what they enjoy
love = input(["What do u love doing"])

#create output text
string = "Your name is {} ,You're {} years old. you live in {} and you love {}. "
output = string.format(name,age,city,love)

#print output to screen
print(output)
