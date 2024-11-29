import datetime

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
        data = input("Data: ")
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
    if ivestis == "q":
        break
