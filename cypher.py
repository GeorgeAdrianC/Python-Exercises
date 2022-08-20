

prompt = input("Do you want to decode(E) or decode (D): ")
message = input("Enter the message: ")
shift = int(input("Enter the shift values: "))

new_message = ""

for ch in message:
    if prompt in "eE":
        if ch >= "a" and ch <= "z":
            position = ord(ch) - ord("a")
            position = (position + shift) % 26
            new_ch = chr(position + ord("a"))
            new_message = new_message + new_ch 
        elif ch >= "A" and ch <= "Z":
            position = ord(ch) - ord("A")
            position = (position + shift) % 26
            new_ch = chr(position + ord("A"))
            new_message = new_message + new_ch 
        else:
            new_message = new_message + ch
    else:
        if ch >= "a" and ch <= "z":
            position = ord(ch) - ord("a")
            position = (position - shift) % 26
            new_ch = chr(position + ord("a"))
            new_message = new_message + new_ch 
        elif ch >= "A" and ch <= "Z":
            position = ord(ch) - ord("A")
            position = (position - shift) % 26
            new_ch = chr(position + ord("A"))
            new_message = new_message + new_ch 
        else:
            new_message = new_message + ch
print(f"The shifted message is {new_message}")