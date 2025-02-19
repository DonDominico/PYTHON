# Uzduotis. Sukurkite Stačiakampio klasę ir suteikite jai sąvybes aukštis ir plotis ir sukurkite jam metodą Perimetras, 
# perimetro tikslas būtų grąžinti paskaičiuotą stačiakampio perimetrą ir tada jį atspausdinkite. Leiskite naudotojui įvesti plotį ir aukštį. 
# Daug tikrinimų daryti nereikia (ten ar tikrai skaičius ir ar toks stačiakampis yra įmanomas)

# Uzduotis, apskaiciuoti staciakampio perimetra.
# class forma:
#     def __init__(self,aukstis, plotis): # metodas yra tiesiog funkcija priklausanti klasei
#         self.aukstis = aukstis
#         self.plotis = plotis
#     def perimetras(self):
#         print(f"Perimetras: {self.aukstis  * self.plotis}")
 
# staciakampis = forma(50,70) 
# staciakampis.perimetras()

#****************************************UZDUOTIS PIRMA PRADZIA*******************************************************************8#

# Uzduotis:Parašyti klasę Sakinys, kuri turi savybę tekstas irmetodus,kurie:
# •Gražina tekstą atbulai
# •Gražina tekstą mažosiomis raidėmis
# •Gražina tekstą didžiosiomis raidėmis
# •Gražina žodį pagal nurodytą eilės numerį
# •Gražina, kiek teksteyranurodytų simbolių arba žodžių
# •Gražinatekstą su pakeistu nurodytu žodžiu arba simboliu
# •Atspausdina, kiek sakinyje yra žodžių,skaičių,didžiųjų ir mažųjų raidžių
# Susikurti kelis klasės objektus ir išbandyti visus metodus
# class Sakinys:#Klases sukurimas

#     def __init__(self,tekstas=("Bet kur visi 2000 mes lekiam, o kas atsakys Man")): 
# #Metodas sakinio atbulam uzrasymui
#         self.tekstas = tekstas
#     def atbulai(self):
#         return self.tekstas[::-1]
# #Metodas sakinio mažosiomis raidėmis uzrasymui
#     def mazom(self):
#         return self.tekstas.lower()
# #Metodas sakinioą didžiosiomis raidėmis grazinimui
#     def didz(self):
#         return self.tekstas.upper()
# #Metodas gražinti žodį pagal nurodytą eilės numerį
#     def rvieta(self):
#         listekstis=self.tekstas.split()
#         index=int(input("iveskite ieskomo elemento numeri"))
#         return listekstis[index]
# # Metodas žodžių skaiciui tekste nurodymui
#     def zodsk(self):
#         listekstis=self.tekstas.split()
#         zodziai=0
#         for zodis in listekstis:
#             if zodis.isdigit()==False:
#                 zodziai+=1
#         return (zodziai)
    
# #Metodas teikstui su pakeistu nurodytu žodžiu grazinti
#     def repl(self):
#         indexold=input("iveskite zodi kuri norite pakeisti")
#         indexnew=input("iveskite zodi kuri norite pakeisti")
#         return self.tekstas.replace(indexold,indexnew)
    
# #Metodas kiek sakinyje yra žodžių,skaičių,didžiųjų ir mažųjų raidžių atspausdinimui
#     def inventor(self):
#         listekstis=self.tekstas.split()
#         zodz_kiekis=0
#         didziosiosr=0
#         mazosiosr=0
#         skaiciai=0
#         for zodis in listekstis:
#             if zodis.isdigit()==False:
#                 zodz_kiekis+=1
#         for simbolis in self.tekstas:
#             if simbolis.isdigit():
#                 skaiciai+=1
#             if simbolis.isupper():
#              didziosiosr+=1
#             if simbolis.islower():
#                 mazosiosr+=1
#         rezultatas=(
#         f"Jusu irase tiek skaiciu: {skaiciai}\n"
#         f"Jusu irase tiek zodziu: {zodz_kiekis}\n"
#         f"Jusu irase tiek didziuju raidziu: {didziosiosr}\n"
#         f"ir jusu irase tiek mazuju raidziu: {mazosiosr}\n"
#     )
#         return (rezultatas)

# Metodas objekto sakinio atspausdinimui
    # def esybe(self):
    #   return self.tekstas


