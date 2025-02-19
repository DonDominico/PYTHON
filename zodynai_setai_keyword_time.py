# dictionary={"Petras":15,"Vytautas":16,"Merkys":6, "Mykoliuka":1}
# print(dictionary)
# dictionary["Vycka"]=20 
# print(dictionary)
# del dictionary["Merkys"]
# print(dictionary)
# dictionary["Vytautas"]=115
# print(dictionary)
# print(dictionary.keys())
# print(dictionary.values())
# print(dictionary.get("Liulka"))
# # dictionary.clear()
# # print(dictionary)
# # dictionary_kopija=dictionary.copy()
# # print(dictionary_kopija)
# # difrtface=dictionary.items()
# # print(difrtface)
# # fartfc=dictionary.fromkeys("Vytautas","Mykoliuka")
# # print(fartfc)
# dictionary.pop("Vycka")
# print(dictionary)
# dictionary.popitem()
# print(dictionary)
# # voltai=dictionary.setdefault("Petras,"Vytautas")
# dictionary2={"PetLyras":125,"Vytautas2":17,"Merkys":6, "Mykoliukas":125}   
# dictionary.update(dictionary2)  
# # print(dictionary)   
# # print(dictionary2)      
# print(dictionary)
# nulis=dictionary.setdefault("sausis",5)
# print(dictionary)
# dictionary={"Petras":15,"Vytautas":16,"Merkys":6, "Mykoliuka":1}
# nulis=dictionary.setdefault("sausis",5)
# print(dictionary)

# # Uzduotis1 "Zen of Python"

# #Atspausdinti paskutinis antro zodzio simbolis
# Zenius="Zen of Python"
# print(Zenius[-8])

#Atspausdinti pirma trecio zodzio simboli
# print(Zenius[-6])

# #Atspausdinti tik pirma zodi
# print(Zenius[0:3])

# #Atspausdinti visa fraze atbulai
# print(Zenius[::-1])

# #Atspausdinti kiekviena zodi atskirai
# print(Zenius[0:3])
# print(Zenius[4:7])
# print(Zenius[7:14])

#Zodi python pakeiciam i programming
# Zenius_programming=Zenius.replace("Python","Programming")
# print(Zenius_programming)

#UZDUOTIS SARASAI/TUPLE
#isgryninti sarasa
# Sarasas_kartoklis=["varske","sviestas","pienas","sviestas","desra","sviestas","varske","pienas"]
# setas=set(Sarasas_kartoklis)
# print(setas)

#UZDUOTIS SARASAI/TUPLE vs SARASAS
# import time
# # sarasas=["varske","sviestas","pienas","sviestas","desra","sviestas","varske","pienas"]
# # tuplas=("varske","sviestas","pienas","sviestas","desra","sviestas","varske","pienas")
# # #Skaiciuojam sarasa
# start=time.perf_counter()
# # print(sarasas)
# end=time.perf_counter()
# print((end-start)*1000)
# # #Skaiciuojam tupla
# start=time.perf_counter()
# # print(tuplas)
# end=time.perf_counter()
# print((end-start)*1000)
# # #Reziume
# # print("Tuplas greitesnis uz sarasa")

#Antra Uzduotis laiko nesustabdysi ir neatsuksi atgal
# metai=int(input("iveskite savo gimimo metus"))1952
# keliamieji_metai=(1928, 1932, 1936, 1940, 1944, 1948, 1952, 1956, 1960, 1964, 1968, 1972, 1976, 1980, 1984, 1988, 1992, 1996, 2000, 2004, 2008, 2012, 2016, 2020, 2024)
# if metai in keliamieji_metai: 
#     print("Jus gimete keliamaisiais metais")
# else:
#     print("Jus gimete nekeliamaisiais metais")

#Sios dienos uzduotis

#vartotojas iveda varda pavarde ir sukuriu zodyna
vardas=input("iveskite savo varda")
pavarde=input("iveskite savo pavarde")
Vardapavarde={"vardelis":vardas, "pavardele":pavarde}
Vardas=Vardapavarde["vardelis"]
Pavarde=Vardapavarde["pavardele"]
print(Vardas, Pavarde)

#5-iu elementu kombinacija vartotojui
# Skaicius1=float(input("pirma skaiciu"))
# Skaicius2=float(input("pirma skaiciu"))
# Skaicius3=float(input("pirma skaiciu"))
# Skaicius4=float(input("pirma skaiciu"))
# Skaicius5=float(input("pirma skaiciu"))
# Sarasas=[Skaicius1, Skaicius2, Skaicius3,Skaicius4, Skaicius5]
# print(Sarasas)
# naujar=float(input("nauja skaiciu"))
# if naujar in Sarasas:
#     print("jusu ivestas skaicius jau buvo ivestas anksciau")
# else:
#     print("jus ivedete nauja skaitmeneli")

#Vardo uzduotis
# Vardas=input("iveskite savo varda")
# Vardas=Vardas.capitalize()
# print(f"sveiki, {Vardas}")

#Egzamino balo uzduotis
# egzaminobal=int(input("Iveskite savo egzamino bala"))
# if egzaminobal <= 49: 
#     print("Neislaikete")
# elif egzaminobal >= 50 and egzaminobal <= 64:
#     print("Patenkinamai")
# elif egzaminobal >= 65 and egzaminobal <= 79:
#     print("Gerai")
# elif egzaminobal >= 80 and egzaminobal <= 89:
#     print("Lab gera")
# elif egzaminobal >= 90 and egzaminobal <= 100:
#     print("Pukiai")

