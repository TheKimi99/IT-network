
class Pes():
    jmeno = None
    vek = 1

    def __init__(self, jmeno):
        self.jmeno = jmeno

    def __str__(self):
        return f"{self.jmeno} ({self.vek})"

    def zestarni(self):
        self.vek += 1