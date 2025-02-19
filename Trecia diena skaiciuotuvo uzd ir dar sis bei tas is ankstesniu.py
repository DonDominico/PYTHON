# pirma uzduotis
# vardas=input("jusu vardas: ")
# pavarde=input("jusu pavarde: ")
# amzius=input("jusu amzius: ")
# print(f"Sveiki,{vardas}, {pavarde}, {amzius}")
# Antra uzduotis
# kovas=float(input("iveskite jusu kovo men alga: "))
# balandis=float(input("iveskite jusu balandzio men alga:"))
# geguzis=float(input("iveskite jusu geguzes men alga:"))
# print(kovas+balandis+geguzis)
# Trecia uzduotis
# kovas=float(input("iveskite jusu kovo men alga: "))
# balandis=float(input("iveskite jusu balandzio men alga:"))
# geguzis=float(input("iveskite jusu geguzes men alga:"))
# birzelis=float(input("iveskite jusu birzelio men alga:"))
# liepa=float(input("iveskite jusu liepos men alga:"))
# print((kovas+balandis+geguzis+birzelis+liepa)/5)
#ketvirta uzduotis
# vardas=input("jusu vardas: ")
# print(vardas.upper())
#Penkta uzduotis
# info=input("´jusu isilavinimas: ")
# print(info.replace(".","PERIOD"))

# vardas1=input("iveskite varda")
# pavarde1=input("iveskite pavarde")
# vardas2=input("iveskite varda")
# pavarde2=input("iveskite pavarde")

# loginas=input("iveskite logina")
# passwordas=input("iveskite passworda")
# # print(f"koks jusu,{loginas}{passwordas}")
# if loginas=="Jonas" and passwordas=="kurmis": 
#     print("sveiki prisijunge")
# # if loginas!="Jonas" or passwordas!="kurmis": 
# #     print('prisijungimas negalimas')    
# else: 
#     print("kazkas negerai zmogau")
# Pirma uzduotis
# skaicius_a=float(input("iveskite skaiciu a"))
# skaicius_b=float(input("iveskite pavarskaiciu b"))
# if skaicius_a < skaicius_b:
#     print ("skaicius a mazesnis uz skaicius b")
# if skaicius_a == skaicius_b: 
#     print("skaicius a lygus skaiciui b")
# if skaicius_a > skaicius_b:
#     print ("skaicius a didesnis uz skaicius b")
# Trecia uzduotis
# kiekis=float(input("iveskite prekiu kieki"))
# kaina_uz_vieneta=float(input("iveskite kaina uz vieneta"))
# bendra_suma=kiekis*kaina_uz_vieneta
# # print(f'bendra suma "{bendra_suma}')
# if bendra_suma > 500:
#     print(f'bendra suma {bendra_suma*1.1}')
# else:
#     print(f'bendra suma {bendra_suma +5}')
# trecia uzduotis
# amzius=float(input("iveskite savo amzeli"))
# if amzius < 1:
#      print("tamsta naujagimis arba kudikis")
#  if amzius > 1 and amzius <13 or amzius==1: 
#      print("tamsta esat vaikas")
#  if amzius > 13 and amzius <18: 
#      print("tamsta esat paauglys")
#  if amzius > 18 and amzius < 25:
#       print("tamsta esat jaunuolis")
#  if amzius > 25 and amzius <55: 
#       print("tamsta esat suauges")
#  if amzius > 55 and amzius < 99: 
#           print("tamsta esat senjoras")
#  if amzius > 99: 
#       print("tamsta esat simtametis")
#Lentele
# print(f"{"vardas":^{20}}|{"pavarde":^{20}}|{"amzius":^{6}}|")
# print(f"{"Vytukas":^{20}}|{"Pabedinskas":^{20}}|{"66":^{6}}|")
# print(f"{"Dziugiukas":^{20}}|{"Pabackiukas":^{20}}|{"16":^{6}}|")
# print(f"{"Jonas":^{20}}|{"Stasiukaitis":^{20}}|{"16":^{6}}|")
#Uzduotis Kalkuliatorius
skaicius1=input("iveskite pirma skaiciu")
skaicius1_svarus=skaicius1.replace("-","",1).replace(".","",1)#kaip pasitikrinti ar stringas ivestas yra skaicius
if skaicius1_svarus.isdigit()==False:#kaip pasitikrinti ar stringas ivestas yra skaicius
    print("ivesta neteisinga reiksme")
else: 
    skaicius1=float(skaicius1)

skaicius2=(input("iveskite antra skaiciu"))
skaicius2_svarus=skaicius2.replace("-","",1).replace(".","",1)
if skaicius2_svarus.isdigit()==False:
    print("ivesta neteisinga reiksme")
else: 
    skaicius1=float(skaicius2)

matematinis_veiksmas=input("iveskite matematini veiksma")
if matematinis_veiksmas!="+" or "-" or "/" or "*" or "**":
    print("netinkamas matematinis veiksmas")

#Skaiciavimai:

if matematinis_veiksmas=="+":
    print(f"rezultatas {skaicius1+skaicius2}")
elif matematinis_veiksmas=="-": 
    print(f"rezultatas {skaicius1-skaicius2}")
elif matematinis_veiksmas=="/" and (int(skaicius1)==0 or int(skaicius2)==0):
    print("klaida")   
elif matematinis_veiksmas=="/": 
    print(f"rezultatas {skaicius1/skaicius2}")
elif matematinis_veiksmas=="*": 
    print(f"rezultatas {skaicius1*skaicius2}")
elif matematinis_veiksmas=="**": 
    print(f"rezultatas {skaicius1**skaicius2}")



# ivestis=input(¨iveskite skaiciu")
#     print("visi yra skaiciai")
# if ivestis.isdigit():
#     print(visi yra skaiciai)
#     konvertuotas=int(ivestis)
# else:
#     print ("ivedei ne skaiciu")