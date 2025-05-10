import random

class GeneratorVet:
    privlastky = ["modrý", "velký", "hubený", "nejlepší", "automatizovaný"]
    podmety = ["jednorožec", "programátor", "manažer", "hroch", "T-rex"]
    prislovce = ["rychle", "s oblibou", "hodně", "málo", "se zpožděním"]
    slovesa = ["spal", "ležel", "vařil", "uklízel", "derivoval"]
    mista = ["pod stolem", "v lese", "u babičky", "v práci", "na stole"]

    def generuj_vetu(self):
        self.veta = f"{random.choice(self.privlastky)} {random.choice(self.podmety)} {random.choice(self.prislovce)} {random.choice(self.slovesa)} {random.choice(self.mista)}"
        print(self.veta)
    
