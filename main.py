from datetime import *
from random import randint

kelimeler = ["bilgisayar", "oyun", "fortnite", "klavye", "fare", "ekran", "pugb","hack","siber","kod","yazılım","kod"]
dogru = 0
yanlis = 0
c=0
a = input("Başla>> (b) ")
if a == "b":
    start = datetime.now()
    while c!=10:
        speed = kelimeler[randint(0, 11)]
        cevap = input("{} >> ".format(speed))
        if cevap == speed:
            dogru += 1

        else:
            yanlis += 1

        c+=1
    simdi=datetime.now()

sonuc=simdi-start


print("""
doğru sayısı: {}
yanlış sayısı: {}
süre: {}
""".format(dogru, yanlis, sonuc))







