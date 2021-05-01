# Onaylandı
import sys
Büyük_Harf = 65
Kücük_Harf = 97
Mod_deger = 26



key = sys.argv[1]
if len(sys.argv)  != 2 or key.isdigit() == False:
    print("Usage:python caesar.py k")
else:
    key = int(key) % Mod_deger
    text = input("plaintext: ")
    print("ciphertext: " ,end ="")
    for words in text:
        if words.isalpha() == False:
            print(words ,end = "")
            continue
        else:
            if words.isupper() == True:
                Ayrım = Büyük_Harf
            else:
                Ayrım = Kücük_Harf
            text = ord(words) - Ayrım
            text = (text + key) % Mod_deger
            text = chr(text + Ayrım) 
            print(text , end="")
    print()

        












