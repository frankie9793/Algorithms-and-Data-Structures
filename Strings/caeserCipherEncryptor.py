# O(N) Time | O(N) Space
def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26 
    for letter in string:
        newLetters.append(getLetter(letter, newKey))
    return "".join(newLetters)

def getLetter(letter, key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)


# O(N)  Time | O(N) Space
def caesarCipherEncryptor(string, key):
    newLetters = []
    newKey = key % 26
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    for letter in string:
        newLetters.append(getLetter(letter, newKey, alphabets))
    return "".join(newLetters)

def getLetter(letter, key, alphabets):
    newLetterCode = alphabets.index(letter) + key
    return alphabets[newLetterCode] if newLetterCode <= 25 else alphabets[-1 + newLetterCode % 25]