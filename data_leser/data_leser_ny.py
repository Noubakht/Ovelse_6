# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 12:17:19 2024

@author: nouba
"""

# =============================================================================
# Her en en ny kode med kun det vi har lært i DAT120. ingen tilleggsbiblioteker 
# som i de to andre kodene. Jeg har skrevet en detaljert beskrivelse av to
# deler i koden som vi sleit med for å få til de to forrige kodene, og som gjorde
# at vi brukte csv biblioteket. Denne koden kan godt endres til å lese inn data
# fra den andre filen også.
# =============================================================================

from datetime import datetime

#filnavnet som skal leses
filnavn = 'trykk_og_temperaturlogg_rune_time.csv.txt'

#funksjon som leser inn data fra 'filnavn'
def data_leser (filnavn):
    datoer = []
    tider = []
    tid_siden_start = []
    trykk_bar = []
    trykk_abs = []
    temperatur = []

# =============================================================================
# DETALJERT BESKRIVELSE AV LISTEN "data_deler"
# =============================================================================
# Denne listen lagrer dataene og gjør to ting:
# linje.strip() fjerner tegn som mellomrom, linjeskift , tab osv. f.eks:
# "  123,3; 321;3234;  12\n" blir til '123,3;321;3234;12'
# split(';') deler strengen "linje" i deler ved å bruke ; som skilletegn. Så 
# hver gang det finnes en ; blir "linje" delt opp i en liste med alle 
# elementene som finnes i "linje". f.eks: '123,3;321;3234;12' blir til 
# ['123,3', '321', '3234', '12']
# =============================================================================
    
#åpner filen "filnavn" for lesing ("r") og konverterer til "utf-8" som er 
#standard for tekstfilbehandling, og kaller filen for "fil"
    with open(filnavn, 'r', encoding='utf-8') as fil:
        
#itererer gjennom hver "linje" i "fil" og lagrer data i de forskjellige listene 
        for linje in fil:
            #try, except for å håndtere når datoene skifter format
            try:
                data_deler = linje.strip().split(';') #Detaljert beskrivelse over
                dato_tid = datetime.strptime(data_deler[0], '%d.%m.%Y %H:%M')
                datoer.append(dato_tid.date())  #legger kun til dato
                tider.append(dato_tid.time())   #legger kun til tid
            except ValueError:
                continue   #fortsetter (hopper over) når datoene skifter format
            
# =============================================================================
# "Tid siden start" dataene har ingen komma i verdiene så konverterer firekte
# til flyttall når verdiene legges til i lista.
# =============================================================================
# Trykk barometer, trykk absolutt og temperatur har kommaer så de behandler jeg
# lenger nede i koden med en for-løkke og endrer verdiene til flyttall. 
# Foreløpig legger jeg bare de verdiene som er i hver "linje" inn i listene.
# En detaljert beskrivelse for endring til flyttall er gitt lenger ned.
# =============================================================================
            
            tid_siden_start.append(float(data_deler[1])) #beskrivelse over
            trykk_bar.append(data_deler[2])              #beskrivelse over
            trykk_abs.append(data_deler[3])              #beskrivelse over
            temperatur.append(data_deler[4])             #beskrivelse over
            

    return datoer, tider, tid_siden_start, trykk_bar, trykk_abs, temperatur

#Kaller på funksjonen data_leser med alle listenavnene slik at de fylles
datoer, tider, tid_siden_start, trykk_bar, trykk_abs, temperatur = data_leser(filnavn)

 
# =============================================================================
# Bruker en for-løkke og går igjennom (itererer) listene element for element.
# Sjekker om verdien i den relative indeksen [i] er tom (False) eller 
# ikke (True). Hvis verdien er gyldig (ikke tom), konverteres den fra en streng
# med komma som desimaltegn til et float ved å erstatte komma med punktum. 
# Hvis verdien er ugyldig (tom), konverteres den til None for å ikke få 
# problemer senere når vi skal plotte verdiene inn i grafer. 
# Resultat: listen oppdateres med flyttallsverdier eller None for tomme verdier
# =============================================================================

#Endrer trykk barometer lista
for i in range(len(trykk_bar)):
    if trykk_bar[i]:    #sjekker om det er verdier der
        trykk_bar[i] = float(trykk_bar[i].replace(',', '.'))
    else:               #hvis verdien er tom, sett det til None
        trykk_bar[i] = None

#Endrer trykk absolutt lista
for i in range(len(trykk_abs)):
    if trykk_abs[i]:    #sjekke om det er verdier der
        trykk_abs[i] = float(trykk_abs[i].replace(',', '.'))
    else:               #hvis verdien er tom, sett det til None
        trykk_abs[i] = None
        
#Endrer temperatur lista
for i in range(len(temperatur)):
    if temperatur[i]:   #sjekker om det er verdier der
        temperatur[i] = float(temperatur[i].replace(',', '.'))
    else:               #hvis verdien er tom, sett det til None
        temperatur[i] = None
        
#Skriv ut en prøve
for i in range (0, 7):
    print(f"INDEKS nr. {i}:")
    print(f"dato:        {datoer[i]}")
    print(f"tider:       {tider[i]}")
    print(f"tid siden s: {tid_siden_start[i]}")
    print(f"trykk bar:   {trykk_bar[i]}")
    print(f"trykk abs:   {trykk_abs[i]}")
    print(f"temperatur:  {temperatur[i]}")
    print("______________________________")