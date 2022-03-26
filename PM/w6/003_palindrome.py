def checkPalindrome(s):
    n = len(s)
    if n <= 1:
        return True
    elif n == 2:
        return s[0] == s[1]
    return (s[0] == s[-1]) and checkPalindrome(s[1:n - 1])


print(checkPalindrome(input("Enter String = ")))
