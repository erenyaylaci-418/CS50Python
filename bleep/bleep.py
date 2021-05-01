from sys import argv


def main():
    if len(argv) != 2:
        print("Usage: python bleep.py dictionary")
        return 1
    else:
        filename = argv[1]
        
        dosya = open(filename, "r")
        
        sözlük = dosya.read()
        sözlük = sözlük.split()
        print("What message would you like to censor?")
        text = input()
        text = text.split()
        a = True
        for kelime in text:
            for yasakli in sözlük:
                if kelime.isupper() == True:
                    yasakli = yasakli.upper()                
                if kelime == yasakli:
                    sansür(kelime)
                    a = False
                    continue
            
            if a == True:
                print(kelime, end=" ")
            
        print()
        return 0

def sansür(words):
    for i in words:
        print("*", end="")
    print(end=" ")


if __name__ == "__main__":
    main()
