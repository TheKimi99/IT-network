
from pes import Pes
from osoba import Osoba

karel = Osoba("Karel Novák")
lenka = Osoba("Lenka Nováková")
azor = Pes("Azor")

karel.pes(azor)
lenka.pes(azor)

print(azor)

karel.pes.zestarni()
lenka.pes.zestarni()

print(azor)