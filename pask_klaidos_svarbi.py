# Uzduotele: Pakeisti 1 ir 3 uzduotis taip, kad neteisingai ivedus duomenis ar ivykus kalidoms, programos mestu norimas klaidas lietuviu kalba.
# 
# Motinines uzdoties salygos taikymas pirmai is triju uzduotelei:

# try:
#     numbers = [3, 1, 3, 2, 3, 4, 5]
#     target = 3
#     count = 0
#     for i in range(len(numbers)):
#         if numbers[i] == target:
#             count =+ 1  
#     print("The number " + target + " appears " + count + " times.")
# except TypeError:
#     print("isivele kintamojo tipo klaida")# isivele kintamojo tipo klaida 12 eiluteje, kur operacija galima tik su stringu 
# bet ne su intu. Galima sujungti-sudeti tik du stringus bet ne stringa su intu siuo atvekju.  

# Motinines uzdoties salygos taikymas antrai is triju uzduotelei:
# try:
#     list1 = [1, 2, 3]
#     list2 = [4, 5, 6]
#     merged = []
#     for i in range(len(list1)):
#         merged.append(list1[i])
#         merged.append(list2[i+1])
#     print("The merged list is: " + str(merged))
# except IndexError:
#     print("isivele indexavimo klaida")# isivele indexavimo klaida tipo klaida 24-oje eiluteje, kur 
#  merged.append(list2[i+1]) kodas kreipiasi i indeksa nr. 3 kai tuo tarpu kintamojo list2 indexas yra nuo 0 iki 2. 

# Motinines uzdoties salygos taikymas antrai is triju uzduotelei:
# try:
#     matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],[13, 14, 15, 16]]
#     border_sum = 0
#     for i in range(len(matrix)):
#         for j in range(len(matrix[0])):
#             if (i == 0 and i == len(matrix)-1) or (j == 0 and j == len(matrix[0])-1):
#                 border_sum += matrix[i][j]
#     print("The sum of the border elements is: " + border_sum)
# except TypeError:
#     print("isivele kintamojo tipo klaida")#paskutineje kodo eiluteje (38-oje) bandoma 
    # sudeti string su integeriu, kas yra neimanoma/neleistina.

# Uzduoties tikslas sukurti Sukurti programą, kuri 
# cikliškai prašo vartotojo įvesti sveikąjį skaičių, kol bus įvesta teisinga reikšmė.

# while True:
#     try:
#         ivestis=input("iveskite sveika skaiciu")
#         skaicius=int(ivestis)
#         if skaicius==10:
#             print("Bingo!")
#         else:
#             print("nepataiket su skaiciumi, bandykite dar karta")
#     except ValueError:
#         print("ivedete ne skaiciu, bandykite dar karta")      
#     finally: 
#         print("Bandymas baigtas")
    
# # Parasyti programa, kuri paprasys ivesti du skaicius(skaitikli ir vardikli) ir atliks dalijimo operacija.

# while True:
#     try:
#         ivestis1=input("ivesk skaitikli")
#         skaitiklis=float(ivestis1)
#         break#nulauzia cikla jei nera klaidos
#     except ValueError:
#         print("ivedei ne skaiciu, bandyk dar kateli")
# while True:
#     try:
#         ivestis2=input("ivesk vardikli")
#         vardiklis=float(ivestis2)
#         break
#     except ValueError:
#         print("ivedei ne skaiciu, bandyk dar kateli")
# # while True:
# #     try:
# #         if vardiklis==0:
# #             raise ZeroDivisionError("ivyko klaida, dalyba is nulio negalima")
# #         dalyba=skaitiklis/vardiklis
# #         print("rezultatats", dalyba)
# #         break
# #     except ZeroDivisionError as e:#pagaunama konkreti raise klaida uzkoduojama i e ir isprintinam zemiau
# #         print(e)
# #         break # uzdaromas while ciklas
# #     finally:
# #         print("skaiciavimas baigtas")
# #arba paskutinis blokas gali buti:
# try:
#     if vardiklis==0:
#        raise ZeroDivisionError("ivyko klaida, dalyba is nulio negalima") 
#     else:
#         print(f"rezultatas {skaitiklis/vardiklis}")
# except ZeroDivisionError as e:
#     print(e)
# finally:
#     print("skaiciavimas baigtas")

# Uzduotis Sukurti programą, kuri turi iš anksto apibrėžtą sąrašą 
# (pvz., vaisių sąrašą) ir paprašyti vartotojo įvesti indeksą, 
# kad būtų pasiektas atitinkamas sąrašo elementas.
# sarasas=["kiausiniai", "laikrastis", "lasiniai", "arielkos","silkutes", "desrytes"]

