import re

pattern = re.compile("[A-Z][a-z]+")

def findSequence(strInp):
    return re.findall(pattern, strInp)

print(findSequence(input("String = ")))
