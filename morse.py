MorseCode = {
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}
NedCode = {v: k for k, v in MorseCode.items()} #Value en Key wordt om gedraaid in de dict

def M2N(): #functie voor het decoderen van de morse code
    inputM = input("Type here the morse code (there must be space's between the morse) : ")
    morse = inputM.split()
    for element in morse:
        print(NedCode[element])

def N2M(): #functie voor het coderen van de tekst
    inputN = input("Type here your text : ")
    for tekst in inputN:
        for key in MorseCode:
            if key == tekst.lower():
                print(MorseCode[key])

def vraag():    
    x = input("choose (m) for morse to text or choose (t) for text to morse: ")
    if x == "m" :
        M2N()
    elif x == "t":
        N2M()
    else:
        print(x +" is not reconised, try again!")
        vraag()


print("Welcome to the Morse encoder and decoder")
vraag()
