def is_palindrome(input_string):
    new_string = ""
    reverse_string = ""
    for letter in input_string[::-1]:
        reverse_string += letter.lower().strip()
    for letter in input_string:
        new_string += letter.lower().strip()
    if new_string == reverse_string:
        return True
    return False
        


    


print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True