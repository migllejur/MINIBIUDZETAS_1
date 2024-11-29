def gauk_statistika(sk, operacija="suma"):
    if operacija == "suma":
        return sum(sk)
    elif operacija == "min":
        return min(sk)
    elif operacija == "max":
        return max(sk)
    elif operacija == "average":
        return sum(sk) / len(sk) if sk else 0
    return None


def istrinti_ieskoti(duomenys, operacija="istrinti"):
    if operacija == "istrinti":
        for nr, elem in enumerate(duomenys, start=1):
            print(f"{nr}. {elem}")
        try:
            sk = int(input("Įveskite skaičių duomenų, kuriuos norite ištrinti: "))
            if 1 <= sk <= len(duomenys):
                del duomenys[sk - 1]
                print("Duomenys ištrinti")
            else:
                print("Klaida. Duomenys neištrinti. Bandykite dar kartą.")
        except ValueError:
            print("Klaida. Įvestas netinkamas kriterijus. Bandykite dar kartą.")
    if operacija == "ieskoti":
        search = input("Įveskite raktažodį (sumą, pavadinimą arba datą): ")
        found = False
        for elem in duomenys:
            if search in elem:
                print(elem)
                found = True
        if not found:
            print("Duomenys nerasti")
    return duomenys