#Penkiu skaiciu saraso uzduotis su vartotojo ivestim
# Sarasas=[1, 2, 3, 4, 5]
# Vartsk=int(input("iveskite savo skaiciu, vartotojau"))
# if Vartsk in Sarasas:
#     Sarasas.remove(Vartsk)
#     print(Sarasas)
# else:
#     Sarasas.append(Vartsk)
#     print(Sarasas)

#Uzduotis studentu zodynas
# Studiction={"Vytas":5,"Aloyzas":7,"Bronislovas":8}
# Sarasas=[1, 2, 3, 4, 5]
# if Vardas in Studiction:
#     print(f"Studento pazymys yra:{Studiction[Vardas]}")
# else:
#     print("tokio studijuotojo nera")


# #Uzduotis tekstas bent 4 zodziu
# Keturizod=input("iveskite teksta")
# ilgis=len(Keturizod.split())
# print(ilgis)
# if ilgis <4:
#     print("Reikia ilgesnio teksto, iveskite daugiau zodziu")
# else:
#     print("dekojame uz jusu laika")

# Sunkesne uzduotele - naudotojas įveda 3 atsitiktinius skaičius, išrykiuokite juos nuo mažiausio iki didžiausio, nenaudodami ciklų.
# skaiciai3=input("iveskite tris skaicius")
# skaiciai3_1=list(skaiciai3)
# skaiciai3_1.sort()
# print(f"jusu ivesti skaiciai is eiles {skaiciai3_1}")


# sumUDETINGESNE UZDUOTELE SUKURTI SARASA IR LEISTI VARTOTOJUI SUKURTI DU INDESKUS BEI SUKEISTI TUOSE INDEKSUOSE ESANCIA REIKSMES
# Sarasas=[1, 2, 3, 4, 5]
# indexas1=input("iveskite pirma indexa")
# indexas2=input("iveskite antra indexa")
# Sarasas[0]=indexas1
# Sarasas[1]=indexas2
# print(Sarasas)

# sumUDETINGESNE UZDUOTELE leisti ivesti teksta ir patikrinti ar jame yra "programavimas"
# Keturizod=input("iveskite teksta")
# sarKeturizod=Keturizod.split()
# if "Programavimas" in sarKeturizod:
#     print("Yra!")
# else:
#     print("ar jus tikrai neturite nieko bendro su programavimu?")

# Sunkesne uzduotele 5 simboliu slaptazodis vartotojui kur didzioji, mazoji, skaicius 
# Slaptazodis=input("Sveskite penkiu simboliu slaptazodi ivesdami tarpa po kiekvieno simbolio.Slaptazodyje turi buti bent vienas skaicius, bent viena mazoji raide, bent viena didzioji raide")
# ilgis=len(Slaptazodis)
# if ilgis !=5:
#     print("iveskite 5-iu simboliu slaptazodi")
# elif Slaptazodis[0].isdigit()==False and Slaptazodis[1].isdigit()==False and Slaptazodis[2].isdigit()==False and Slaptazodis[3].isdigit()==False and Slaptazodis[4].isdigit()==False:
#     print("ivestame slaptazdy nera skaiciaus")
# elif Slaptazodis[0].islower()==False and Slaptazodis[1].islower()==False and Slaptazodis[2].islower()==False and Slaptazodis[3].islower()==False and Slaptazodis[4].islower()==False:
#     print("netinkamas slaptazodis, slaptazodyje turi buti bent viena mazoji raide")
# elif Slaptazodis[0].isupper()==False and Slaptazodis[1].isupper()==False and Slaptazodis[2].isupper()==False and Slaptazodis[3].isupper()==False and Slaptazodis[4].isupper()==False:
#     print("netinkamas slaptazodis, slaptazodyje turi buti bent viena didzioji raide")
# else:
#     print("jusu slaptazodis isaugotas")


# Uzduotis su valiutu kursais ir konvertavimu
# valkur={"EUR":3.45, "USD":4, "GBP":5}
# pradval=input("iveskite norima konvertuoti valiuta")
# galval=input("iveskite norima gauti valiuta")
# if pradval.upper() not in valkur or galval.upper() not in valkur:
#     print("sios valiutos nekonvertuojame")
# else:
#     sumele=float(input("iveskite norima konvertuoti suma")) 
#     konvert_rez=(sumele*valkur[pradval.upper()])/valkur[galval.upper()]
#     print(f"konvetavimo rezultatas {konvert_rez}")

# Kitos uzduotys namu darbams

# Restorano dienos patieklau meniu programa
# Meniu={"pirmadienis":"Vistos koja","antradienis":"karka", "treciadienis":"kiaule pataluose", "ketvirtadienis":"silkute", "pektadienis":"cepai"}
# uzklausimas=input("ivesk savaites diena, kad suzinoti tos dienos patiekala")
# uzklausimas=uzklausimas.lower()
# if uzklausimas in Meniu:
#     print(f"dienos patiekalas {Meniu.get(uzklausimas)}")
# else:
#     print("savaitgaliais ir svenciu dienomis nedirbame")

# Temperaturos patikrinimo uzduotis
# temperatura=float(input("Iveskite jusu temperatura: "))
# if temperatura >= 37.5:
#     print ("jus ligonis, gerkite daugiau skysciu ir daugiau ilsekites horizantalioje padetyje")
# else:
#     print("jums niekas negresia")

# Spalvu maisymo uzduotis
# spalva1=input("iveskite pirma spalva maisymui")
# spalva2=input("iveskite antra spalva maisymui")
# spalvynas={("raudona", "geltona"):"oranzine",("raudona", "melyna"):"violetine",("geltona","melyna"):"zalia"}