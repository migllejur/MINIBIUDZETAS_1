import datetime
from mylib.mano_funkcijos import statistika, istrinti_ieskoti
import logging
import pickle

logging.basicConfig(filename="minibiudzetas_1.log",
                    level=logging.INFO,
                    encoding="utf-8",
                    format="%(asctime)s || %(lineno)d || %(levelname)s || %(message)s")

pajamos = []
islaidos = []

logging.info("Bandymas atidaryti pickle failą")
try:
    with open("biudzetas.pickle", mode="rb") as file:
        bendras = pickle.load(file)
        pajamos, islaidos = bendras
except FileNotFoundError:
    logging.error("Nepavyko atidaryti failo")
    pajamos = []
    islaidos = []
    bendras = [pajamos, islaidos]

logging.info("Pradėta programa, atspausdinamas pirmas meniu")
while True:
    print("1. Įvesti pajamas\n"
          "2. Įvesti išlaidas\n"
          "3. Atspausdinti pajamų eilutes\n"
          "4. Atspausdinti išlaidų eilutes\n"
          "5. Atspausdinti statistiką\n"
          "6. Ištrinti duomenis iš pajamų\n"
          "7. Ištrinti duomenis iš išlaidų\n"
          "8. Ieškoti duomenų tarp pajamų\n"
          "9. Ieškoti duomenų tarp išlaidų\n"
          "q - išeiti")
    ivestis = input("> ")
    logging.info(f"Pasirinktas skaičius: {ivestis}")
    if ivestis == "1":
        logging.info("Įvedami pajamų duomenys")
        data = input("Data (YYYY MM DD): ")
        logging.info(f"Įvesta data: {data}")
        datos_formatas = datetime.datetime.strptime(data, "%Y %m %d")
        pajamu_pav = input("Pajamų pavadinimas: ")
        logging.info(f"Įvestas pavadinimas: {pajamu_pav}")
        suma = float(input("Pajamų suma: "))
        logging.info(f"Įvesta suma: {suma}")
        pajamu_listas = [datos_formatas.strftime("%Y %m %d"), pajamu_pav, suma]
        pajamos.append(pajamu_listas)
        logging.info("Nauja informacija sudėta į listą ir prijungta prie bendro pajamų listo")
    if ivestis == "2":
        logging.info("Įvedami išlaidų duomenys")
        data = input("Data: ")
        logging.info(f"Įvesta data: {data}")
        datos_formatas = datetime.datetime.strptime(data, "%Y %m %d")
        islaidu_pav = input("Išlaidų pavadinimas: ")
        logging.info(f"Įvestas pavadinimas: {islaidu_pav}")
        suma = float(input("Išlaidų suma: "))
        logging.info(f"Įvesta suma: {suma}")
        islaidu_listas = [datos_formatas.strftime("%Y %m %d"), islaidu_pav, suma]
        islaidos.append(islaidu_listas)
        logging.info("Nauja informacija sudėta į listą ir prijungta prie bendro išlaidų listo")
    if ivestis == "3":
        for elem in pajamos:
            print(elem)
        logging.info("Atspaudintas pajamų sąrašas")
    if ivestis == "4":
        for elem in islaidos:
            print(elem)
        logging.info("Atspaudintas išlaidų sąrašas")
    if ivestis == "5":
        logging.info("Atspaudintas statistikos meniu")
        while True:
            print("1. Pajamų statistika\n"
                  "2. Išlaidų statistika\n"
                  "x - sugrįžti į pagrindinį meniu")
            ivestis = input("> ")
            logging.info(f"Pasirinktas skaičius: {ivestis}")
            if ivestis == "1":
                if not pajamos:
                    logging.error("Bandyta pasiekti pajamų statistiką - nėra įvestų pajamų.")
                    print("Nėra įvestų pajamų.")
                    continue
                while True:
                    print("1. Bendra pajamų suma\n"
                          "2. Didžiausia pajamų suma\n"
                          "3. Mažiausia pajamų suma\n"
                          "4. Pajamų vidurkis\n"
                          "z - sugrįžti į statistikos meniu")
                    ivestis = input("> ")
                    logging.info(f"Pasirinktas skaičius: {ivestis}")
                    sumos = [suma for data, pav, suma in pajamos]
                    if ivestis == "1":
                        res = statistika(*sumos)
                        print(res)
                        logging.info(f"Bendra pajamų suma: {res}")
                    if ivestis == "2":
                        res = statistika(*sumos, operacija="max")
                        print(res)
                        logging.info(f"Didžiausios pajamos: {res}")
                    if ivestis == "3":
                        res = statistika(*sumos, operacija="min")
                        print(res)
                        logging.info(f"Mažiausios pajamos: {res}")
                    if ivestis == "4":
                        res = statistika(*sumos, operacija="average")
                        print(res)
                        logging.info(f"Pajamų vidurkis: {res}")
                    if ivestis == "z":
                        logging.info("Sugrįžta į statistikos meniu")
                        break

            if ivestis == "2":
                if not islaidos:
                    logging.error("Bandyta pasiekti išlaidų statistiką - nėra įvestų išlaidų.")
                    print("Nėra įvestų išlaidų.")
                    continue
                while True:
                    print("1. Bendra išlaidų suma\n"
                          "2. Didžiausia išlaidų suma\n"
                          "3. Mažiausia išlaidų suma\n"
                          "4. Išlaidų vidurkis\n"
                          "z - sugrįžti į statistikos meniu")
                    ivestis = input("> ")
                    logging.info(f"Pasirinktas skaičius: {ivestis}")
                    sumos = [suma for data, pav, suma in islaidos]
                    if ivestis == "1":
                        res = statistika(*sumos)
                        logging.info(f"Bendra pajamų suma: {res}")
                        print(res)
                    if ivestis == "2":
                        res = statistika(*sumos, operacija="max")
                        logging.info(f"Didžiausios pajamos: {res}")
                        print(res)
                    if ivestis == "3":
                        res = statistika(*sumos, operacija="min")
                        logging.info(f"Mažiausios pajamos: {res}")
                        print(res)
                    if ivestis == "4":
                        res = statistika(*sumos, operacija="average")
                        logging.info(f"Pajamų vidurkis: {res}")
                        print(res)
                    if ivestis == "z":
                        logging.info("Sugrįžta į statistikos meniu")
                        break
            if ivestis == "x":
                logging.info("Sugrįžta į pagrindinį meniu")
                break
    if ivestis == "6":
        res = istrinti_ieskoti(*pajamos)
        logging.warning(f"Ištrinti duomenys: {res}")
        print(res)
    if ivestis == "7":
        res = istrinti_ieskoti(*islaidos)
        logging.warning(f"Ištrinti duomenys: {res}")
        print(res)
    if ivestis == "8":
        res = istrinti_ieskoti(*pajamos, operacija="ieskoti")
        logging.info(f"Surasti duomenys: {res}")
        print(res)
    if ivestis == "9":
        res = istrinti_ieskoti(*islaidos, operacija="ieskoti")
        logging.info(f"Surasti duomenys: {res}")
        print(res)
    if ivestis == "q":
        logging.info("Programa baigta")
        break

with open("biudzetas.pickle", mode="wb") as file:
    # noinspection PyTypeChecker
    pickle.dump([pajamos, islaidos], file)
    logging.info("Duomenys įrašyti į pickle failą")