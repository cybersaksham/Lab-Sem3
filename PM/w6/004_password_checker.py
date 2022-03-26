import re

reg = "^.*(?=.{6,20})(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[?@#$%^&+=]).*$"
match_reg = re.compile(reg)

def checkPassword(passwd):
    return re.search(match_reg, passwd)


print("Valid Password" if checkPassword(input("Enter password = ")) else "Invalid Password")
