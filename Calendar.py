import os
import calendar
from datetime import datetime,date, timedelta
import pickle
a = calendar.TextCalendar(calendar.MONDAY)
today = datetime.now()
kopio1 = {}
"""""
    Seuraavia funktioita ovat viikkojen ja kuukauden selailemiseen.
"""""
# http://mvsourcecode.com/python-how-to-get-date-range-from-week-number-mvsourcecode/
# getdDateRangeFromWeek tulostaa haluttu viikon ensimmäinen ja viimeinen päivät.
def getDateRangeFromWeek(p_year,p_week):
    firstdayofweek = datetime.strptime(f'{p_year}-W{int(p_week )- 1}-1', "%Y-W%W-%w").date()
    lastdayofweek = firstdayofweek + timedelta(days=6.9)
    return firstdayofweek, lastdayofweek
# This function is exclusively for getDateRangeFromWeek() to use.
# Luo lista, jonka sisältää getDateRangeFromWeek funktiolta 
def Datelist(firstdate:date, lastdate:date)-> list: 
    paivat = [firstdate + timedelta(days=x) for x in range(0, (lastdate-firstdate).days)]
    return paivat

def viikko1():
    try:
        kek1 = int(input("Vuosi?: "))
        kek2 = int(input("Viikon numero?: "))
        first, last = getDateRangeFromWeek(kek1,kek2)
        lista = [[i.strftime("%a") for i in Datelist(first,last)], [i.day for i in Datelist(first,last)]]
        print("")
        for i in lista:
            print("{: >5} {: >5} {: >5} {: >5} {: >5} {: >5}".format(*i))
        print("")
    except ValueError:
        print("Vain kokonaisnumeroina")
def kuukausi():
    try:
        kek1 = int(input("Vuosi?: "))
        kek2 = int(input("Kuukausi?: "))
        print(a.formatmonth(kek1,kek2))
    except ValueError:
        print("Vain kokonaisnumeroina")
def selailu():
    global today
    global a
    print(a.formatmonth(today.year,today.month))
    print(
    ''' 
            Input Menu:
        lopeta      --  Takaisin paaohjelmaan
        viikko1     --  Viikon numeron avulla tulostaa sen viikon paivat
        viikko2     --  Laittamalla tietyn vuoden, kuukauden ja paivan numero saat tulostettu viikon numero
        kuukausi    --  Tulostaa tietyn kuukautta laittamalla tietyn vuoden ja kuukauden numeroina
    '''
    )
    while True:
        try:
            kek1 = input("Here: ").lower()
            if kek1 == "lopeta":
                return 
            elif kek1 == "viikko1":
                viikko1()
            elif kek1 == "viikko2":
                vuosi = int(input("Vuosi: "))
                kuu = int(input("Kuukausi: "))
                päivä = int(input("Päivä: "))
                print(f"Viikko numero on {date(vuosi,kuu,päivä).isocalendar().week}")
            elif kek1 == "kuukausi":
                kuukausi()
           
        except ValueError:
            print("Error")
"""""
Seuraava funktioita ovat muistukuksen ominaisuudelle tarkoitettu.
"""""
def deletedict(data: str):
    if os.path.exists(os.path.abspath(f"{data}.txt")):
        os.remove(os.path.abspath(f"{data}.txt"))
    else:
        print("Data not found")
def loaddict(a: str):
    try:
        with open(f"{a}.txt","rb") as f:
            lista = pickle.load(f)
        for i in lista:
            print(f"{i.strftime('%d/%m/%Y')} : {lista[i]}")
    except:
        print("Data not found")
def save_dict(lista: str):
    # os.getcwd = Returns a string that contains the absolute path of the current working directory
    a = os.getcwd
    if os.path.isfile(os.path.abspath(f"{lista}.txt")):  # os.path.abspath(file) = To find the absolute path to a file
        print("This file already exits")                   # os.path.isfile(filepath) = Is there a file in this directory?
        kek1 = input("Add to it?(Yes/No):").lower()     # lisaa tekstitiedostoon 
        if kek1 == "yes":
            with open(f"{lista}.txt","ab") as f:
                pickle.dump(kopio1, f)
        else:
            kek2 = input("Owerwrite It?(Yes/No): ").lower()
            if kek2 == "yes":
                overwrite_dict(lista)
            else:
                print("Takaisin sitten") 
    else:
        print("The File doesnt exist. So let's create one.")
        with open(f"{lista}.txt","wb") as f:
            pickle.dump(kopio1, f)
    kopio1.clear()
# needs correction
def overwrite_dict(lista:str):
    global kopio1
    if os.path.isfile(os.path.abspath(f"{lista}.txt")):
        with open(f"{lista}.txt", "wb") as f:
            pickle.dump(kopio1, f)
    else:
        print("file doesnt exist")   
def notify (): 
    print("")
    print(" Muistutukset:")
    print("")
    for filename in os.listdir(os.getcwd()):    
        if filename.endswith(".txt"):    
            with open(filename,"rb") as f:
                lista = pickle.load(f)
                for i in lista:
                    print(f"{i.strftime('%d/%m/%Y')} : {lista[i]}")
    

# needs correction
def muistutus(vuosi: int, kuu: int, päivä: int):
    global kopio1
    if kopio1 == True:
        kopio1.clear()
    try:
        a = datetime(vuosi,kuu,päivä)
    except:
        print("Wrong dates")
        return
    teksti = input("Muistutus teksti: ")
    kopio1[a] = teksti
    kek1 = input("filename: ")
    save_dict(kek1)        
        
def main():   
    notify()
    print(
    '''
                Input Menu:

    muistutus   --  Muistiin laittaminen
    selailu     --  Viikon tai kuukauden selaileminen
    delete      --  Poistaa tiedosto
    load        --  Lataa tiedosto
    save        --  Tallentaa tai luo uusi tiedosto      
    '''    
    )
    print("")
    while True:
        kek1 = input("Here: ").lower()
        if kek1 == "lopeta":
            break
        elif kek1 == "selailu":
            selailu()
        # needs correction
        elif kek1 == "muistutus":               
            vuosi = int(input("Vuosi: "))
            kuu = int(input("Kuukausi: "))
            päivä = int(input("Päivä: "))
            muistutus(vuosi, kuu, päivä)
        elif kek1 == "save":
            save = input("Filename here(pelkästään nimi eikä tyyppi perään esim. ei file.txt vaan file): ")
            save_dict(save)
        elif kek1 == "load":
            load = input("Filename here(pelkästään nimi eikä tyyppi perään esim. ei file.txt vaan file): ")
            loaddict(load)
        elif kek1 == "delete":
            delete = input("What file to delete?(pelkästään nimi eikä tyyppi perään esim. ei file.txt vaan file): ")
            deletedict(delete)
main()






