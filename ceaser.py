#from cs50 import get_string
import sys

Büyük_Harf = 65
Kücük_Harf = 97
Mod_deger = 26
def myAtoi(string):
    res = 0
    #str formatındaki veriyi integera çevirir
    for i in range(len(string)):
        res = res * 10 + (ord(string[i]) - ord('0'))
        #Sorun: -/+ kavramı yok
 
    return res
# Sorun : harf ayrımı yapılması gerekli
if len(sys.argv) != 2 or :
    print("Usage:python caesar.py k")
    #return 1
else:
    
    key =myAtoi (sys.argv[1]) % Mod_deger
    if key > 0:
        text = input("plaintext:")

        print("ciphertext: ",end="")
        #strlen = len(text)

        for i in text:
            if (i.isalpha()) == False:
                print(i , end="")
                continue
            
            if i.isupper() == True:
                Hassasiyet = Büyük_Harf
            else:
                Hassasiyet = Kücük_Harf
            ceviri = ord(i) - Hassasiyet
            #Sorun : çevirimde anormallik var
            sonuc = (ceviri + key) % Mod_deger
            yazi = sonuc + Hassasiyet
            print(chr(yazi) , end="")
    else:
        print("Usage:python caesar.py k")
    #return 0



    
