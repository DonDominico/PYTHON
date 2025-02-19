# #OT PRATYBOS TAI JEGA DZIAUGIAS VISA LIETUVA,  BRASKA CIKLAI PO PRINTAIS NESUPRASI VAKARAIS

# #uzduoetrela Create a loop with a range statement, that prints out the numbers 1 to 6:
# # for x in range(1,7):
# #     print(x)
# #Task:Create a loop that prints out the letters A B C D E:

# # list=("A B C D E")

# # while True:
# #     print(list)
# # arba
# # for x in "ABCDE":
# #     print(x)

# #Uzduotele:Create a dictionary {"France": "Paris", "Japan": "Tokyo", "USA": "Washington DC"}, 
# # then create a loop that prints out the name of the countries, then another that prints out the names of the capital cities.
# # coutrcap={"France": "Paris", "Japan": "Tokyo", "USA": "Washington DC"}
# # print("Countries:")
# # for country in coutrcap.keys(): 
# #     print(country)
# # print(f"\nCapitals:")
# # for capital in coutrcap.values(): 
# #     print(capital)
# # Arba:
# # countries = {"France": "Paris", "Japan": "Tokyo", "USA": "Washington DC"}

# # for country in countries: #nenurodant per kur eina zodyno atveju atomatiskai eina per raktus
# #     print(country)

# # for country in countries:
# #     print(countries.get(country))#su get coutry komanda praso isprintinti raktu reiksmes

# #Uzduotele:Create a loop that iterates over the list [1, 10, 9, 4] and checks whether each number is greater than 3:
# # list=[1, 10, 9, 4]

# # for trys in list:
# #     if trys>3:
# #         print(trys,"greater than 3")
# #     else: 
# #         print(trys,"lesser than 3")

# #Arba
# # numbers = [1, 10, 9, 4]
  
# # for number in numbers:
# #     if number>3:
# #         print(number, "is greater than 3")

# # Uzduotela: Create a loop that iterates over the list ["France", "Japan", "the USA"] and searches for “the USA” in the list:

# # list=["France", "Japan", "the USA"]
# # for us in list:
# #     if us=="the USA":
# #         print("this is USA is in the list")
# #     else:
# #         print("esto no es ninguna USA")

# # Uzduotela:Create a loop that iterates over the list [-1, 2, 3, 0, -4] and checks whether each number is positive or negative:
# # list=[-1, 2, 3, 0, -4]
# # for posneg in list:
# #     if posneg>0:
# #         print(posneg,"is a positive number")
# #     elif posneg<0:
# #         print(posneg,"is a negetive number")
# #     else: 
# #         print(posneg, "ar tik nebus cia nulis zmogau")

# # Uzduotele Create code with a nested loop based on the list of lists [["apple", "orange"], ["carrot", "cabbage"], ["chicken", "beef"]]. f
# # foras eina per sarasa sarase (nestled loop)

# # lists=[["apple", "orange"], ["carrot", "cabbage"], ["chicken", "beef"]]
# # for listlist in lists:
# #     for item in listlist:
# #         print(item)

# # UUzduotele Create code with a nested loop based on the list of lists [["go", "went", "gone"], ["see", "saw", "seen"], ["take", "took", "taken"]] 

# # lists=[["go", "went", "gone"], ["see", "saw", "seen"], ["take", "took", "taken"]] 
# # 
# # for group in conjugations:
# #     print("The conjugations of ", group[0], " are:")
# #     for conjugation in group:
# #         print(conjugation)

# # Uzduotele Create code with a nested loop that searches the list of lists [[50, 48, -40], [57, 99, 80], [49, 40, 45]]
# #  and prints out all the numbers greater than or equal to 50:
# # list=[[50, 48, -40], [57, 99, 80], [49, 40, 45]]

# # for grand in list:
# #     for number in grand:
# #         if number >=50:
# #             print(number)

# # Uzduotele su while  Write a Python program 
# # that keeps asking the user for a number and stops when they enter 0

# # number=float(input("insert a number"))

# # while number!=0:
# #     print(number)

# # while True:
# #     number = int(input("Enter a number (enter 0 to stop): "))
# #     if number == 0:
# #         break    

# # Uzduotele. Write a Python program to find those numbers which are divisible by 7 and multiples of 5, between 1500 and 2700 (both included).

# # for x in range(1500,2701):
# #     if x%7==0:
# #         print("this number is divisible by 7", x)
# # for x in range(1500,2701):
# #     if x%5==0:
# #         print("this number is multiple of 5", x)

# # Uzduotis:  Write a Python program to guess a number between 1 and 9.
# # Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears again until the guess is correct, 
# # on successful guess, user will get a "Well guessed!" message, and the program will exit.



# # while True:
# #     userguess=int(input("pick a number"))
# #     if userguess in range(1,10):
# #         print("Well guessed mf!")
# #         break
# #     else:
# #         print("No luck this time mf")

# biblioteka=[{"Pavadinimas":"vytautas ir pimpackiukai","Metai":1999,"Zanras":"dokumentika"},{"Pavadinimas":"slibinas ir grazuole","Metai":2000,"Zanras":"romantika"},{"Pavadinimas":"cepelinai garaze","Metai":2020,"Zanras":"mokslas ir pazinimas"}]
# # naujaknyga=input("irasykite pridedamos knygos pavadinima")
# # metai=input("irasykite pridedamos knygos isleidimo metus")
# # zanras=input("irasykite pridedamos knygos zanra")
# # naujakn={"Pavadinimas":naujaknyga,"Metai":metai,"Zanras":zanras}
# # def nkivedimas(nk):
# #     biblioteka.append(nk)
# #     return(biblioteka)
# # nauajbib=nkivedimas(naujakn)
# # print(biblioteka)
# # irasas=input("irasykite ieskomos knygos pavadinima, zanra ar metus")
# # irasas=irasas.lower()
# # if irasas in biblioteka[0]:
# #     print("yes")
# # print(irasas)
# # print(biblioteka[0])
# # if irasas in biblioteka(0):
# #     print("Yes")
# # def paieska(pa):
# #     rezultatai=[]
# #     for value in biblioteka:
# #         rezultatai.append(value[pa])
# #         return(rezultatai)
# # paieska(irasas)

