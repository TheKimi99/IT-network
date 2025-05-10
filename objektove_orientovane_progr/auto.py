
class Auto():
    spz = None
    barva = None

    def __str__(self):
        return "hovno"

    def __init__(self, spz, barva):
        self.spz = spz
        self.barva = barva

    def vrat_spz(self):
        return self.spz
    
    def zaparkuj(self,garaz):
        garaz.vloz(self)