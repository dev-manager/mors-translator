from pyperclip import copy
import sys

ETM = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}
MTE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'}

while True:
    mode = sys.argv[1]
    if mode == '-E' or mode == '-e':
        result = ''
        sentence = sys.argv[2]
        for j in sys.argv[2:]:
            for i in j:
                i = i.upper()
                result += ETM.get(i) + ' '
        print(result)
        copy(result)
        print('mors is copied')
        sentence = ''
        break
    elif mode == '-M' or mode == '-m':
        result = ''
        sentence = sys.argv[2:]
        for i in sentence:
            result += MTE.get(i)
        print(result.capitalize())
        sentence = ''
        break