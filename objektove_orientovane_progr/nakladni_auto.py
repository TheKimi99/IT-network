# vypocet nakladniho auta
class NakladniAuto:
    nosnost = 3000
    hmotnost_nakladu = 0

    def naloz(self, hmotnost):
        if (self.hmotnost_nakladu + hmotnost) <= self.nosnost:
            self.hmotnost_nakladu += hmotnost
        return self.hmotnost_nakladu
    
    def vyloz(self, hmotnost):
        if (self.hmotnost_nakladu - hmotnost) >= 0:
            self.hmotnost_nakladu -= hmotnost
        return self.hmotnost_nakladu
    
    def vypis_nalozeni(self):
        print(f"V nákladním autě je naloženo {self.hmotnost_nakladu} kg")
