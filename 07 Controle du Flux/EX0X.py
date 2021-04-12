import sys

morse_dic = {'F': '..-.', 'X': '-..-', 'P': '.--.', 'T': '-', '2': '..---', 
            '4': '....-', '0': '-----', '7': '--...', 'V': '...-', 
            'C': '-.-.', 'E': '.', 'J': '.---', 'O': '---', 'K': '-.-', 
            '9': '----.', 'I': '..', 'L': '.-..', '5': '.....', 
            '3': '...--', 'Y': '-.--', '6': '-....', 'W': '.--', 
            'H': '....', 'N': '-.', 'R': '.-.', 'B': '-...', '8': '---..', 
            'Z': '--..', 'D': '-..', 'Q': '--.-', 'G': '--.', 'M': '--', 
            'U': '..-', 'A': '.-', 'S': '...', '1': '.----'}

if (len(sys.argv) != 2):
    print("Usage: python3 morse.py 'Message to translate'")
else:
    translation = ""
    for letter in sys.argv[1]:
        if letter == ' ':
            translation += '\t'
        elif letter.upper() in morse_dic:
            translation += morse_dic[letter.upper()] + ' '
        else:
            print("Letter '", letter, "' is not part of morse dic.")
            print("Please, only use letters and numbers")
            sys.exit()
    print(sys.argv[1], ' -> ', translation)
