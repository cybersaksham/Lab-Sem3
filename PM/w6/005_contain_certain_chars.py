import re

def checkValid(strInp, pattern):
    match_re = re.compile("^[" + pattern + "]+$")
    return re.search(match_re, strInp)


print("Valid String" if checkValid(input("Enter string = "), input("Enter pattern = ")) else "Invalid String")
