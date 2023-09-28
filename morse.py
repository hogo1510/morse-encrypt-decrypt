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
    inputM = input("Type hier de morse code in (er moeten spaties tussen de morse) : ")
    morse = inputM.split()
    for element in morse:
        print(NedCode[element])

def N2M(): #functie voor het coderen van de tekst
    inputN = input("Type hier de tekst in : ")
    for tekst in inputN:
        for key in MorseCode:
            if key == tekst.lower():
                print(MorseCode[key])

def vraag():    
    x = input("kies (m) voor morse naar nederlands of kies (n) voor nederlands naar morse: ")
    if x == "m" :
        M2N()
    elif x == "n":
        N2M()
    else:
        print(x +" wordt niet herkend, kies opnieuw!")
        vraag()


print("Welkom bij de Morse encoder en decoder")
vraag()
