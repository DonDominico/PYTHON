# Uzduotis. Sukurti programą, kuri:
# •Sukurtų failą „Tekstas.txt“ su pilnu tekstu "Zen of Python".
# •Atspausdintų tekstą iš sukurto failo
# •Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką
# •Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).
# •Sukurtame faile eilutę "Beautifulis better than ugly." pakeistų į "Gražu yra geriau nei bjauru."
# •Atspausdintų visą failo tekstą atbulai
# •Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
# •Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS

# #*******************************************************PIRMOS UZDUOTIES "Zen of Python" PRADZIA******************************************

# import datetime
# import os

# laiks=datetime.datetime.today()

# #sukuriame textini failai ir irasome i ji Zen of Python
# with open("textfailz.txt",'w') as failas:
#     failas.write("""Zen of Python, by Tim Peters
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those! """)
#     failas.close()

# # with open("textfailz.py",'w') as failas:
# #     failas.write("Sveikas, pasauli!")
# #     failas.close()    

# # Perskaitom faila
# # with open("textfailz.txt",'r+') as failas:
# #     print(failas.read())

# # Idedam i faila sios dienos laika data etc. Laika paverciam i stringa, nes kitap neidesi. ir perskaitom ji nuo pradzios su seek(0). 

# with open("textfailz.txt",'a+') as failas:
#     failas.write("\n"+str(laiks))# Nurodom, kad laika kelsim i kita eilute. Laika paverciam i stringa, nes kitap neidesi.
#     failas.seek(0)#perskaitom ji nuo pradzios su seek(0).
#     print(failas.read())

# #Sunumeruojam eilutes faile:

# with open("textfailz.txt",'r+') as failas:
#     lines=failas.readlines() #perskaitome visas eilutes faile
#     failas.seek(0)#griztame i pradzia
#     for n, line in enumerate(lines, start=1):#uznumeruojam eilutes su enumerate comanda pradedant nuo pirmos eilutes
#         failas.write(f"{n}: {line}")#pridedame skaiciu prie kiekvienos eilutes faile(uzrasome)
#     failas.seek(0)#griztame i pradzia
#     print(failas.read())#perskaitome visa faila nuo pradzios. 

# #Sukurtame faile eilutę "Beautifulis better than ugly." pakeistų į "Gražu yra geriau nei bjauru."Padarome pokyti liste ir po to pakeiciam teksta siuo listu. 

# with open("textfailz.txt",'r+') as failas:
#     lines=failas.readlines() #pasiverciam eilutes faile/visa faila i lista
#     lines[1] ="2: Gražu yra geriau nei bjauru.\n"#pakeiciame antra eilute liste
#     failas.seek(0)#gristame i texto pradzia
#     failas.writelines(lines)#irasome i faila nauja eilute
#     failas.seek(0)#gristame i texto pradzia
#     print(failas.read())#atspausdiname updeitinta texta. 

# #Atspausdinti visa failo teksta atbulai. 

# with open("textfailz.txt",'r+') as failas:
#     lines=failas.readlines() #pasiverciam eilutes faile/visa faila i lista
#     new_lines=[line[::-1] for line in lines]# list comprehensionas atstojantis si cikla new_lines = [] for line in lines:new_lines.append(line[::-1])
#     failas.seek(0)#gristame i texto pradzia
#     failas.writelines(new_lines)#irasome i faila susikurta sarasa new_lines/tiksliau texta faile pakeiciam txtu(atvirsciu) sarase.
#     failas.seek(0)#gristame i texto pradzia
#     print(failas.read())#atspausdiname updeitinta texta. 

# #Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių

# stringeris="".join(lines)#paversta is teksto lista lines pasiverciam i stringa.Kad suskaiciuoti atskirus simbolius (skaicius, didziasias, mazasias)
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
    
# print(cymbolupaieska(stringeris,lines))

# #Nukopijuotų visą sukurto failą tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS

# uperlist=[]#sukuriame nauja lista su upper raidemis
# for u in lines:
#     uperlist.append(u.upper()) #sito list comprehension butu uperlist=[u.upper() for u in lines]

# uppertextas="".join(uperlist)#konvertuojame upper lista i stringa taip, kad nesitskirtu simboliu vieno nuo kito. 


# with open("kopija.txt",'a+') as kopija_failas:
#    kopija_failas.write(uppertextas)# Sukuriam nauja faila - kopija ir idedam auksciau susikurta str texta. 
#    kopija_failas.seek(0)#perskaitom ji nuo pradzios su seek(0).
#    print(kopija_failas.read())#isprintinam upper str texta naujajame sarase  - kopijoje

# *******************************************************PIRMOS UZDUOTIES "Zen of Python" PABAIGA******************************************


# *******************************************************ANTROS UZDUOTIES "PROGRAMA VARTOTOJUI FAILA SUKURTI" PRADZIA******************************************
# Sukurti programą, kuri:
# •Leistų vartotojui įvesti norimą eilučių kiekį
# •Įrašytų įvestą tekstą atskiromis eilutėmis į failą
# •Leistų vartotojui įrašyti norimą kuriamo failo pavadinimą

# Patarimai:
# •Sukurti while ciklą, kuris užsibaigtų tik įvedus vartotojui tuščią eilutę (nuspaudus ENTER)
# def didskaicius(xx):    

#     with open(xx+".txt",'w') as failas:

#         while True:
#             inputs=input("iveskite teskta naujai eilutei")
#             failas.write("\n"+inputs)
#             if inputs==(""):
#                 break

# def skaitfail(zzz):

#     with open(zzz+".txt",'r') as failas:
#         return (print(failas.read()))


# failopav=input("iveskite kaip norite pavadinti faila")

# didskaicius(failopav)

# skaitfail(failopav)

# def didskaicius(*arges):
    
#     maxskaicius=arges[0]

#     for num in arges:
#         if num>maxskaicius:
#             maxskaicius=num
#     return(maxskaicius)

# rezultatas=didskaicius(2,3,5,9,8,7)
# print(rezultatas)
    # lines=failas.readlines() #pasiverciam eilutes faile/visa faila i lista
    # lines[1] ="2: Gražu yra geriau nei bjauru.\n"#pakeiciame antra eilute liste
    # failas.seek(0)#gristame i texto pradzia
    # failas.writelines(lines)#irasome i faila nauja eilute
    # failas.seek(0)#gristame i texto pradzia
    # print(failas.read())#atspausdiname updeitinta texta. 


#  *******************************************************TRECIOS UZDUOTIES(katalogas+failas+sukurimo laikas) PRADZIA******************************************

# # Uzduotis: Sukurti programą, kuri:
# # •Kompiuterio darbalaukyje (Desktop) sukurtų katalogą „Naujas Katalogas“
# # •Šiame kataloge sukurtų tekstinį failą, kuriame būtų šiandienos data ir laikas
# # •Atspausdintų šio tekstinio failo sukūrimo datą ir dydį baitais
# import os
# # os.mkdir(r"C:\Users\lodor\Desktop\os_naujofailo_sukurimas_jo_vardo_ir_turinio_keitimas_skaitymas")
# import datetime 
# laikas=str(datetime.datetime.today())

# with open(r"C:\Users\lodor\Desktop\os_naujofailo_sukurimas_jo_vardo_ir_turinio_keitimas_skaitymas\data_laikas.txt",'a+') as datalaik_failas:
#    datalaik_failas.write("Sio tekstinio failo sukurimo data ir laikas:"+laikas)
#    datalaik_failas.seek(0)#perskaitom ji nuo pradzios su seek(0).
#    print(datalaik_failas.read())#isprintinam 

# bday=(os.stat(r"C:\Users\lodor\Desktop\os_naujofailo_sukurimas_jo_vardo_ir_turinio_keitimas_skaitymas\data_laikas.txt").st_birthtime)
# filebday=datetime.datetime.fromtimestamp(bday)
# bites=(os.stat(r"C:\Users\lodor\Desktop\os_naujofailo_sukurimas_jo_vardo_ir_turinio_keitimas_skaitymas\data_laikas.txt").st_size)
# bdaystr=str(filebday)
# bitstr=str(bites)

# with open(r"C:\Users\lodor\Desktop\os_naujofailo_sukurimas_jo_vardo_ir_turinio_keitimas_skaitymas\data_laikas.txt",'a+') as datalaik_failas:
#     datalaik_failas.write("\nSio tekstinio failo sukurimo data:"+bdaystr)
#     datalaik_failas.write("\nSio tekstinio failo dydis baitais:"+bitstr)
#     datalaik_failas.seek(0)
#     print(datalaik_failas.read())

#  *******************************************************TRECIOS UZDUOTIES(katalogas+failas+sukurimo laikas) PABAIGA******************************************