# The declaration of the Morse Code class
class morseCode:
    def __init__(self,ltr,code):
        self.ltr = ltr
        self.code = code

def translateToMorse(codes, msg):
    tmpMsg = ""
    for letter in msg:
        for code in codes:
            if letter == code.ltr:
                tmpMsg = tmpMsg + code.code + "/"
                break
    return tmpMsg

# The list of codes that are used
codes = []

# Saving the codes in the list
codes.append(morseCode("a", ".-"))
codes.append(morseCode("b", "-..."))
codes.append(morseCode("c", "-.-."))
codes.append(morseCode("d", "-.."))
codes.append(morseCode("e", "."))
codes.append(morseCode("f", "..-."))
codes.append(morseCode("g", "--."))
codes.append(morseCode("h", "...."))
codes.append(morseCode("i", ".."))
codes.append(morseCode("j", ".---"))
codes.append(morseCode("k", "-.-"))
codes.append(morseCode("l", ".-.."))
codes.append(morseCode("m", "--"))
codes.append(morseCode("n", "-."))
codes.append(morseCode("o", "---"))
codes.append(morseCode("p", ".--."))
codes.append(morseCode("q", "--.-"))
codes.append(morseCode("r", ".-."))
codes.append(morseCode("s", "..."))
codes.append(morseCode("t", "-"))
codes.append(morseCode("u", "..-"))
codes.append(morseCode("v", "...-"))
codes.append(morseCode("w", ".--"))
codes.append(morseCode("x", "-..-"))
codes.append(morseCode("y", "-.--"))
codes.append(morseCode("z", "--.."))
codes.append(morseCode(" ", " "))
codes.append(morseCode("1", ".----"))
codes.append(morseCode("2", "..---"))
codes.append(morseCode("3", "...--"))
codes.append(morseCode("4", "....-"))
codes.append(morseCode("5", "....."))
codes.append(morseCode("6", "-...."))
codes.append(morseCode("7", "--..."))
codes.append(morseCode("8", "---.."))
codes.append(morseCode("9", "----."))
codes.append(morseCode("0", "-----"))
codes.append(morseCode("?", "..--.."))
codes.append(morseCode("!", "-.-.--"))
codes.append(morseCode(".", ".-.-.-"))
codes.append(morseCode(",", "--..--"))
codes.append(morseCode(";", "-.-.-."))
codes.append(morseCode(":", "---..."))
codes.append(morseCode("+", ".-.-."))
codes.append(morseCode("-", "-....-"))
codes.append(morseCode("/", "-..-."))
codes.append(morseCode("=", "-...-"))

# Reading the text from keyboard
msg = input("Please enter the message you want to send:\n")
msg = msg.lower()

msg = translateToMorse(codes, msg)

print(msg)    