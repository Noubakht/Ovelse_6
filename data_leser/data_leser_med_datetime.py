# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:16:11 2024

@author: nouba
"""
# =============================================================================
# bruker csv-biblioteket i python for å gjøre lesing av datafilene enklere. 
# Fra google: csv-biblioteket i Python brukes til å lese fra og skrive til 
# CSV-filer (Comma-Separated Values), som er en vanlig filtype for lagring av
# tabulær data i et tekstformat. I stedet for å bruke kommandoer for å manuelt
# gå gjennom en CSV-fil, forenkler csv-biblioteket denne prosessen ved å gi 
# verktøy for enkel lesing og skriving av strukturerte data.
# =============================================================================
# =============================================================================
# importerer datetime også for å gjøre om dato og tid til datetime objekter, 
# for å kunne plotte. matplotlib godtar datetime objekter. Senere deler også
# tiden og datoen i hver sin liste med .date() og .time()
# =============================================================================
# =============================================================================
# alle andre data bortsett fra tid og dato gjøres om til float for å kunne 
# plotte i matplotlib. der det ikke finnes data bruker jeg NONE for å fylle
# de tomme cellene med "ingenting" slik at matplotlib godtar dette. Hvis en tom
# celle ikke er NONE klarer ikke matplotlib å hoppe over disse
# =============================================================================

import csv
from datetime import datetime

#definerer en funksjon for å lese filen med data og lagre de i lister
def les_data(filnavn):
    datoer = []
    tider = []
    tid_siden_start = []
    trykk_barometer = []
    trykk_absolutt = []
    temperatur = []
    
    #åpner filen for lesing og bruker csv.reader til å lese gjennom fila og
    #skille mellom dataene med semikolon
    with open(filnavn, 'r', encoding='utf-8') as fil:
        fil = csv.reader(fil, delimiter=';')
        next(fil)  #hopp over første linje
        
        for linje in fil:
            #håndtering av dato og tid med datetime. Har med exceptions for at
            #det ikke skal krasje når datoformat endres
            try:
                #deler dato og tid i separate datetime-objekter
                dato_tid = datetime.strptime(linje[0], '%m.%d.%Y %H:%M')
                datoer.append(dato_tid.date())  #lagrer bare datoen
                tider.append(dato_tid.time())  #lagrer bare tiden
            except ValueError:
                continue  #hopp over linjer med ugyldige datoformat (dd/mm/yyyy)

            #sjekker om det finnes en verdi i "linje" (2. og 3. kolonne) 
            #hvis ja, konverter til flyttal og legg til listen "tid_siden_start" 
            #hvis nei, (tom celle), legg "None" til listen i stedet.
            tid_siden_start.append(float(linje[1]) if linje[1] else None)
            trykk_barometer.append(float(linje[2].replace(',', '.')) if linje[2] else None)
            trykk_absolutt.append(float(linje[3].replace(',', '.')))
            temperatur.append(float(linje[4].replace(',', '.')))

    return datoer, tider, tid_siden_start, trykk_barometer, trykk_absolutt, temperatur

# Bruk funksjonen til å lese inn data fra en fil
filnavn = 'trykk_og_temperaturlogg_rune_time.csv.txt'
datoer, tider, tid_siden_start, trykk_barometer, trykk_absolutt, temperatur = les_data(filnavn)

#skriver ut en prøve av hver indeks i listene under hverandre
for i in range(0, 11):
    print(f"Dato:       {datoer[i]}")
    print(f"Tid:        {tider[i]}")
    print(f"tid s.s.:   {tid_siden_start[i]}") 
    print(f"trykk bar.: {trykk_barometer[i]}")
    print(f"Trykk abs.: {trykk_absolutt[i]}") 
    print(f"Temp. :     {temperatur[i]}")
    print("__________________________________")
    
#skriver ut verdiene i listene ved siden av hverandre    
for i in range(0, 11):
    print(f"dato: {datoer[i]} tid: {tider[i]} tid s: {tid_siden_start[i]} "
          f"trykk b: {trykk_barometer[i]} trykk a:{trykk_absolutt[i]} temp: {temperatur[i]}" )