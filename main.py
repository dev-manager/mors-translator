from pyperclip import copy

etm = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..'}
mte = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z'}

while True:
    mode = input('type mode \n(E)nglish to mors \n(M)ors to english\ne(X)it\n')
    if mode == 'E' or mode == 'e':
        result = ''
        print('Please type english sentence : \n')
        sentence = input('').upper()
        for i in sentence:
            if i == ' ':
                pass
            else:
                result = result + etm.get(i) + ' '
        print(result)
        copy(result)
        print('mors is copied')
        sentence = ''
    elif mode == 'M' or mode == 'm':
        result = ''
        print('Please type mors sentence : \n')
        sentence = input('').upper()
        for i in sentence:
            if i == '':
                pass
            else:
                result += mte.get(i)
        print(result)
        sentence = ''
    else:
        break
    break
