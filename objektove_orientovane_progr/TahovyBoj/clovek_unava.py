# Vytvoreni tridy cloveka dle priklady 3.-5. lekce

class ClovekUnava:
    unava = 0

    def __init__(self, jmeno, vek):
        self._jmeno = jmeno
        self._vek = vek

    def __str__(self):
        return str(f"{self._jmeno} {self._vek}")
    
    def spanek(self,cas):
        self.unava = max(self.unava-10*cas,0)

    def beh(self,cas):
        if (self.unava + cas) <= 20:
            self.unava += cas
        else:
            print("Jsem příliš unavený")

        