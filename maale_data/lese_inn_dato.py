#Denne funksjonen leser inn datoen fra målingene i datafilene

filnavn = "temperatur_trykk_met_samme_rune_time_datasett.csv.txt"
dato_monster = r'\b\d{2}\.\d{2}\.\d{4}\b'


def les_inn_dato():
    
    dato_liste = list()
    
    with open(filnavn, 'r') as fila: 
        for linje in fila:
            if linje.find(dato_monster):
                dato_liste.append(dato)
                