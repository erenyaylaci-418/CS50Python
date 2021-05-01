from cs50 import get_int

while True:
    Height = get_int("Height:")
    if Height>0 and Height<9:
        break
  
         

for a in range(Height):#kacıncı satır
    c = Height-a -1
    satır = a + 1
    for k in range(c):
        print(" ", end="")
    for s in range(satır):#satıra yazdırılan
        print("#", end="")
    print("  ", end="") 
    for s in range(satır):#satıra yazdırılan
        print("#", end="")
    print()

