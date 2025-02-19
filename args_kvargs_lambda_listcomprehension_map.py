# Atspausdintų didžiausią 
# iš kelių paduotų skaičių (panaudojant *args).

# inputas=input("iveskite sveikus skaicius ir sudetike tarp ju tarpus")
# inputlist=inputas.split()

# int_list=list(map(int, inputlist)) #su map funkcija paverciam lista i integeriu lista

# def didskaicius(*arges):
    
#     maxskaicius=arges[0]

#     for num in arges:
#         if num>maxskaicius:
#             maxskaicius=num
#     return(maxskaicius)

# rezultatas=didskaicius(2,3,5,9,8,7)
# print(rezultatas)

#Gražintų paduotą stringą atbulai.
# stringas=input("parasyk kas negerai")

# def didskaicius(hohoho):
#     atbulai=hohoho[::-1]
#     return(atbulai)
# ats=didskaicius(stringas)
# print(ats)

# Uzduotis: Atspausdinti, kiek paduotame stringe yra žodžių, 
# didžiųjų ir mažųjų raidžių, skaičių.
# inputas=input("""isvardink savo seimos nariu vardus ir pavardem it irasyk ju gimimo metus
# (viska ivesti per tarpa):""")
# inputsarasa=inputas.split()

# def cymbolupaieska(cymbolai,mokolai):
#     skaiciai=0
#     zodziai=0
#     upperis=0
#     loweris=0
#     for wordas in mokolai:
#         if wordas.isdigit()==False:
#             zodziai+=1
#     for cymbol in cymbolai:
#         if cymbol.isdigit():
#             skaiciai+=1
#         if cymbol.isupper():
#              upperis+=1
#         if cymbol.islower():
#             loweris+=1
#     rezultatas=(
#         f"Jusu irase tiek skaiciu: {skaiciai}\n"
#         f"Jusu irase tiek zodziu: {zodziai}\n"
#         f"Jusu irase tiek didziuju raidziu: {upperis}\n"
#         f"ir jusu irase tiek mazuju raidziu: {loweris}\n"
#     )
#     return(rezultatas)
    
# print(cymbolupaieska(inputas,inputsarasa))

#Uzduotis.Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.

# inputas=input("isvardink Baltijos salis (viska ivesti per tarpa):")


# def svarybe(tra):
#     inputsarasa=tra.split()
#     svarusarasas=set(inputsarasa)
#     return list(svarusarasas) 

# print(svarybe(inputas))

# Uzduotis. Gražintų, ar paduotas skaičius yra pirminis.

# inputas=int(input("ivesk sveika, pirmini skaiciu jei nori gauti doleri"))

# def svarybe(tra):
#     if tra==2 or tra%2!=0 and tra>1:
#         print("Jusu ivestas skaicius tikrai pirminis, stai jusu doleris - $")
#     else:
#         print("Jusu ivestas skaicius nepirminis, spyga taukuota jums")

# print(svarybe(inputas))

# lambda versija
# lfartface=lambda inputas:True if (inputas==2 or (inputas%2!=0 and inputas>1)) else False

# print(lfartface(inputas))

# Uzduotis.Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo

# inputas=input("Irasyk sakini be kableliu atbulai")
# def svarybe(tra):
#     inputsarasa=tra.split()
#     inputsarasa.reverse()
#     return(inputsarasa)

# print (svarybe(inputas))

#Uzduotele. Gražina, ar paduoti metai yra keliamieji, ar ne.
# metai=int(input("irasykite savo gimimo metus"))
 
# def keliamiejine(tra):
#     if tra % 4 == 0 and tra % 100 != 0 or tra % 400 == 0: 

#         return("Jus gimete keliamaisiais metais")
#     else:
#         return("Jus gimete nekeliamaisiasi metais")

# print(keliamiejine(metai))

#Uzduotis. Atspausdina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių.
# laikas=input("iveskite savo gimimo data ir laika siuo formatu yyyy-mm-dd-hours:minutes:seconds")