# #Objekto Zen sukurimas po klase Sakinys       
# Zen=Sakinys("Errors should never pass silently")
# Statistika=Sakinys("Buvo sunmaikinta 500 tanku, 300 belzabubu ir 3 lektuvai")
# Romantika=Sakinys("Ir kraupūs šešėliai atgal iš bedugnių užslinko.")
# Kurlekiam=Sakinys() # objektas naudojantis salygini klases argumenta - sakini. 

#Metodo atbulai iskvietimas ir pritaikykas objektams
# print(Zen.atbulai())
# print (Romantika.atbulai())
# print (Statistika.atbulai())
# print (Kurlekiam.atbulai())# objektas naudojantis salygini klases argumenta - sakini. 


# #Metodo sakinio mažosiomis raidėmis uzrasymui iskvietimas ir pritaikykas objektams
# print (Zen.mazom())
# print (Romantika.mazom())
# print (Statistika.mazom())
# print (Kurlekiam.mazom())# objektas naudojantis salygini klases argumenta - sakini. 

#Metodo sakinio didziosiomis raidėmis uzrasymui iskvietimas ir pritaikykas objektams
# print (Zen.didz())
# print (Romantika.didz())
# print (Statistika.didz())
# print (Kurlekiam.didz())# objektas naudojantis salygini klases argumenta - sakini. 

#Metodo žodzio pagal nurodytą eilės numerį gražinimui iskvietimas ir pritaikykas objektams
# print (Zen.rvieta())
# print (Romantika.rvieta())
# print (Statistika.rvieta())
# print (Kurlekiam.rvieta())# objektas naudojantis salygini klases argumenta - sakini. 

#Metodo žodziu suksiaciavimui sakinyje iskvietimas ir pritaikymas objektams
# print (Zen.zodsk())
# print (Romantika.zodsk())
# print (Statistika.zodsk())
# print (Kurlekiam.zodsk())# objektas naudojantis salygini klases argumenta - sakini. 

#Metodo žodziu pakeitimui sakinyje iskvietimas ir pritaikymas objektams
# print (Zen.repl())
# print (Romantika.repl())
# print (Statistika.repl())
# print (Kurlekiam.repl())# objektas naudojantis salygini klases argumenta - sakini. 

#Metodo Atspausdina, kiek sakinyje yra žodžių,skaičių,didžiųjų ir mažųjų raidžių iskvietimas ir taikymas objektams. 
# print (Zen.inventor())
# print (Romantika.inventor())
# print (Statistika.inventor())
# print (Kurlekiam.inventor())# objektas naudojantis salygini klases argumenta - sakini. 

# Metodo objekto sakinio atspausdinimui isbandymas
# print (Zen.esybe())
# print (Romantika.esybe())
# print (Statistika.esybe())
# print (Kurlekiam.esybe())# objektas naudojantis salygini klases argumenta - sakini. 

#****************************************UZDUOTIS PIRMA PABAIGA*********************************************************************

#****************************************UZDUOTIS ANTRA PRADZIA*********************************************************************
# Sukurti klasę Sukaktis, kuri turėtų savybę data (galima atskirai įvesti metus, mėnesius ir kt.) irmetodus,kurie:
# •Gražina, kiek nuo įvestos sukakties praėjo metų, savaičių, dienų, valandų, minučių, sekundžių
# •Gražina,ar nurodytos sukakties metai buvo keliamieji
# •Atima iš nurodytos datos nurodytą kiekį dienų ir gražina naują datą
# •Prideda prie nurodytos datos nurodytą kiekį dienų ir gražina naują datą
# Taip pat klases argumente taikos salyginis argumentas - užduotį taip, kad 
# jei kuriant objektą, nepaduodamas jokia data,veiksmai turi būti atliekami su programuotojo gimtadieniu


# import datetime
# prdob=("1980-03-29-17:03:29")
# defaultd=datetime.datetime.strptime(prdob, "%Y-%m-%d-%H:%M:%S")

# class Sukaktis:#Klases sukurimas
#     def __init__(self,data=defaultd): 
#         self.data = data
# #Metodas(laiko pralekimo skaiciukles) grazinti kiek nuo įvestos sukakties praėjo metų, savaičių, dienų, valandų, minučių, sekundžių
#     def skaiciuokle(self):
#         pralekeslaikas=datetime.datetime.today()-self.data
#         praejometu=pralekeslaikas.total_seconds()/31557600
#         praejomen=(praejometu*12)
#         dienu=pralekeslaikas.days
#         valandu=pralekeslaikas.total_seconds()/60
#         sekundeliu=pralekeslaikas.total_seconds()
#         return(f"{round(praejometu)},praleke sitiek metu utatatata,\n Praejo sitiek menesiu {round(praejomen)} \n Praejo sitiek dienu {dienu} \n Praejo sitiek valandu {round(valandu)} \n Praejo sitiek sekundziu{round(sekundeliu)}")

