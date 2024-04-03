# Morse Code Encoder

This Python script encodes input text into Morse code using a predefined dictionary. Each English letter (uppercase), digit, and space character is mapped to its corresponding Morse code representation.

## Usage
1. Run the script in a Python environment.
2. Enter the text you want to encode when prompted.
3. The script will output the Morse code representation of the input text.

## Morse Dictionary
The Morse code dictionary used in this script maps characters to their Morse code representations. The dictionary contains uppercase English letters A-Z, digits 0-9, and space character.

```python
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
```


## License

This project is licensed under the [MIT License](LICENSE).
