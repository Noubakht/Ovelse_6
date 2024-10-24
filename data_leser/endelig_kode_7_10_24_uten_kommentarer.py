# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 12:37:15 2024

@author: nouba
"""


from datetime import datetime
import matplotlib.pyplot as plt

# =============================================================================
# OPPGAVE D OG E (FIL NR. 1 (DEN LANGE FILA))
# =============================================================================

#filnavnet som skal leses
filnavn_1 = 'trykk_og_temperaturlogg_rune_time.csv.txt'

#funksjon som leser inn data fra 'filnavn'
def data_leser (filnavn):
    datoer = []
    tider = []
    dt_objekter_1 = []
    tid_siden_start = []
    trykk_bar = []
    trykk_abs = []
    temperatur = []
    
#åpner filen "filnavn_1" for lesing ("r") og konverterer til "utf-8" som er 
#standard for tekstfilbehandling, og kaller filen for "fil"
    with open(filnavn_1, 'r', encoding='utf-8') as fil:
        
#itererer gjennom hver "linje" i "fil" og lagrer data i de forskjellige listene 
        for linje in fil:
            #try, except for å håndtere når datoene skifter format
            try:
                data_deler = linje.strip().split(';') #Detaljert beskrivelse over
                dato_tid = datetime.strptime(data_deler[0], '%m.%d.%Y %H:%M')
                dt_objekter_1.append(dato_tid)     #Datetime objekter for plott?
                
                datoer.append(dato_tid.date())  #legger kun til dato(unødvendig?)
                tider.append(dato_tid.time())   #legger kun til tid(unødvendig?)
            except ValueError:
                continue   #fortsetter (hopper over) når datoene skifter format
                
            
            tid_siden_start.append(float(data_deler[1])) #beskrivelse over
            trykk_bar.append(data_deler[2])              #beskrivelse over
            trykk_abs.append(data_deler[3])              #beskrivelse over
            temperatur.append(data_deler[4])             #beskrivelse over
            

    return (datoer, tider, dt_objekter_1, 
            tid_siden_start, trykk_bar, trykk_abs, temperatur)

#Kaller på funksjonen data_leser med alle listenavnene slik at de fylles
(datoer, tider, dt_objekter_1, 
tid_siden_start, trykk_bar, 
trykk_abs, temperatur) = data_leser(filnavn_1)

#Endrer trykk barometer lista (ganger med 10 for å gjøre om til hPa)
for i in range(len(trykk_bar)):
    if trykk_bar[i]:    #sjekker om det er verdier der
        trykk_bar[i] = float(trykk_bar[i].replace(',', '.')) * 10
    else:               #hvis verdien er tom, sett det til None
        trykk_bar[i] = None

#Her har jeg driti meg ut og trodd at matplotlib godtar None. men det gjorde
#den ikke så jeg gidder ikke endre koden mer nå. bare legger til denne her
#for å fikse problemet       
trykk_bar_endret = []
tid_trykk_bar_endret = []

for i in range(len(trykk_bar)):
    if trykk_bar[i] is not None:  #Sjekker om verdien ikke er None
        trykk_bar_endret.append(trykk_bar[i])
        tid_trykk_bar_endret.append(dt_objekter_1[i])

#Endrer trykk absolutt lista (ganger med 10 for å gjøre om til hPa)
for i in range(len(trykk_abs)):
    if trykk_abs[i]:    #sjekke om det er verdier der
        trykk_abs[i] = float(trykk_abs[i].replace(',', '.')) * 10
    else:               #hvis verdien er tom, sett det til None
        trykk_abs[i] = None
        
#Endrer temperatur lista
for i in range(len(temperatur)):
    if temperatur[i]:   #sjekker om det er verdier der
        temperatur[i] = float(temperatur[i].replace(',', '.'))
    else:               #hvis verdien er tom, sett det til None
        temperatur[i] = None
        
        
# =============================================================================
# OPPGAVE D OG E. (FIL NR 2. (DEN KORTE FILA))
# =============================================================================

#filnavnet som skal leses
filnavn_2 = 'temperatur_trykk_met_samme_rune_time_datasett.csv.txt'

#funksjon som leser inn data fra 'filnavn'
def data_leser_2 (filnavn_2):

    datoer_2 = []
    tider_2 = []
    dt_objekter_2 = []
    temperatur_luft = []
    trykk_hav = []
    
#Åpner filen "filnavn" for lesing i utf-8 konvertert form    
    with open(filnavn_2, 'r', encoding='utf-8') as fil:
#Leser linje for linje og opretter datetime objekter og fyller tid og dato i
#hver sin liste. Fyller de andre to listene med relaterte data i strengformat
        for linje in fil:
            try:
                data_deler = linje.strip().split(';')
                dato_tid = datetime.strptime(data_deler[2], '%d.%m.%Y %H:%M')
                dt_objekter_2.append(dato_tid)
                datoer_2.append(dato_tid.date())    #bare datoen (Unødvendig?)
                tider_2.append(dato_tid.time())     #bare tiden (Unødvendig?)
            except ValueError: 
                continue
            
            temperatur_luft.append(data_deler[3])
            trykk_hav.append(data_deler[4])
        
    return datoer_2, tider_2, dt_objekter_2, temperatur_luft, trykk_hav

#Kaller på funksjonen og fyller listene
(datoer_2, tider_2, dt_objekter_2, 
temperatur_luft, trykk_hav) = data_leser_2(filnavn_2)


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
        
# =============================================================================
# OPPGAVE G) Gjennomsnittstemperatur fra den lange lista med data.
# =============================================================================

#Funksjon som regner gjennomsnittet på de 30 siste, gjeldende og 30 neste temp.
def gj_temp (gj_tider, gjennomsnitt_temp, n):
    gjennomsnitt_temp = []  #tom liste for gjennomsnittet som skal regnes ut
    gj_tider = []  #tom liste til tider som skal høre til gjennomsnittet


    for i in range(n, len(temperatur) - n):
        delta_temp = temperatur[(i-n) : (i + n + 1)]
        gjennomsnitt = sum(delta_temp)/len(delta_temp)
        
        gjennomsnitt_temp.append(gjennomsnitt)
        gj_tider.append(dt_objekter_1[i])
        
    return gj_tider, gjennomsnitt_temp

gj_tider, gjennomsnitt_temp = gj_temp(dt_objekter_1, temperatur, 30)

# =============================================================================
# OPPGAVE H (Temperaturfall mellom 11.06.21 kl 17:32 til 12.06.21 kl 03:05)
# =============================================================================

#funksjon for å beregne temperaturfallet
def temperaturfall(dt_objekter_1, temperatur):
    delta_temp = temperatur[4570] - temperatur[1128]
    delta_tid = (dt_objekter_1[4570] - dt_objekter_1[1128]).total_seconds()
    
    stigningstall = delta_temp / delta_tid  # Endring i temperatur per sekund
    
    #returner de to punktene og stigningstallet
    return (stigningstall, dt_objekter_1[1128], 
            temperatur[1128], dt_objekter_1[4570], temperatur[4570])

#indeks_1 = 1128  #indeks for starttid
#indeks_2 = 4570  #indeks for sluttid

(stigningstall, tid_start, temp_start,tid_slutt,
temp_slutt) = temperaturfall(dt_objekter_1, temperatur)

# =============================================================================
# ØVING 10 KOMMER UNDER HER. ALL NY KODE FOR ØVING 10 MÅ SKRIVES UNDER HER SÅ
# VI FÅR HOLDT OVERSIKTEN
# =============================================================================

# =============================================================================
# OPPGAVE A (Temperaturfall mellom 11.06.21 kl
# =============================================================================

#funksjon for temperaturfall i den korte fila
def temperaturfall_2(dt_objekter_2, temperatur_luft):
       
    delta_temp_2 = temperatur_luft[slutt] - temperatur_luft[start]
    delta_tid_2 = (dt_objekter_2[slutt] - dt_objekter_2[start]).total_seconds()
    
    stigningstall_2 = delta_temp_2 / delta_tid_2
    
    return (stigningstall_2, dt_objekter_2[start], temperatur_luft[start], 
            dt_objekter_2[slutt], temperatur_luft[slutt])

slutt = 26
start = 10

(stigningstall_2, tid_start_2, temp_start_2, tid_slutt_2, 
temp_slutt_2) = temperaturfall_2(dt_objekter_2, temperatur_luft)

print(temperatur_luft[start])
print(dt_objekter_2[start])

# =============================================================================
# ALL PLOTTING SKJER UNDER DENNE LINJA
# =============================================================================

fig, (akse1, akse2) = plt.subplots(2, 1, figsize=(12, 8))

# =============================================================================
# OPPGAVE I (plotting av lufttrykk,)
# =============================================================================

#x og y_koordinater for barometrisk og absolutt lufttrykk fra den lange fila
x_trykk_bar = tid_trykk_bar_endret
y_trykk_bar = trykk_bar_endret

x_trykk_abs = dt_objekter_1
y_trykk_abs = trykk_abs

#Plotting av barometrisk trykk (oransj graf)
akse2.plot(x_trykk_bar, y_trykk_bar, label="Barometrisk trykk", 
           color='orange', linewidth=0.5)
#Plotting av absolutt trykk (blå graf)
akse2.plot(x_trykk_abs, y_trykk_abs, label="Absolutt trykk", color='blue', 
           linewidth=0.5)

#x og y_koordinater for absolutt trykk MET fra den korte fila
x_lufttrykk_MET = dt_objekter_2
y_lufttrykk_MET = trykk_hav

#plotting av absolutt trykk MET (Grønn graf)
akse2.plot(x_lufttrykk_MET, y_lufttrykk_MET, label="Absolutt trykk MET",
           color='green', linewidth=0.5)

# =============================================================================
# OPPGAVE F (Plotting av temperaturer fra begge datafilene)
# =============================================================================

#x og y-koordinater til temperaturer fra lengste fil 
x_temperatur = dt_objekter_1
y_temperatur = temperatur

#x og y-koordinater til temperaturer fra korteste fil
x_temperatur_2 = dt_objekter_2
y_temperatur_2 = temperatur_luft

#Plotting av temperaturer fra den lengste fila (blå graf)
akse1.plot(x_temperatur, y_temperatur, label="Temperatur", color='blue', 
         linewidth=0.5)

#Plotting av temperaturer fra den korteste fila (grønn graf)
akse1.plot(x_temperatur_2, y_temperatur_2, label="Temperatur MET", color='green',
         linewidth=0.5)

# =============================================================================
# Plotting av gjennomsnittstemperatur fra oppgave G
# =============================================================================

#x og y-koordinater til gjennomsnittstemperaturen
x_gjennomsnitt_temp = gj_tider
y_gjennomsnitt_temp = gjennomsnitt_temp

#Plotting av gjennomsnittstemperaturen (oransj graf)
akse1.plot(x_gjennomsnitt_temp, y_gjennomsnitt_temp, 
           label="Gjennomsnittstemperatur", color='orange', linewidth=0.5)


# =============================================================================
# Plotting av temperaturfall fra oppgave H
# =============================================================================

#x og y-koordinater for temperaturfallet
x_temperaturfall = tid_start, tid_slutt
y_temperaturfall = temp_start, temp_slutt

#grafen som representerer temperaturfallet (rød graf, litt svak rødfarge)
akse1.plot(x_temperaturfall, y_temperaturfall, label="Temperaturfall", 
         color='red', linewidth=0.5)

# =============================================================================
# Plotting av temperaturfall 2 fra oppgave A - Øving 10
# =============================================================================
#x og y-koordinater for temperaturfall 2
x_temperaturfall = tid_start_2, tid_slutt_2
y_temperaturfall = temp_start_2, temp_slutt_2

#graf som representerer temperaturfallet (rød graf, litt svak farge)
akse1.plot(x_temperaturfall, y_temperaturfall, label="Temperaturfall Rune", 
         color='red', linewidth=0.5)


#plottemetoder for koordinatsystem med temperaturer
akse1.legend()
akse1.grid()

#plottemetoder for koordinatsystem med trykk
akse2.legend()
akse2.grid()

plt.plot()
plt.show()