#Metodas patikrinti ar nurodyti metai buvo keliamieji 
    # def keltuvas(self):
    #     metai=self.data.year
    #     if (metai % 4 == 0 and metai % 100 != 0) or (metai % 400 ==0 ):  
    #         return("Jus gimete keliamaisiais metais")
    #     else:
    #         return("Jus gimete nekeliamaisiais metais")
        
# # Metodas atima iš nurodytos datos nurodytą kiekį dienų ir gražina naują datą
#     def atimtuvas(self): 
#         atimtidien=int(input("nurodykite skaiciumi kiek dienu norite atimti is sio piliecio gimtadienio"))
#         return(f"Stai kokia data iseina atemus jusu nurodytas dienas {self.data - datetime.timedelta(days=atimtidien)}")

# # Metodas pridedantis prie nurodytos datos nurodytą kiekį dienų ir gražina naują datą

#     def pridetuvas(self): 
#         atimtidien=int(input("nurodykite skaiciumi kiek dienu norite prideti prie sio piliecio gimtadienio"))
#         return(f"Stai kokia data iseina pridejus jusu nurodytas dienas {self.data + datetime.timedelta(days=atimtidien)}")

# Metodas objekto datos atspausdinimui
#     def esybe(self):
#       return self.data

# tadiena=input("iveskite savo gimimo data siuo formatu yyyy-mm-dd-hh:mm:ss")
# dob = datetime.datetime.strptime(tadiena, "%Y-%m-%d-%H:%M:%S") 

# Birvzday=Sukaktis(dob)#sukuriam Sukaktis klases objekta
# progdob=Sukaktis()#sukuriam Sukaktis klases objekta kuris naudos defaultine data-argumenta

#Pritaikome susikurtam objektui laiko pralekimo skaiciukles metoda
# print(Birvzday.skaiciuokle())
#print(progdob.skaiciuokle())#bandymas su objektu su defaultiniu argumentu

#Pritaikome keliamuju metu patikrinimo metoda objektui 
# print(Birvzday.keltuvas())
#print(progdob.keltuvas())#bandymas su objektu su defaultiniu argumentu

#Pritaikome dienu atimties moduli objektui 
# print(Birvzday.atimtuvas())
#print(progdob.atimtuvas())#bandymas su objektu su defaultiniu argumentu

#Pritaikome dienu prideties moduli objektui 
#print(Birvzday.pridetuvas())
#print(progdob.pridetuvas())#bandymas su objektu su defaultiniu argumentu

# Metodas objekto datos atspausdinimui
# print(Birvzday.esybe())
# print(progdob.esybe())#bandymas su objektu su defaultiniu argumentu

#****************************************UZDUOTIS ANTRA PABAIGA**************************************************************************


#****************************************UZDUOTIS TRECIA PRADZIA**************************************************************************

# Padarytiminibiudžetoprogramą, kuri:
# •Leistų vartotojui įvesti pajamas
# •Leistų vartotojui įvesti išlaidas
# •Leistų vartotojui parodyti pajamų/išlaidų balansą
# •Leistų vartotojui parodyti biudžeto ataskaitą (visus pajamų ir išlaidų įrašus su sumomis)
# •Leistų vartotojui išeiti iš programos
 
# Rekomendacija, kaip galima būtų padaryti:
# •Programa turi turėti klasę Irasas, kuri turėtų argumentus tipas (Pajamos arba Išlaidos) ir suma. Galima prirašyti str metodą, kuris gražintų, kaip bus atvaizduojamas spausdinamas objektas.
# •Programa turi turėti klasę Biudzetas, kurioje būtų:
# •Metodas init, kuriame sukurtas tuščias sąrašas zurnalas, į kurį bus dedami sukurti pajamų ir išlaidų objektai
# •Metodasprideti_pajamu_irasa(self, suma), kuris priimtų paduotą sumą, sukurtų pajamų objektą ir įdėtų jį į biudžeto žurnalą
# •Metodasprideti_islaidu_irasa(self, suma), kuris priimtų paduotą sumą, sukurtų išlaidų objektą ir įdėtų jį į biudžeto žurnalą
# •Metodasgauti_balansą(self), kuris gražintų žurnale laikomų pajamų ir išlaidų balansą.
# •Metodasparodyti_ataskaita(self), kuris atspausdintų visus pajamų ir išlaidų įrašus (nurodydamas kiekvieno įrašo tipą ir sumą).

