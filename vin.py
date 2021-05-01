import sys

Büyük_Harf = 65
Kücük_Harf = 97
Mod_deger = 26


def dogrulama(k):
    for words in k:
        if words.isalpha() == False:
            return False
        else:
            return True


def main():
    if len(sys.argv) != 2 or dogrulama(sys.argv[1]) == False:
        print("Usage: python vigenere.py k")
        return 1
    else:
        i = 0
        key = sys.argv[1]
        text = input("plaintext: ")
        key_len = len(key)

        print("ciphertext: ", end="")

        for words in text:
            if words.isalpha() == False:
                print(words , end="")
                continue
            else:
                if words.isupper() == True:
                    Ayrım = Büyük_Harf
                else:
                    Ayrım = Kücük_Harf
                key_word = key[i % key_len]
                text = ord(words) - Ayrım
                key_log = ord(key_word.upper()) - Büyük_Harf
                text = ((text + key_log) % Mod_deger) + Ayrım
                text = chr(text)
                print(text , end="")
            
            i += 1

        print()
        return 0


main()



