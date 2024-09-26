# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:34:02 2024

@author: nouba
"""
import re
from datetime import datetime

dato_mønster = r'\b\d{2}\.\d{2}\.\d{4}\b'

dato_liste_1 = []

def finn_mønster_i_fil(filnavn, mønster):
    # Initialiserer en tom liste for å lagre treffene
    dato_liste_1 = []
    
    # Åpner filen og leser linje for linje
    with open('trykk_og_temperaturlogg_rune_time.csv.txt', 'r') as fil:
        for linje in fil:
            # Finn alle forekomster av mønsteret i hver linje
            treff = re.findall(mønster, linje)
            
            # Hvis det er noen treff, legg dem til i listen
            dato_liste_1.extend(treff)
    
    # Returnerer listen med alle treff
    return dato_liste_1

datoer = finn_mønster_i_fil('trykk_og_temperaturlogg_rune_time.csv.txt', dato_mønster)
print(datoer)



dato_streng = 
dato_objekt = datetime.strptime(dato_streng, "%d-%m")

tid_streng = "14:30"
tid_objekt = datetime.strptime(tid_streng, "%H:%M")
print(tid_objekt)

print(dato_objekt)