#Pagrindinai programos kintamieji
ivesti_pajamas=1
Ivesti_islaidas=2
Atvaizduoti_ivestas_pajamas_islaidas_balansa=3
Atvaizduoti_ibalansa=4
iseiti_is_programos=5


#Funkcija pajamu-islaidu ivedimas(pagal meniu 1-2):

def paisived(paj):
    if paj>=0:
        Sarasas.pajamos.append(paj)
        return(Sarasas.pajamos)
    else:
        Sarasas.islaidos.append(paj)
        return(Sarasas.islaidos)
#Funkcija islaidu ivedimas(pagal meniu 2):

# def islaidout(out):
#     Sarasas.islaidos.append(out)
#     return(Sarasas.islaidos)

#Klase Irasas

class Biudzetas:#Klases sukurimas
    def __init__(self,pajamos, islaidos,  balansas): 
        self.islaidos = islaidos
        self.pajamos = pajamos
        self.balansas = balansas

#Metodas atspausdintų visus pajamų ir išlaidų įrašus (nurodydamas kiekvieno įrašo tipą ir sumą).
    def visiirasai(self): 

        print("Jusu pajamos:\n"+'\n'.join(str(x) for x in Bonketas.pajamos))
        print("Jusu islaidos: \n", '\n'.join(str(x) for x in Bonketas.islaidos))
        print("Jusu balansas:\n", '\n'.join(str(x) for x in Bonketas.balansas))

#Klase Biudzetas

class Irasas:#Klases sukurimas
    def __init__(self,pajamos, islaidos,  balansas): 
        self.islaidos = islaidos
        self.pajamos = pajamos
        self.balansas = balansas


Sarasas=Irasas([500,200,600,1000,115,899,777],[-577,-185,-690,-1009,-130,-800,-700],[0])#sukuriam Sukaktis klases objekta

Bonketas=Biudzetas(Sarasas.pajamos, Sarasas.islaidos, (f"{sum(Sarasas.pajamos)+sum(Sarasas.islaidos)}"))


# Vartotojui pateikiamas programos/bibliotekos meniu
menu=("Programos meniu: \n 1. Ivesti pajamas \n 2. Ivesti islaidas \n 3. Atvaizduoti ivestas pajamas ir islaidas \n 4. Atvaizudoti balansa \n 5. Išeiti iš programos")
print(menu)
# # Atliekami programos veiksmai pagal vartotojo pageidavima
while True:
    try:
        pasirinkimas=input("pasirinkite norima veiksma ivesdami tinkamo saraso is meniu eiles numeri")
        if  pasirinkimas.isdigit()==False:
            raise ValueError ("iveskite skaiciu atstojanti meniu punkta")
        pasas=int(pasirinkimas)

        if pasas<1 or pasas > 5:
            raise ValueError("pasirinkite norima veiksma ivesdami tinkamo saraso is meniu eiles numeri")
        elif pasas==1:#Ivesti pajamas
            incomas=float(input("iveskite pajamu suma"))
            paisived(incomas)
        elif pasas==2:#Ivesti islaidas
            minusas=float(input("iveskite islaidu suma"))
            paisived(minusas)

        elif pasas==3:#Gauti islaidu ir pajamu sarasa   
            Bonketas.visiirasai()
         
        elif pasas==4:#Gauti balansa
             balansas=(f"{sum(Bonketas.pajamos)+sum(Bonketas.islaidos)}")
             print("Esamas balansas", balansas)     
        elif pasas==5: 
            # balansas=(f"{sum(Pajamos)+sum(Islaidos)}")
            # uzseivinimas(balansas)
            print("Dekojame uz apsilnakyma musu banke, linkime nenuskursti") 
            break
    except ValueError as badchoice:
        print (badchoice)
    except:
        print("isivele klaida, gal ivedete texta vietoj skaiciaus?")