# # def get_value(listOfDicts, key):
# #     for subVal in listOfDicts:
# #         if key in subVal:
# #             return subVal[key]
# # get_value(biblioteka, irasas)
# # def kpaieska(ir):
# #     for knyga in biblioteka:
# #         if ir in knyga["Pavadinimas"]:
# #              print("paieskos rezulatatai", knyga)
# #              return(knyga)
# #         elif ir in knyga ["Zanras"]:
# #             print("paieskos rezulatatai", knyga)
# #             return(knyga)
# #         else:
# #              print("ivedete netesinga duomeni arba tokios knygos musu bibliotekoje nera")
# # kpaieska(irasas)

# # def ktrintis(lst):
# #     try:
# #         listas=[]
# #         for knyga in biblioteka:
# #             # listas=knyga
# #             if tr in knyga["Pavadinimas"]:
# #              print("Si knyga istrinta is bibliotekos:", knyga)
# #              return(knyga)
# #             else:
# #                 raise ValueError("ivedete netesinga duomeni arba tokios knygos musu bibliotekoje nera")
# #     except ValueError as ouch:
# #             print(ouch)
# #  rezultatas=argumentas*num

# # def inventorius():
# #     for knyga in biblioteka:
# #         rezultatas = biblioteka.index(knyga),knyga
# #         return(rezultatas)
# # inventorius()
# #         results.append(f"{argumentas} x {num} = {rezultatas}")#skaiciouoja kiekviena iteracija atskirai ir ja isreiskia sarase
# #     return results
# # #       print(f"{argumentas} x {num} = {rezultatas}")
# #     return(rezultatas)

# # def nkivedimas(nk):
# #     biblioteka.append(nk)
# #     return(biblioteka)
# # nauajbib=nkivedimas(naujakn)
# # print(biblioteka)

# # Write a Python program that asks the user to enter multiple students’ names and their corresponding test scores. The program should store the data in a dictionary and then use a loop 
# # to analyze and print out the following information:
# scorelist={"Steve":78, "John":69, "Vytold":55, "Ivan":59, "Aurimas":100}
# stname=input("students name")
# stscore=input("students score")
# scorelist[stname]=stscore
# for student in scorelist:
#     scorelist[student] = int(scorelist[student])
# maxvalue = list(scorelist.values())[0]
# for score in scorelist.values():
#     if score > maxvalue:
#         maxvalue=score
#         print(maxvalue)
# # Papildomos su funkcijom užduotys
# # Parašyk funkciją, kuri gauna sąrašą žodžių ir grąžina tik tuos žodžius, kurie yra ilgesni nei nurodytas ilgis.DONE
# zodziai=input("itrasykite savo zodzius")

# sarasas=zodziai.split()

# for n in sarasas:
#     if len(n)>5:
#         print(n)
 
# # Parašyk funkciją, kuri gauna du skaičius n ir m ir grąžina sumą visų skaičių nuo n iki m (įskaitant).DONE
# # Pvz., sekos_suma(3, 7) turėtų grąžinti 25 (3 + 4 + 5 + 6 + 7).DONE

# n=int(input("irasyk pirma skaiciu"))
# m=int(input("irasyk antra skaiciu"))
# sarasas=[]

# for g in range(n,m+1):
#     sarasas.append(g)
#     print(sum(sarasas))
 
# # Parašyk funkciją, kuri tikrina, ar žodis yra palindromas (tas pats skaitomas iš priekio ir iš galo).DONE
# # Pvz., ar_palindromas("savas") turėtų grąžinti True.DONE

# sarasas=["savas","meslas", "sigis", "Petras", "summus", "snobelis", "sunus", "varsketis" ]

# for palindromas in sarasas:
#     if palindromas==palindromas[::-1]:
#         print(palindromas)
 
# # Skaičių suma: Sukurkite funkciją, kuri priima sąrašą skaičių ir grąžina jų sumą. Panaudokite for ciklą.

skaiciai=input("Irasykite penkis skaitmenus")

sarasas=list(map(int, skaiciai))

for x in sarasas:
    print(sum(x)[0:])


 
# # Lyginių ir nelyginių skaičių atskyrimas: Sukurkite funkciją, kuri priima skaičių sąrašą ir grąžina du sąrašus: vieną su lyginiais, kitą su nelyginiais skaičiais.
 
# # Žodžių skaičius sakinyje: Parašykite funkciją, kuri priima sakinį ir grąžina žodžių skaičių jame.
 
# # Vardų klasifikacija: Sukurkite funkciją, kuri priima vardų sąrašą ir grąžina du sąrašus: vieną su vardais, kurie prasideda balsėmis, ir kitą su vardais, kurie prasideda priebalsėmis.
 
# # Sukurkite funkciją, kuri priima prekių žodyna su kainomis ir grąžina bendra sumą. Papildomai, jei bendra suma viršija 100€, suteikiama 10% nuolaida.
 



     