from cs50 import get_float

while True:
    cash = get_float("Cash owed:")
    if cash > 0:
        break
ceyrek = 25
onluk = 10
beslik = 5
birlik = 1
#değerler belirlendi
cash = int(cash*100)

bozukluk = int(cash/ceyrek)
kalan = cash % ceyrek
bozukluk = int(kalan/onluk) + bozukluk
kalan = kalan % onluk
bozukluk = int(kalan/beslik) + bozukluk
kalan = kalan % beslik
bozukluk = int(kalan/birlik) + bozukluk
kalan = kalan % birlik





print(bozukluk)



