# numbers = [2, 4, 6, 8, 10]
# sum = 0
# for i in numbers:
#     sum = sum + i
# average = sum / len(numbers)
 
# print("The average is: ", average)

# numbers = [1, 2, 3, 4, 5, 6]
# for i in numbers:
#     if i % 2 == 0:
#         print(i)

#Find the maximum number.
# numbers = [45, 22, 89, 33, 72]
# max = 0
# for i in numbers:
#     if max < numbers[]:
#         max = i
# print("The maximum number is: ",i)
# pass

# Uzduotis sukurkite sarasa is keliu skirtingu tipu elementu, sukurkite cikla kuris paimtu visus skaicius (int ir float) ir isvestu ju suma
# sarasas=[45, "litras", 89.8, 33, True]

# suma=0

# for x in sarasas:
#     if type(x) is int or type(x) is float:
#         suma+=x
# print(suma)

# Uzduotis parasyti programa kuri leistu vartotojui ivesti sveika skaiciu, atspausdinti true jei skaicius teigiamas,
# atspausdinti false, jei skaicius neigiamas ar lygus 0 (True/false reikemsi isaugoti naudoti boolean tipo kintamaji ar_skaiciu_teigiamas)
# vartskaic=int(input("iveskite skaiciu posimts kalaklutu"))

# if vartskaic>0:
#     print(7!=0,"ivestas skaicius teigiamas")
# elif vartskaic<=0:
#      print(7==0,"ivestas skaicius neigiamas arba lygus 0")

# uzduotis parasyt prog. kuri atspausdintu dabartini data ir laika, atimtu is dabartines datos ir laiko 5 dienas ir juos atspausdintu, 
# pridetu prie dabartines datos ir laiko 8 valandas ir juos atspausdintu, 
# atspausdintu dabartini laika ir data tokiu formatu:2019 03 08, 09:57:17(naudojant datetime, timedelta(from datetime import timedelta=)

# #Atspausdinu dabartini data-laika:
import datetime
# siandatetaimas=datetime.datetime.today()
# print(siandatetaimas)
# #Atimti is dabartines datos ir laiko 5 dienas ir juos atspausdintu:
# print(siandatetaimas - datetime.timedelta(days=5))
# #Prideti prie dabartines datos ir laiko 8 valandas ir juos atspausdintu
# print(siandatetaimas - datetime.timedelta(hours=8))
# #Atspausdintu dabartini laika ir data tokiu formatu:2019 03 08, 09:57:17
# siandatetaimas=datetime.datetime(2019,3,8,9,57,17) 
# print(siandatetaimas)

# Uzduotis ivesti norima data ir laika (pvz. gimtadieni), 
# paskaiciuoti ir atspausditni kiek nuo ivestos datos ir laiko praejo:metu-menesiu-dienu-valandu-minuciu-sekundziu, 
# kadangi galima paskaiciuoti tik dienas ir sekundes, metus ir menesius paskaiciuokite apytiksliai 
# 
# (naudoti datetime, .days, what what bblabla.total_seconds() )

birvzday=input("iveskite savo gimimo data ir laika yyyy-mm-dd-hours-minutes-seconds")
print(birvzday)
sufbirvzdejus=datetime.datetime.strptime(birvzday, "%Y-%m-%d,%H:%M:%S")
pralekeslaikas=datetime.datetime.today()-sufbirvzdejus
print(pralekeslaikas,"praleke sitiek laiko")
#Paskaiciuoti kiek praejo metu
praejometu=pralekeslaikas.total_seconds()/31557600#pralekes laikas konvetuojamas i sskundes ir padalinamas is sekundziu metuose (aprox)
print(f"{round(praejometu)},praleke sitiek metu utatatata")#suapvalinamas rezultatas su round operacija
#Paskaiciuoti kiek praejo menesiu
praejomen=(praejometu*12)#apskaiciuotas skirtumas metais dauginamas is menesiu metuose ir suzinomas skirtumas dienomis
print(f"{round(praejomen)},praleke sitiek menesiu utatatata")#suapvalinamas rezultatas
#Kiek praejo dienu
dienu=pralekeslaikas.days
print("Praejo sitiek dienu",dienu)
#Kiek praejo valandu
valandu=pralekeslaikas.total_seconds()/60
print("Praejo sitiek valandu",valandu)
#Kiek praejo sekundeliu
sekundeliu=pralekeslaikas.total_seconds()
print(f"{round(sekundeliu)}, Praejo sitiek sekundziu")#vistiek suapvalinau, kad gautusi sveikas skaicius
