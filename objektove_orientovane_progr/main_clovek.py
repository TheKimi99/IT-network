# Vytvoreni aplikace na predstaveni osoby

from clovek import Clovek

karel = Clovek()
karel.jmeno = "Karel Novák"
karel.vek = 33
karel.kamarad = "Cyril Nový"

cyril = Clovek()
cyril.jmeno = "Cyril Nový"
cyril.vek = 27
cyril.kamarad = "Karel Novák"

karel.predstaveni()
cyril.predstaveni()