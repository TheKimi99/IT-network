# pouziti kalkulacky

from kalkulacka import Kalkulacka

kalkulacka = Kalkulacka()

cislo1 = input("Zadej 1. číslo: ")
cislo2 = input("Zadej 2. číslo: ")
cislo1 = float(cislo1)
cislo2 = float(cislo2)

soucet = kalkulacka.scitani(cislo1,cislo2)
rozdil = kalkulacka.odcitani(cislo1,cislo2)
soucin = kalkulacka.nasobeni(cislo1,cislo2)
podil = kalkulacka.deleni(cislo1,cislo2)

print("Součet: " + str(soucet) + "\nRozdíl: " + str(rozdil) + "\nSoučin: " + str(soucin) + "\nPodíl: " + str(podil))