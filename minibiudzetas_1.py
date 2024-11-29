import datetime
import mano_funkcijos

pajamos = []
islaidos = []

while True:
    print("1. Įvesti pajamas\n"
          "2. Įvesti išlaidas\n"
          "3. Atspausdinti pajamų eilutes\n"
          "4. Atspausdinti išlaidų eilutes\n"
          "5. Atspausdinti statistiką\n"
          "q - išeiti")
    ivestis = input("> ")
    if ivestis == "1":
        data = input("Data (YYYY MM DD): ")
        datos_formatas = datetime.datetime.strptime(data, "%Y %m %d")
        pajamu_pav = input("Pajamų pavadinimas: ")
        suma = float(input("Pajamų suma: "))
        pajamu_listas = [datos_formatas.strftime("%Y %m %d"), pajamu_pav, suma]
        pajamos.append(pajamu_listas)
    if ivestis == "2":
        data = input("Data: ")
        datos_formatas = datetime.datetime.strptime(data, "%Y %m %d")
        islaidu_pav = input("Išlaidų pavadinimas: ")
        suma = float(input("Išlaidų suma: "))
        islaidu_listas = [datos_formatas.strftime("%Y %m %d"), islaidu_pav, suma]
        islaidos.append(islaidu_listas)
    if ivestis == "3":
        for elem in pajamos:
            print(elem)
    if ivestis == "4":
        for elem in islaidos:
            print(elem)
    if ivestis == "5":
        while True:
            print("1. Pajamų statistika\n"
                  "2. Išlaidų statistika\n"
                  "x - sugrįžti į pagrindinį meniu")
            ivestis = input("> ")
            if ivestis == "1":
                if not pajamos:
                    print("Nėra įvestų pajamų.")
                    continue
                while True:
                    print("1. Bendra pajamų suma\n"
                          "2. Didžiausia pajamų suma\n"
                          "3. Mažiausia pajamų suma\n"
                          "4. Pajamų vidurkis\n"
                          "z - sugrįžti į statistikos meniu")
                    ivestis = input("> ")
                    sumos = [suma for data, pav, suma in pajamos]
                    if ivestis == "1":
                        res = mano_funkcijos.statistika(*sumos)
                        print(res)
                    if ivestis == "2":
                        res = mano_funkcijos.statistika(*sumos, operacija="max")
                        print(res)
                    if ivestis == "3":
                        res = mano_funkcijos.statistika(*sumos, operacija="min")
                        print(res)
                    if ivestis == "4":
                        res = mano_funkcijos.statistika(*sumos, operacija="average")
                        print(res)
                    if ivestis == "z":
                        break
            if ivestis == "2":
                if not islaidos:
                    print("Nėra įvestų išlaidų.")
                    continue
                while True:
                    print("1. Bendra išlaidų suma\n"
                          "2. Didžiausia išlaidų suma\n"
                          "3. Mažiausia išlaidų suma\n"
                          "4. Išlaidų vidurkis\n"
                          "z - sugrįžti į statistikos meniu")
                    ivestis = input("> ")
                    sumos = [suma for data, pav, suma in islaidos]
                    if ivestis == "1":
                        res = mano_funkcijos.statistika(*sumos)
                        print(res)
                    if ivestis == "2":
                        res = mano_funkcijos.statistika(*sumos, operacija="max")
                        print(res)
                    if ivestis == "3":
                        res = mano_funkcijos.statistika(*sumos, operacija="min")
                        print(res)
                    if ivestis == "4":
                        res = mano_funkcijos.statistika(*sumos, operacija="average")
                        print(res)
                    if ivestis == "z":
                        break
            if ivestis == "x":
                break
    if ivestis == "q":
        break
