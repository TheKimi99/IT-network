# Vytvoreni aplikace na predstaveni osoby

class Clovek:
    jmeno = None
    vek = None
    kamarad = None

    def predstaveni(self):
        print(f"Ahoj, já jsem {self.jmeno}, je mi {self.vek} let a můj kamarád je {self.kamarad}")