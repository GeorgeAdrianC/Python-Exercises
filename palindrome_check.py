
word = input("Enter a string ")

is_palindrome = True 

for i in range(0, len(word) //2):
    if word[i] != word[len(word) - i -1]:
        is_palindrome = False
if is_palindrome == True:
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")
