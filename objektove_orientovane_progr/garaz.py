
class Garaz():
    auto = None

    def vloz(self,auto):
        self.auto = auto

    def __str__(self):
        return f"V garáži je auto: {self.auto.vrat_spz()}"