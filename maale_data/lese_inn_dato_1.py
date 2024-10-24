# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:34:02 2024

@author: nouba
"""
# =============================================================================
# importerer re, "regular expressions" (regulære uttrykk). 
# Den gir funksjonalitet for å arbeide med mønstergjenkjenning i tekst, slik 
# at du kan finne, matche, og manipulere tekst som følger spesifikke mønstre
# =============================================================================
# Definerer funksjon som leter og finner etter en viss type mønster. I denne
# spesifikke koden leter funksjonen etter typen DD.MM.ÅÅÅÅ
# =============================================================================
# =============================================================================

import re
from datetime import datetime

#mønsteret for dato av typen DD.MM.ÅÅÅÅ
dato_mønster = r'\b\d{2}\.\d{2}\.\d{4}\b'

dato_liste_1 = []

def finn_mønster_i_fil(filnavn, mønster):
    
    dato_liste_1 = []   # Initialiserer en tom liste for å lagre treffene
    
    # Åpner filen og leser linje for linje
    with open('trykk_og_temperaturlogg_rune_time.csv.txt', 'r') as fil:
        for linje in fil:
            # Finn alle forekomster av mønsteret i hver linje
            #treff = re.findall(mønster, linje)
            # Sjekk om linjen inneholder en dato og klokkeslett
            if re.match(mønster, linje):
                # Konverterer strengen til et datetime-objekt
                tidsdata = datetime.strptime(linje, '%d.%m.%Y %H:%M')
                dato_liste_1.append(tidsdata)
                
            # Hvis det er noen treff, legg dem til i listen
            #dato_liste_1.extend(treff)
    
    # Returnerer listen med alle treff
    return dato_liste_1

datoer_1 = finn_mønster_i_fil('trykk_og_temperaturlogg_rune_time.csv.txt', dato_mønster)

print(datoer_1)

