# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 21:13:05 2024

@author: nouba
"""
# Funksjon for å lese værdata fra fil og lagre i lister
def les_vaerdata(filnavn):
    datoer = []
    tider = []
    tid_siden_start = []
    trykk_barometer = []
    trykk_absolutt = []
    temperaturer = []

    # Åpne filen for lesing
    with open(filnavn, 'r') as fil:
        next(fil)
        for linje in fil:
            # Fjerner eventuelle ekstra mellomrom eller linjeskift
            linje = linje.strip()

            # Deler linjen basert på skilletegnet ";"
            dato_split = linje.split(" ")  #for datoformatet som bruker " " som skille            
            tid_split = linje.split(";")  #for tiden som bruker ":" som skille
            data = linje.split(";")        #for resten av dataene som bruker ";" som skille
            
            # Legg til data i de respektive listene
            datoer.append(data[0])           #første kolonne: datoer
            tider.append(data[1])                 #andre kolonne: tid
            tid_siden_start.append(data[2])         #tredje kolonne: tid siden start
            trykk_barometer.append(data[3])         #fjerde kolonne: trykk - barometer
            trykk_absolutt.append(data[4])              #femte kolonne: trykk - absolutt trykk maaler
            temperaturer.append(data[5:])    #sjette kolonne: temperatur (konverter til flyttall)

    return datoer, tider, tid_siden_start, trykk_barometer, trykk_absolutt, temperaturer

# Bruk funksjonen for å lese en fil
filnavn = 'trykk_og_temperaturlogg_rune_time.csv.txt'
datoer, tider, tid_siden_start, trykk_barometer, trykk_absolutt, temperaturer = les_vaerdata(filnavn)

#prøv å print ut en liste med kolonnenavn og radnummer
#print(datoer[12097])   #skille på ny datoformat går her, (12097)   
#print(tider[0:30])
print("dato:            ", datoer[2])
print("klokkeslett:     ", tider[2])
print("tid siden start: ", tid_siden_start[2])
print("trykk - barom.:  ", trykk_barometer[2])
print("trykk - absol.:  ", trykk_absolutt[2])
print("temperaturer:    ", temperaturer[2])

#print(f"Dato: {datoer[0:5]}", f"tider etter start: {tid_siden_start[0:5]}")

#hei på deg