# while True:
#     try:
#         sarasoelementas=input("ivesk numeri is saraso jo turiniui gauti")
#         skaitiklis=int(sarasoelementas)
#         if skaitiklis<0:
#             raise ImportError ("neigiami indeksai neleidziami!")
#         if skaitiklis >0 and skaitiklis <=len(sarasas):
#             print(sarasas[skaitiklis])
#         else:
#             raise IndexError ("ivyko klaida, nurodyto saraso numerio nera")
#         break
#     except ValueError as eroras:
#         print("ivyko klaida, ivesk sveika skaiciu saraso numeriui gauti")
#     except IndexError as ineroras:
#         print (ineroras)
#     except ImportError as impoeror:
#         print (impoeror)
#     finally: 
#         print("viskas baigta, prisidirbai")
# 
# Uzduotele: Parašyti programą, kuri paprašys vartotojo įvesti datą formatu "YYYY-MM-DD" 
# ir bandys konvertuoti ją į datetime objektą.
# import datetime
# while True:
#     try:
#         vartdat=input("iveskite savo gimimo data siuo formatu YYYY-MM-DD")
#         year=vartdat[0:4] #issiemam inputo pozicijas atsakingas uz metus, ked veliau patikrinti ar skaiciai
#         month=vartdat[5:7] #issiemam inputo pozicijas atsakingas uz menesius, ked veliau patikrinti ar skaiciai
#         day=vartdat[8:10] #issiemam inputo pozicijas atsakingas uz dienas, ked veliau patikrinti ar skaiciai
#         int_year=int(year) # konvertuojam metus i integeri, kad veliau patikrinti ar tinkamai irasyta
#         int_month=int(month)# konvertuojam menesius i integeri, kad veliau patikrinti ar tinkamai irasyta
#         int_day=int(day)# konvertuojamn dienas i integeri, kad veliau patikrinti ar tinkamai irasyta
#         if len(vartdat) != 10 or vartdat[4] != '-' or vartdat[7] != '-'or year.isdigit()==False or month.isdigit()==False or day.isdigit()==False or int_year<1915 or int_year>2025 or int_month<1 or int_month>12 or int_day<1 or int_day>31:#cia tikrinam art inputo ilgis tesingas, ar bruksniai vietoj ir ar ivesti ti ksakitmenys
#             raise ValueError ("kokia cia nesamone ivedei?!")
#         dob=datetime.datetime.strptime(vartdat,"%Y-%m-%d")
#         print(dob)
#         break
#     except ValueError as nesamone:
#         print(nesamone)
#     finally:
#         print("datos patikrinimas baigtas")
 
# Uzduoetele:Sukurti programą su iš anksto apibrėžtu žodynu (pvz., šalių ir jų sostinių) ir paprašyti vartotojo įvesti raktą (šalies pavadinimą), kad gautų atitinkamą reikšmę.

# enciklopedija={"Lietuva": "Vilnius", "Prancūzija": "Paryžius", "Japonija": "Tokijas"}
# while True:
#     try:
#         uzklausa=input("iveskite salies pavadinima")
#         if len(uzklausa) == 0:
#             raise ValueError ("ivesk ka nors posimts kalakutu")
#         uzklausa=uzklausa.capitalize()# kapitalizuoju inputa jei kartais ivestas mazosiomis
#         miestas=enciklopedija[uzklausa]
#         # if miestas==None:#kadangi 
#         # CIA TOKI VARIANTA NAUDOCIAU JEI RAKTO IESKOCIAU SU GET IR TOKIO RAKTO NEBUTU IR GAUCIAU NE ERRORA OR NONE ATSAKYAM
#         #     raise KeyError("Tokios salies musu enciklopedijoje nera")
#         print("Jusu ieskomas miestas yra", miestas)
#         break
#     except ValueError as nulisakiu:
#         print(nulisakiu)
#     except KeyError:
#         print("Tokios salies musu enciklopedijoje nera")
#     finally:
#         print("Paieskos enciklopedijoje baigtos")

#Sunkioji uzduotis:Parašykite programą, kuri paprašys įvesti dvi datas formatu "YYYY-MM-DD" 
# (pradžios ir pabaigos datas) ir atliks šiuos veiksmus:

import datetime
try:
    while True:
        data1=input("iveskite prima data siuo formatu YYYY-MM-DD")
        data2=input("iveskite antraja data siuo formatu YYYY-MM-DD")
        if len(data1) and len(data2)!= 10 or data1[4] and data2[4] != '-' or data1[7] and data2[7] != '-':
            raise ValueError ("kokia cia nesamone ivedei?!")
        kondata1=datetime.datetime.strptime(data1,"%Y-%m-%d")
        kondata2=datetime.datetime.strptime(data2,"%Y-%m-%d")
        if kondata1<kondata2:
            raise ImportError ("antra data turi buti ankstesne uz pirmaja")
        break
except ValueError as neformatas:
    print(neformatas)
except ImportError as andata:
    print(andata)
finally:
    print("Datos ivedimo kosmaras baigtas")