# def keliamiejine(tra):
#     try:
#         import datetime
#         laikasgeras=datetime.datetime.strptime(tra, "%Y-%m-%d-%H:%M:%S")
#         print(laikasgeras)
#         pralekeslaikas=datetime.datetime.today()-laikasgeras
#         print(pralekeslaikas,"praleke sitiek laiko")
# #Paskaiciuoti kiek praejo metu
#         praejometu=pralekeslaikas.total_seconds()/31557600#pralekes laikas konvetuojamas i sskundes ir padalinamas is sekundziu metuose (aprox)
#         print(f"{round(praejometu)},praleke sitiek metu utatatata")#suapvalinamas rezultatas su round operacija
# #Paskaiciuoti kiek praejo menesiu
#         praejomen=(praejometu*12)#apskaiciuotas skirtumas metais dauginamas is menesiu metuose ir suzinomas skirtumas dienomis
#         print(f"{round(praejomen)},praleke sitiek menesiu utatatata")#suapvalinamas rezultatas
# #Kiek praejo dienu
#         dienu=pralekeslaikas.days
#         print("Praejo sitiek dienu",dienu)
# #Kiek praejo valandu
#         valandu=pralekeslaikas.total_seconds()/60
#         print("Praejo sitiek valandu",valandu)
# #Kiek praejo sekundeliu
#         sekundeliu=pralekeslaikas.total_seconds()
#         print(f"{round(sekundeliu)}, Praejo sitiek sekundziu")#vistiek suapvalinau, kad gautusi sveikas skaicius
#     except:
#         print("soriukas, isivele klaida")

# keliamiejine(laikas)

#Sukurti funkciją, kuri grąžintų True reikšmę, jei įvesto skaičiaus pirma skaitmenų pusė yra lygi antrąjai, priešingu atveju grąžintų False.
# inputas=input("iveskite keturis sveikus skaicius be tarpu")
   
# def didskaicius(hohoho):   
#     try:
#         if len(hohoho)>4 or len(hohoho)<4 or hohoho.isdigit()==False:
#             raise ValueError("kazka ne taip ivedete")
#         tarp_sarasas=list(hohoho)
#         sarasas=list(map(int,tarp_sarasas))
#         if sarasas[0]+sarasas[1]==sarasas[2]+sarasas[3]:
#             return(True)
#         else:
#             return(False)
#     except ValueError as valer:
#         print(valer)
#      
# didskaicius(inputas)

#Uzduotis. arašyti funkciją, kuri grąžintų, kiekvieno elemento gretimą skaičių. Pvz:
    #   Input: 5678
    #   Output: 5 – 46, 6 – 57, 7 – 68, 8 - 79
# inputas=input("iveskite skaicius be tarpu")
   
# def didskaicius(hohoho):   
#     try:
#         if hohoho.isdigit()==False:
#             raise ValueError("kazka ne taip ivedete")
#         tarp_sarasas=list(hohoho)
#         sarasas=list(map(int,tarp_sarasas))
#         for i in range(0, len(sarasas)):
#             if i==0:
#                 print(f"{sarasas[i]} - {sarasas[i+1]}")
#                         # jei skaicius nepaskutinis, spausdina skaiciu ir per bruksni kairi bei desini kaimyna
#             if i < len(sarasas) - 1:
#                 print(f"{sarasas[i]} - {sarasas[i-1]}{sarasas[i+1]}")
#             else:
#             # paskutiniam skaiciui printinam tik kairi kaimyna per bruksni. 
#                 print(f"{sarasas[i]} - {sarasas[i-1]}")

#     except ValueError as valer:
#         print(valer)
#         return("bandysim dar karta?")
    
# didskaicius(inputas)

import os 
# os.mkdir"("os_modulis_sukurti_faila__perskaitytyti_pakeisti_turini_pavadinima_lokacija.py")
# with open("failas.py",'w')

# os_modulis_sukurti_faila__perskaitytyti_pakeisti_turini_pavadinima_lokacija

# os.mkdir("Testinis.py")
# filename = "os_modulis_sukurti_faila__perskaitytyti_pakeisti_turini_pavadinima_lokacija.py"
# os.mknod(filename)
print(os.mkdir("os_modulis_sukurti_faila__perskaitytyti_pakeisti_turini_pavadinima_lokacija.py"))
