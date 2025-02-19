#Provaloma uzduotele: Sukurti minibiudžeto programą, kuri:
# •Leistų vartotojui įvesti pajamas arba išlaidas (su "-" ženklu)
# •Pajamas ir išlaidas saugotų sąraše, o sąrašą pickle faile (uždarius programą, įvesti duomenys nedingtų)
# •Atvaizduotų jau įvestas pajamas ir išlaidas
# •Atvaizduotų įvestų pajamų ir išlaidų balansą (sudėtų visas pajamas ir išlaidas)
#  Patarimas:
# •importpickle

import pickle

#Pagrindinai programos kintamieji
ivesti_pajamas=1
Ivesti_islaidas=2
Atvaizduoti_ivestas_pajamas_islaidas=3
Atvaizduoti_ibalansa=4
iseiti_is_programos=5


with open("abc.pkl","rb") as pickle_3:
    a=pickle.load(pickle_3)
    b=pickle.load(pickle_3)
    c=pickle.load(pickle_3)

    Pajamos=a
    Islaidos=b

    # print(a)
    # print(b)
    # print(c)
# # # Funkcija pajamu ivedimas(pagal meniu 1):
def pajived(paj):
    Pajamos.append(paj)
    return(Pajamos)
# # # # Funkcija islaidu ivedimas(pagal meniu 2):
def islaidout(out):
    Islaidos.append(out)
    return(out)

# # # # # # # #Pickle sukurimas uzdarant programa funkcija
def uzseivinimas(bal):
    with open("abc.pkl","wb") as pickle_3:
        pickle.dump(Pajamos, pickle_3)
        pickle.dump(Islaidos, pickle_3)
        pickle.dump(bal, pickle_3)


    

# # # # Vartotojui pateikiamas programos/bibliotekos meniu
# # # # menu=("Programos meniu: \n 1. Ivesti pajamas \n 2. Ivesti islaidas \n 3. Atvaizduoti ivestas pajamas ir islaidas \n 4. Atvaizudoti balansa \n 5. Išeiti iš programos")
# # # # print(menu)
# # # # Atliekami programos veiksmai pagal vartotojo pageidavima
while True:
    try:
        pasirinkimas=input("pasirinkite norima veiksma ivesdami tinkamo saraso is meniu eiles numeri")
        if  pasirinkimas.isdigit()==False:
            raise ValueError ("iveskite skaiciu atstojanti meniu punkta")
        pasas=int(pasirinkimas)

        if pasas<1 or pasas > 5:
            raise NameError("pasirinkite norima veiksma ivesdami tinkamo saraso is meniu eiles numeri")
        elif pasas==1:#Ivesti pajamas
            incomas=float(input("iveskite pajamu suma"))
            # if pasirinkimas.isdigit()==False:
            #     raise NameError("Prasau ivesti pajamu suma, kaip skaiciu")
            pajived(incomas)
        elif pasas==2:#Ivesti islaidas
            minusas=float(input("iveskite islaidu suma"))
            # if pasas.isdigit()==False:
            #     raise IndexError("Prasau ivesti islaidu suma, kaip skaiciu")
            islaidout(minusas)

        elif pasas==3:#Gauti islaidu ir pajamu sarasa    
            islaidpaj=(f"Jusu pajamos {Pajamos}\nJusu islaidos {Islaidos}")
            print(islaidpaj)   
        elif pasas==4:#Gauti balansa
             balansas=(f"{sum(Pajamos)+sum(Islaidos)}")
             print("Esamas balansas", balansas)     
        elif pasas==5: 
            balansas=(f"{sum(Pajamos)+sum(Islaidos)}")
            uzseivinimas(balansas)
            print("Dekojame uz apsilnakyma musu banke, linkime nenuskursti") 
            break
    except AttributeError as letra:
        print(letra)
    except ValueError as badchoice:
        print (badchoice)
    except NameError as nn:
        print(nn)
    except IndexError as bn:
        print(bn)
    except:
        print("isivele klaida")




    
 