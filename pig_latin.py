def pig_latin(text):
    list_ = []
    words = text.split()
    for word in words:
        say =  str(word[1:]) + str(word[0]) + "ay"
        list_.append(say)
    return " ".join(list_)

print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"