def skip_elements(elements):
    i=0
    obj_list = []
    obj = list(enumerate(elements))
    for key, value in obj:
        if i % 2 == 0:
            obj_list.append(value)
        i +=1    
    return obj_list
    



print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']