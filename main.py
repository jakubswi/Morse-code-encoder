morse_dictionary={
    "A":"▄ ▄▄▄",
    "B":"▄▄▄ ▄ ▄ ▄",
    "C":"▄▄▄ ▄ ▄▄▄ ▄",
    "D":"▄▄▄ ▄ ▄",
    "E":"▄",
    "F":"▄ ▄ ▄▄▄ ▄",
    "G":"▄▄▄ ▄▄▄ ▄",
    "H":"▄ ▄ ▄ ▄",
    "I":"▄ ▄",
    "J":"▄ ▄▄▄ ▄▄▄ ▄▄▄",
    "K":"▄▄▄ ▄ ▄▄▄",
    "L":"▄ ▄▄▄ ▄ ▄",
    "M":"▄▄▄ ▄▄▄",
    "N":"▄▄▄ ▄",
    "O":"▄▄▄ ▄▄▄ ▄▄▄",
    "P":"▄ ▄▄▄ ▄▄▄ ▄",
    "Q":"▄▄▄ ▄▄▄ ▄ ▄▄▄",
    "R":"▄ ▄▄▄ ▄",
    "S":"▄ ▄ ▄",
    "T":"▄▄▄",
    "U":"▄ ▄ ▄▄▄",
    "V":"▄ ▄ ▄ ▄▄▄",
    "W":"▄ ▄▄▄ ▄▄▄",
    "X":"▄▄▄ ▄ ▄ ▄▄▄",
    "Y":"▄▄▄ ▄ ▄▄▄ ▄▄▄",
    "Z":"▄▄▄ ▄▄▄ ▄ ▄",
    1:"▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄",
    2:"▄ ▄ ▄▄▄ ▄▄▄ ▄▄▄",
    3:"▄ ▄ ▄ ▄▄▄ ▄▄▄",
    4:"▄ ▄ ▄ ▄ ▄▄▄",
    5:"▄ ▄ ▄ ▄ ▄",
    6:"▄▄▄ ▄ ▄ ▄ ▄",
    7:"▄▄▄ ▄▄▄ ▄ ▄ ▄",
    8:"▄▄▄ ▄▄▄ ▄▄▄ ▄ ▄",
    9:"▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄",
    0:"▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄ ▄▄▄",
    " ":"       ",
}
string_to_encode=input("What do you want to encode? : ").upper()
encoded_string=""
for char in string_to_encode:
    if char in morse_dictionary:
        encoded_string+=morse_dictionary[char]+"   "
    else:
        print(f"Character {char} is not in english dictionary")
encoded_string=encoded_string[:len(encoded_string)-3]
print(encoded_string)