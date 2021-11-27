def palindrome(string):
    reverse_string=string[::-1]
    if string==reverse_string:
        print("given string is palindrome")
    else:
        print("given string is not palindrome")
palindrome("madam")
palindrome("pune")