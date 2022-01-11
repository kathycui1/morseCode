def morse(text):
    encrypt = {'A': '.-', 'B': '-...', 'C': '-.-.',
               'D': '-..', 'E': '.', 'F': '..-.',
               'G': '--.', 'H': '....', 'I': '..',
               'J': '.---', 'K': '-.-', 'L': '.-..',
               'M': '--', 'N': '-.', 'O': '---',
               'P': '.--.', 'Q': '--.-', 'R': '.-.',
               'S': '...', 'T': '-', 'U': '..-',
               'V': '...-', 'W': '.--', 'X': '-..-',
               'Y': '-.--', 'Z': '--..',

               '0': '-----', '1': '.----', '2': '..---',
               '3': '...--', '4': '....-', '5': '.....',
               '6': '-....', '7': '--...', '8': '---..',
               '9': '----.',

               ' ': ' ', '?': '..--..', ',': '--..--', '.': '.-.-.-',
               }
    decrypt = {value: key for key, value in encrypt.items()}

    # check if text is morse code or letters
    i = 0
    while i != len(text):
        if text[i] == "." or text[i] == "-" or text[i] == " ":
            i += 1
        else:
            return ' '.join(encrypt[i] for i in text.upper())
    if i == len(text):
        j = 0
        code = list(encrypt.values())
        splitted_text = text.split()
        while j != len(splitted_text):
            if splitted_text[j] in code:
                j += 1
            else:
                return "Invalid morse code representation"
        if j == len(splitted_text):
            return ''.join(decrypt[i] for i in text.split())