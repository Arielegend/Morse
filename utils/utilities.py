import time

from playsound import playsound

MORSE_CODE_DICT = {' ': '/', 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
                   'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
                   'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
                   'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
                   '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def Txt_to_Morse(msg: str, mode: int) -> str:
    """
    Args: ->
        1. msg  (str): the message we wish to play in morse code
        2. mode (int): the sounds we will use to play the morse code.
    Returns ->
        The message in 'morse', to update log field, at morse_object.
    """
    code = [MORSE_CODE_DICT[i.upper()] + ' ' for i in msg if i.upper() in MORSE_CODE_DICT.keys()]
    morse = ''.join(code)

    # Each morse after all uses 2 sounds.
    # At Sounds directory, we have 10 touples of sounds.
    sound1 = "utils\\sounds\\" + str(mode) + ".1.mp3"
    sound2 = "utils\\sounds\\" + str(mode) + ".2.mp3"

    # Playing the morse code, with 0.5 seconds between each note.
    for m in morse:
        if m == '.':
            playsound(sound1)
        elif m == '-':
            playsound(sound2)
        else:
            time.sleep(0.5)

    # Returning morse form of the message.
    return morse
