# vytvoreni Hello world objektu

class Zdravic:
    """
    Třída reprezentuje zdravič, který slouží ke zdravení uživatelů.
    """
    text = "nezadany"
    def pozdrav(self, jmeno):
        return f"{self.text} {jmeno}!"

zdravic = Zdravic()

zdravic.text = "Ahoj uzivateli"
print(zdravic.pozdrav("Tomas"))
Zdravic.help()
