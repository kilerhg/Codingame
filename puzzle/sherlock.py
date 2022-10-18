dict_codes = {
    "L" : "B",
    "I" : "G",
    "G" : "N",
    "V" : "L",
    "R" : "S",
    "F" : "Q",
    "Y" : "M",
    "B" : "I",
    "P" : "A",
    "S" : "W",
    "X" : "R",
    "D" : "T",
    "A" : "X",
    "H" : "K",
    "C" : "O",
    "J" : "H",
    "Z" : "U",
    "W" : "Y",
    "U" : "J",
    "T" : "P",
    "N" : "F"
}

dict_final = {
    'A': 'M'
    
    }

all_letters = ''
for letter in letters:
    if letter in dict_codes:
        all_letters += dict_codes[letter]
    else:
        print(f'letter not in dict: {letter}')
print(all_letters)