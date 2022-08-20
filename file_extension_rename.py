filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = []
old=".hpp"
new=".h"
for element in filenames:
    if element.endswith(old):
        i = len(old)
        new_element = element[:-i] + new
        newfilenames.append(new_element)
    else:
        newfilenames.append(element)
        

print(newfilenames) 
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]