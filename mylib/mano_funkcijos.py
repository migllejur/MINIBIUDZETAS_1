def statistika(*args, operacija="suma"):
    if operacija == "suma":
        rezultatas = sum(args)
    elif operacija == "min":
        rezultatas = min(args)
    elif operacija == "max":
        rezultatas = max(args)
    elif operacija == "average":
        rezultatas = sum(args) / len(args)
    return rezultatas


def istrinti_ieskoti(*args, operacija="istrinti"):
    if operacija == "istrinti":
        for nr, elem in enumerate(args, start=1):
            print(f"{nr}. {elem}")
        try:
            sk = int(input("Įveskite skaičių duomenų, kuriuos norite ištrinti: "))
            if sk <= len(args):
                del args[sk - 1]
                print("Duomenys ištrinti")
        except ValueError:
            print("Klaida. Įvestas netinkamas skaičius. Bandykite dar kartą.")
    if operacija == "ieskoti":
        search = input("Įveskite raktažodį (sumą, pavadinimą arba datą): ")
        for elem in args:
            if search in elem:
                print(elem)
        else:
            print("Duomenys nerasti")
    return args