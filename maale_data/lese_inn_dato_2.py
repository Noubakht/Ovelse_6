# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 19:34:02 2024

@author: nouba
"""
import re

dato_monster = r'\b\d{2}\.\d{2}\.\d{4}\b'
tid_monster = r'\b\d{2}\.\d{2}\b'

def finn_monster_i_fil(filnavn, monster):
    #lager en tom liste for å lagre treffene
    dato_liste_1 = []
    tid_liste_1 = []
    # Åpner filen og leser linje for linje
    with open('trykk_og_temperaturlogg_rune_time.csv.txt', 'r') as fil:
        for linje in fil:
            #finner alle forekomster av monsteret i hver linje
            treff = re.findall(monster, linje)
            
            
            # Hvis det er noen treff, legg dem til i listen
            dato_liste_1.append(treff([0]))
    
    # Returnerer listen med alle treff
    return dato_liste_1, tid_liste_1

dato_liste_1 = finn_monster_i_fil('trykk_og_temperaturlogg_rune_time.csv.txt', dato_monster)
#tid_liste_1 = finn_monster_i_fil('trykk_og_temperaturlogg_rune_time.csv.txt', tid_monster)

print(dato_liste_1[0:1])
#print(tid_liste_1[0:1])


