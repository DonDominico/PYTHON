#Pagrindinai programos kintamieji
prideti_nauja_knyga=1
Atvaizduoti_visu_knygu_sarasa=2
ieskoti_knygos=3
istrinti_knyga=4
iseiti_is_programos=5
biblioteka=[{"Pavadinimas":"vytautas ir pimpackiukai","Metai":1999,"Zanras":"dokumentika"},{"Pavadinimas":"slibinas ir grazuole","Metai":2000,"Zanras":"romantika"},{"Pavadinimas":"cepelinai garaze","Metai":2020,"Zanras":"mokslas ir pazinimas"},{"Pavadinimas":"vejas kalnuose","Metai":2005,"Zanras":"erotika"},{"Pavadinimas":"laisva ir demokratriska rusija","Metai":2005,"Zanras":"fantastika"}]

#Funkcija naujai knyga ivesti(pagal meniu 1):
def nkivedimas(nk):
    biblioteka.append(nk)
    return(biblioteka)
#Funkcija bibliotekos sarasui gauti (pagal meniu 2)
def inventorius():
    for knyga in biblioteka:
        rezultatas = biblioteka.index(knyga)+1,knyga
        print(rezultatas)       
#Funkcija naujai knygai ieskoti(pagal meniu 3):
def kpaieska(ir):
    try:
        for knyga in biblioteka:
             if ir in knyga["Pavadinimas"]:
                print("paieskos rezulatatai", knyga)
                return(knyga)
             elif ir in knyga ["Zanras"]:
                print("paieskos rezulatatai", knyga)
                return(knyga)
             else:
               raise ValueError("ivedete netesinga duomeni arba tokios knygos musu bibliotekoje nera")
    except ValueError as ups:
      print(ups)
#Funkcija knygai istrinti (pagal meniu 4):
def ktrintis(tr):
    try:
        for knyga in biblioteka:
            if tr in knyga["Pavadinimas"]:
             biblioteka.remove(knyga)
             print("Si knyga istrinta is bibliotekos:", knyga)
             return(knyga)
            else:
                raise ValueError("ivedete netesinga duomeni arba tokios knygos musu bibliotekoje nera")
    except ValueError as ouch:
            print(ouch)

#Vartotojui pateikiamas programos/bibliotekos meniu
menu=("Programos meniu: \n 1. Pridėti naują knygą \n 2. Atvaizduoti visų knygų sąrašą \n 3. Ieškoti knygos \n 4. Ištrinti knygą \n 5. Išeiti iš programos")
print(menu)
#Atliekami programos veiksmai pagal vartotojo pageidavima
while True:
    try:
        pasirinkimas=int(input("pasirinkite norima veiksma ivesdami tinkamo saraso is meniu eiles numeri"))
        if pasirinkimas<1 or pasirinkimas > 5:
            raise ValueError("pasirinkite norima veiksma ivesdami tinkamo saraso is meniu eiles numeri")
        elif pasirinkimas==1:
            naujaknyga=input("irasykite pridedamos knygos pavadinima")
            metai=input("irasykite pridedamos knygos isleidimo metus")
            zanras=input("irasykite pridedamos knygos zanra")
            naujakn={"Pavadinimas":naujaknyga,"Metai":metai,"Zanras":zanras}
            nkivedimas(naujakn)#paleidziama funkcija
            print("Nauja knyga sekmignai ivesta i biblioteka:", biblioteka)
        elif pasirinkimas==2:
            inventorius()#paleidziama funkcija
        elif pasirinkimas==3: 
            irasas=input("irasykite zodi ieskomos knygos pavadinime ar ieskomos knygos zanre")
            irasas=irasas.lower()
            kpaieska(irasas)#paleidziama funkcija
        elif pasirinkimas==4:
           trint=input("irasykite zodi ieskomos knygos pavadinime, kad ja istrinti is bilbiotekos")
           trint=trint.lower()
           ktrintis(trint)#paleidziama funkcija
        elif pasirinkimas==5:
            exit("Dekojame uz apsilnakyma musu bibliotekoje") 
    except ValueError as badchoice:
        (badchoice)
