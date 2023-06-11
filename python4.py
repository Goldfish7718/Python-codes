def take_input():
    string = input("Enter String to check for palindrome\n")
    return string

def test_palindrome(string):
    reversed_str = ''.join(reversed(string))
    return f"{string} is a palindrome" if string.lower() == reversed_str.lower() else f"{string} is not a palindrome"
    
str = take_input()
result = test_palindrome(str)

print(result)

