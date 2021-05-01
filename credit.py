from cs50 import get_int

def main():
    cc_number = get_int("Number:")
    son_rakam = 0
    iki_rakam = 0
    basamak = 0
    cift_basamak = 0
    tek_basamak = 0
    carpilanlar = 0

    while cc_number > 0:
        iki_rakam = son_rakam
        son_rakam = cc_number % 10
        if basamak % 2 == 0:
            cift_basamak += son_rakam
        else:
            carpilanlar = 2*son_rakam
            tek_basamak += (carpilanlar // 10) + (carpilanlar % 10)

        cc_number //=10
        basamak += 1
    
    dogrulama = (cift_basamak + tek_basamak) % 10 == 0
    ilk_iki_num = (son_rakam * 10) + iki_rakam

    if son_rakam == 4 and basamak >= 13 and basamak <= 16 and dogrulama:
        print("VISA\n")
    elif ilk_iki_num >= 51 and ilk_iki_num <= 55 and basamak == 16 and dogrulama:
        print("MASTERCARD\n")
    elif (ilk_iki_num == 34 or ilk_iki_num == 37) and basamak == 15 and dogrulama:
        print("AMEX\n")
    else:
        print("INVALID\n")

if __name__ =="__main__":
    main()



        
