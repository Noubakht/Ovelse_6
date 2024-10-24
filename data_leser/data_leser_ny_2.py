# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 20:51:38 2024

@author: nouba
"""


from datetime import datetime

#filnavnet som skal leses
filnavn = 'temperatur_trykk_met_samme_rune_time_datasett.csv.txt'

#funksjon som leser inn data fra 'filnavn'
def data_leser_2 (filnavn):

    datoer_2 = []
    tider_2 = []
    dt_objekter_2 = []
    temperatur_luft = []
    trykk_hav = []
    
#Åpner filen "filnavn" for lesing i utf-8 konvertert form    
    with open(filnavn, 'r', encoding='utf-8') as fil:
#Leser linje for linje og opretter datetime objekter og fyller tid og dato i
#hver sin liste. Fyller de andre to listene med relaterte data i strengformat
        for linje in fil:
            try:
                data_deler = linje.strip().split(';')
                dato_tid = datetime.strptime(data_deler[2], '%d.%m.%Y %H:%M')
                dt_objekter_2.append(dato_tid)
                datoer_2.append(dato_tid.date())
                tider_2.append(dato_tid.time()) 
            except ValueError: 
                continue
            
            temperatur_luft.append(data_deler[3])
            trykk_hav.append(data_deler[4])
        
    return datoer_2, tider_2, dt_objekter_2, temperatur_luft, trykk_hav

#Kaller på funksjonen og fyller listene
datoer_2, tider_2, dt_objekter_2, temperatur_luft, trykk_hav = data_leser_2(filnavn)


#Gjør om verdiene i lufttemperatur til flyttall
for i in range (len(temperatur_luft)):
    if temperatur_luft[i]:
        temperatur_luft[i] = float(temperatur_luft[i].replace(',', '.'))
    else:
        temperatur_luft[i] = None
        
#Gjør om verdiene i lufttrykk i havnivå til flyttall
for i in range (len(trykk_hav)):
    if trykk_hav[i]:
        trykk_hav[i] = float(trykk_hav[i].replace(',', '.'))
    else:
        trykk_hav[i] = None
        
#Skriver ut prøve
for i in range (0, 7):
    print(f"INDEKS nr: {i}")
    print(f"dato:       {datoer_2[i]}")
    print(f"tid:        {tider_2[i]}")
    print(f"datetime:   {dt_objekter_2[i]}")
    print(f"lufttemp:   {temperatur_luft[i]}")
    print(f"trykk hav:  {trykk_hav[i]}")
    print("__________________________")