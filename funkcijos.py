# Uzduotis Gražinti trijų paduotų skaičių sumą.
# x=float(input("iveskite pirma skaiciu"))
# n=float(input("iveskite antra skaiciu"))
# y=float(input("iveskite trecia skaiciu"))
# def suskaiciuok(x,n,y):  
#     return (x+n+y)
# suma=suskaiciuok(x,n,y)
# print(suma)

# Uzduotis:Parašykite funkciją, 
# kuri priima vartotojo vardą ir spausdina sveikinimo žinutę, pvz., "Labas, Jonas!".
# def pasveikink(vardas):
#     print("Labas", vardas)
# pasveikink("Pablai")

# Uzduotis Parašyk funkciją, kuri tikrina, 
# ar duotas skaičius yra teigiamas, neigiamas, ar lygus nuliui.

# x=float(input("iveskite skaiciu"))
# def suskaiciuok(x):
#     if x >0:  
#         print ("jusu ivestas skaicius yra daugiau uz nuli")
#     if x<0: 
#         print ("jusu ivestas skaicius yra neigiamas")
#     if x==0: 
#         print ("jusu ivestas skaicius yra nulis")
# suskaiciuok(x)

# Uzduotis:Parašyk funkciją, kuri gauna sąrašą ir grąžina sąrašo elementų kiekį.

# def sarasiukas(vardas):
#     return(len(vardas))
# sarasas=sarasiukas([1,2,3,4,5])
# print(sarasas)

# Uzduotis:Gražintų paduoto sąrašo iš skaičių, sumą. 
# vartsar=input("ivesk skaiciu saraseli")
# sarasas=vartsar.split()
# print(sarasas)
# def sarasiukas(vardas):
#     total=0
#     for num in vardas:
#         total+=int(num)
#         print(total)
# sarasiukas(sarasas)# Kaip butu cia su return?

# Uzduotis: Sukurkite funkciją, 
# kuri priima skaičių sąrašą ir grąžina jų kvadratų sąrašą.

# def sarasiukas(vardas):
#     total=0
#     for num in vardas:
#         print(num ** 2)
#     return(num ** 2)
# sarselis=sarasiukas([1,2,3,4,5])
# print(sarselis)

# Uzduotis:
# Sukurk funkciją, kuri priima sąrašą skaičių ir grąžina 
# didžiausią skaičių tame sąraše.

# def sarasiukas(vardas):
#     max_value=vardas[0]
#     for num in vardas:
#         if num > max_value:
#             max_value=num
#     return(max_value)
# sarselis=sarasiukas([1,2,3,4,5])
# print(sarselis)

#Parašyk funkciją, kuri tikrina, 
# ar duotas skaičius yra lyginis ar nelyginis.

# x=int(input("iveskite sveika skaiciu"))
# def lygarne(argumentas):
#     if x%2==0:
#         return("jusu ivestas skaicius yra lyginis")
#     if x%2!=0:
#         return("jusu ivestas skaicius yra nelyginis")
# info=lygarne(x)
# print(info)

#Uzduotis Parašyk funkciją, kuri gauna skaičių n ir grąžina 
# n daugybos lentelę nuo 1 iki 10.
# x=int(input("iveskite sveika skaiciu"))
# def daugyba(argumentas):
#     # dauglent=[1,2,3,4,5,6,7,8,9,10]
#     for num in range(1,11):
#       rezultatas=argumentas*num
#       print(f"{argumentas} x {num} = {rezultatas}")
#     return(rezultatas)
# frtface=daugyba(x)
# print(frtface)
# reik patobulinti nes paskutinis rezultatas gaunasi 90
#arba
# Chat gpt variantas:
x = int(input("Iveskite sveika skaiciu: "))
def daugyba(argumentas):
    dauglent = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    results = []  # sarasas daygybos iteracijoms saugoti
    for num in dauglent:
        rezultatas = argumentas * num
        results.append(f"{argumentas} x {num} = {rezultatas}")#skaiciouoja kiekviena iteracija atskirai ir ja isreiskia sarase
    return results
multiplication_table = daugyba(x)
print(multiplication_table)


# Uzduotis:Sukurk funkciją, kuri pašalina 
# visus pasikartojančius elementus iš sąrašo. 
# (galite naudoti set, jeigu mokate)
# inputas=input("iveskite sarasa prekiu per kableli")
# inputclean=inputas.replace(",","")
# sarasas=inputclean.split()
# def sarasizmas(argumentas):
#     sarasascealn=set(argumentas)  
#     return(sarasascealn)
# svarussaraselis=sarasizmas(sarasas)
# print(svarussaraselis)

