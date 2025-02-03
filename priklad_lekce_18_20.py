# # # Priklady lekce 18-20
# # Sachovnice
# hotovo na osobnim PC


# # # Prevod cisel z desitkove soustavy
# print("Číslo v desítkové soustavě:")
# cislo = input()
# cislo = int(cislo)

# print("Číselná soustava (2-16):")
# soustava = int(input())

# zbytek = []
# zbytek_10 = 0
# znaky_pro_prevod = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G"]
# cislo_po_deleni = cislo
# i = 0

# while cislo_po_deleni >= soustava:
#     zbytek_10 = cislo_po_deleni % soustava
#     zbytek.append(znaky_pro_prevod[zbytek_10])
#     cislo_po_deleni = cislo_po_deleni // soustava
#     i += 1

# # nakonec musim pripojit finalni zbytek ve formatu dane ciselne soustavy
# zbytek.append(znaky_pro_prevod[cislo_po_deleni])
# zbytek.reverse()
# zbytek_str = "".join(zbytek)

# print(f"Číslo ve zvolené soustavě: {zbytek_str}", end = "")


# # Setrideni cisel
cisla = input("Zadej čísla pro seřazení (oddělená čárkou):\n")

# zjisteni, zda zadani obsahuje mezery
cisla_list = cisla.split(",")
for i in range(len(cisla_list)):
    cisla_list[i] = int(cisla_list[i].strip())

# setrideni pomoci Selection sort
for i in range(len(cisla_list)):
    minimum = cisla_list[i]
    index_minima = i
    for j in range(i+1,len(cisla_list)):
        if cisla_list[j] < minimum:
            minimum = cisla_list[j]
            index_minima = j
    cisla_list[index_minima] = cisla_list[i]
    cisla_list[i] = minimum
    # print(cisla_list)

# prevod int na str pro vypis do konzole
for i in range(len(cisla_list)):
    cisla_list[i] = str(cisla_list[i])

# vypis serazenych cisel do konzole
cisla_serazena = ", ".join(cisla_list)
print(f"Seřazená čísla: \n{cisla_serazena}")

# comment
    