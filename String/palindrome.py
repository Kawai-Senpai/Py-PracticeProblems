# Question: Check if a given string is a palindrome, ignoring case and spaces.

def normalize(str):
    return str.lower().replace(' ','')

def is_palindrome_manual(str):
    str = normalize(str)

    new_str = ""
    size = len(str)
    for i in range(size-1,-1,-1):
        new_str = new_str + str[i]
    
    return new_str == str
    
def is_palindrome(str):
    str = normalize(str)
    return str == str[::-1]
    
# Example usage
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("Hello"))  # False