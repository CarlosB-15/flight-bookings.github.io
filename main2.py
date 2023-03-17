import sys
import time 

print('\nBenvenuto!\nSei un \"user\" o un \"admin\"? ', end='')
while True:
    utente = input()
    if utente.lower() == 'user' or utente.lower() == 'admin':
        break
    print('Inserire o \'user\' o \'admin\'')

# qui convertiamo il nostro database dei voli da stringa in dizionario
with open("database_voli.txt") as file:
    d = file.read()
    
# la funzione "eval()" permette di convertire una stringa nella rispettiva espressione in Python (nel nostro caso in un dizionario) 
database_voli = eval(d)

mesi = ['gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', \
            'dicembre']
giorni = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

if utente.lower() == 'user':

    # inserire dati biglietto con relative verifiche
    while True:
        partenza = input('Da dove desideri partire? (aeroporti disponibili: Napoli, Roma, Milano) ')
        partenza = partenza.lower()
        if partenza in ['napoli', 'roma', 'milano']:
            break 
        print('Inserire un aeroporto tra Napoli, Roma e Milano')
    
    while True:
        destinazione = input('Dove desideri arrivare? (aereoporti disponibili: Napoli, Roma, Milano) ')
        destinazione = destinazione.lower()
        if destinazione in ['napoli', 'roma', 'milano']:
            break 
        print('Inserire un aeroporto tra Napoli, Roma e Milano')
    
    while True:
        anno_partenza = int(input('In quale anno desideri partire? '))
        if anno_partenza >= 2023:
            break
        print('Anno errato!')
        continue
                    
    while True:
        mese_partenza = input('In quale mese desideri partire? ')
        mese_partenza = mese_partenza.lower()
        if mese_partenza in mesi:
            break 
        print('Mese errato!')
        
    while True:
        giorno_partenza = int(input('In quale giorno desideri partire? '))
        if mese_partenza == 'febbraio' and giorno_partenza in giorni and giorno_partenza in [giorni[-1], giorni[-2],giorni[-3]]:
            print('Giorno errato!')
            continue 
        elif mese_partenza in ['aprile', 'giugno', 'settembre', 'novembre'] and giorno_partenza in giorni and giorno_partenza == giorni[-1]:
            print('Giorno errato!')
            continue 
        elif giorno_partenza in giorni:
            break 
        print('Giorno errato!')  
        
    while True:
        anno_arrivo = int(input('In quale anno desideri arrivare? '))
        if anno_partenza > anno_arrivo:
            print('Anno errato!')
            continue
        if anno_arrivo >= 2023:
            break
        print('Anno errato!')  
        continue
            
    while True:
        mese_arrivo = input('In quale mese desideri arrivare? ')
        mese_arrivo = mese_arrivo.lower()
        if anno_partenza == anno_arrivo and mesi.index(mese_partenza) > mesi.index(mese_arrivo):
            print('Mese errato!')
            continue
        if mese_arrivo in mesi:
            break 
        print('Mese errato!')
        
    while True:
        giorno_arrivo = int(input('In quale giorno desideri arrivare? '))
        if mese_arrivo == 'febbraio' and giorno_arrivo in giorni and giorno_arrivo  in [giorni[-1], giorni[-2],giorni[-3]]:
            print('Giorno errato!')
            continue  
        elif mese_arrivo in ['aprile', 'giugno', 'settembre', 'novembre'] and giorno_arrivo in giorni and giorno_arrivo == giorni[-1]:
            print('Giorno errato!')
            continue  
        elif anno_partenza == anno_arrivo and mese_partenza == mese_arrivo and giorno_partenza > giorno_arrivo:
            print('Giorno errato!')
            continue
        elif giorno_arrivo in giorni:
            break 
        print('Giorno errato!')
        
    # Simulazione deposito con carte o Paypal (inserendo dati immaginari)
    print('\nPer garantire l\'acquisto dei biglietti E\' NECESSARIO effettuare un deposito nel nostro software.\n')
    print('\nMetodi di pagamento:\n1)Carta di credito/debito\n2)Paypal\n')
    while True:
        metodo_pagamento = int(input('\nCon quale metodo preferisci effettuare il deposito? 1/2 '))
        if metodo_pagamento in [1, 2]:
            break
        print('\nSelezionare 1 o 2')
        
    if metodo_pagamento == 1:
        print('\nHai scelto carta di credito/debito!')
        while True:
            numero = input('\nInserire numero della carta: ')
            numero_carta = ''
            cont = 0
            for i in numero:
                if cont % 4 == 0:
                    numero_carta += ' '
                    numero_carta += i
                else:
                    numero_carta += i
                cont += 1
            
            b = input(f'\nConfermi il numero della carta "{numero_carta}"? si/no ')
            if b == 'si':
                break
        
        codice = input('\nInserire codice di sicurezza: ')
    else:
        print('\nHai scelto Paypal!')
        while True:
            email = input('\nInserire email: ')
            b = input(f'\nConfermi la seguente email "{email}"? si/no ')  
            if b == 'si':
                break
    while True:
        saldo = int(input('Quanto desideri depositare sul conto? '))
        saldo_iniziale = saldo 
        b = input('\nConfermi? si/no ')
        if b == 'si':
            break
        
    print('\nAttendere...')
    time.sleep(3)
    print(f'Saldo aggiornato con successo!\nSaldo disponibile: {saldo} euro.')
    
    # ricerca voli disponibili andata
    print("\nI posti in prima classe costano il 30% in più rispetto al prezzo del biglietto.")

    print(f'\nI voli disponibili nel giorno {giorno_partenza}/{mese_partenza}/{anno_partenza} sono: ')
    
    if len(database_voli[partenza][destinazione][giorno_partenza]) == 0:
        print('Non ci sono voli disponibili per quel giorno, ricompilare il modulo')
        sys.exit()
        
    j = 1
    for i in database_voli[partenza][destinazione][giorno_partenza]:
        print(f'{j})Orario di partenza: {i[1]}, prezzo: {i[0]} euro, durata del volo: {i[2]}, compagnia: {i[3]}, posti disponibili in seconda classe {i[4]}, posti disponibili in prima classe {i[5]}')
        j+=1
        
    saldo_minimo = min(database_voli[partenza][destinazione][giorno_partenza])  
          
    # qui verifichiamo che il saldo sia sufficiente per acquistare un volo
    if saldo < saldo_minimo[0]:
        print('\nSaldo insufficiente. Non è possibile prenotare alcun biglietto. Ricompilare il modulo e depositare più soldi.')   
        sys.exit()    
        
    # controlli sulla scelta del biglietto         
    while True:
        numero_biglietto = int(input('\nQuale biglietto desideri acquistare? '))
        scelta_classe = int(input("Desideri viaggiare in prima o seconda classe (digitare 1 o 2): "))
        
        if database_voli[partenza][destinazione][giorno_partenza][numero_biglietto-1][0] > saldo:
            print('Saldo insufficiente per qualsiasi classe. Selezionare un nuovo volo.')
            continue
        
        if scelta_classe == 1:
            if database_voli[partenza][destinazione][giorno_partenza][numero_biglietto-1][5] == 0:
                print('Non ci sono posti disponibili in prima classe. Selezionare un nuovo volo.')
                continue
            
            prezzo_seconda_classe = database_voli[partenza][destinazione][giorno_partenza][numero_biglietto-1][0]
            prezzo_aggiunto = ((prezzo_seconda_classe * 30) / 100)
            prezzo_prima_classe =  prezzo_seconda_classe + prezzo_aggiunto
            
            if prezzo_prima_classe > saldo:
                print("Saldo insufficiente per la prima classe. Selezionare un nuovo volo.")
                continue
            
            database_voli[partenza][destinazione][giorno_partenza][numero_biglietto-1][0] = round(prezzo_prima_classe,2)
            saldo -= round(prezzo_prima_classe, 2)
            break
             
        if scelta_classe == 2:
            if database_voli[partenza][destinazione][giorno_partenza][numero_biglietto-1][4] == 0:
                print('Non ci sono posti disponibili in seconda classe. Selezionare un nuovo volo.')
                continue 
            saldo -= database_voli[partenza][destinazione][giorno_partenza][numero_biglietto-1][0]
            break
        
    biglietti = []
    biglietti.append([giorno_partenza, mese_partenza, anno_partenza,\
                      database_voli[partenza][destinazione][giorno_partenza][numero_biglietto-1], scelta_classe])
    
    # acquisto bagaglio 
    print('\nNel biglietto è previsto un bagaglio a mano, dal peso massimo di 7kg. Al prezzo di 50 euro è possibile aggiungere un bagaglio da imbarcare.')
    if saldo >= 50:
        bagaglio1 = input('\nAggiungere un bagaglio da imbarcare? si/no ')
        if bagaglio1 == 'si':
            saldo -= 50
            biglietti[0].append(bagaglio1)
            print('\nBagaglio aggiunto.')
        else:
            biglietti[0].append(bagaglio1)
    else:
        print('Saldo insufficiente. Non è possibile acquistare un bagaglio da imbarcare.')
        
        
    print(f'\nIl saldo aggiornato è {saldo} euro.')
    
    # ricerca voli disponibili ritorno
    if input('\nNel caso in cui si volesse acquistare anche il biglietto di ritorno si avrà uno sconto, sul secondo biglietto, del 10%!\
        \nDesideri acquistare anche il volo del ritorno? si/no ') == 'si':
    
        print("I posti in prima classe costano il 30% in più rispetto al prezzo del biglietto.")        

        print(f'\nI voli disponibili nel giorno {giorno_arrivo}/{mese_arrivo}/{anno_arrivo} sono: ')

        if len(database_voli[destinazione][partenza][giorno_arrivo]) == 0:
            print('Non ci sono voli disponibili per quel giorno, ricompilare il modulo')
            sys.exit()
            
        j = 1
        for i in database_voli[destinazione][partenza][giorno_arrivo]:
            print(f'{j})Orario di partenza: {i[1]}, prezzo: {i[0]} euro, durata del volo: {i[2]}, compagnia: {i[3]}, posti disponibili in seconda classe {i[4]}, posti disponibili in prima classe {i[5]}')
            j+=1
        
        saldo_minimo = min(database_voli[destinazione][partenza][giorno_arrivo])
        
        # qui verifichiamo che il saldo sia sufficiente per acquistare il volo del ritorno
        while True:
            if saldo < saldo_minimo[0]:
                print('\nSaldo insufficiente. Non è possibile prenotare alcun biglietto per il ritorno.')
                break
            else:
                # controlli sui posti e saldo disponibili
                numero_biglietto = int(input('\nQuale biglietto desideri acquistare? '))
                scelta_classe = int(input("Desideri viaggiare in prima o seconda classe (digitare 1 o 2): "))
                
                if database_voli[destinazione][partenza][giorno_arrivo][numero_biglietto-1][0] > saldo:
                    print('Saldo insufficiente per qualsiasi classe. Selezionare un nuovo volo.')
                    continue
                
                if scelta_classe == 1:
                    if database_voli[destinazione][partenza][giorno_arrivo][numero_biglietto-1][5] == 0:
                        print('Non ci sono posti disponibili in prima classe. Selezionare un nuovo volo.')
                        continue
                    
                    prezzo_seconda_classe = database_voli[destinazione][partenza][giorno_arrivo][numero_biglietto-1][0]
                    prezzo_aggiunto = (prezzo_seconda_classe * 30) / 100
                    prezzo_prima_classe =  prezzo_seconda_classe + prezzo_aggiunto
                    if prezzo_prima_classe > saldo:
                        print("Saldo insufficiente per la prima classe. Selezionare un nuovo volo.")
                        continue
                    
                    # applichiamo sconto sulla prima classe
                    sconto_biglietto = (prezzo_prima_classe * 10) / 100
                    database_voli[destinazione][partenza][giorno_arrivo][numero_biglietto-1][0] = round(prezzo_prima_classe - sconto_biglietto, 2)
                    biglietti.append([giorno_arrivo, mese_arrivo, anno_arrivo, \
                                      database_voli[destinazione][partenza][giorno_arrivo][numero_biglietto-1], scelta_classe])
                    
                if scelta_classe == 2:
                    if database_voli[destinazione][partenza][giorno_arrivo][numero_biglietto-1][4] == 0:
                        print('Non ci sono posti disponibili in seconda classe. Selezionare un nuovo volo.')
                        continue 
                    
                    # applichiamo sconto sulla seconda classe
                    sconto_biglietto = (database_voli[destinazione][partenza][giorno_arrivo][numero_biglietto-1][0] * 10) / 100
                    database_voli[destinazione][partenza][giorno_arrivo][numero_biglietto-1][0] -= sconto_biglietto
                    biglietti.append([giorno_arrivo, mese_arrivo, anno_arrivo,\
                      database_voli[destinazione][partenza][giorno_arrivo][numero_biglietto-1], scelta_classe])
                
                print(f'\nIl prezzo del volo scontato è {round(database_voli[destinazione][partenza][giorno_arrivo][numero_biglietto-1][0],2)} ')
                saldo = saldo - database_voli[destinazione][partenza][giorno_arrivo][numero_biglietto-1][0]
                print(f'\nIl saldo aggiornato è {saldo}.')
                
                # acquisto bagaglio
                print('\nNel biglietto è previsto un bagaglio a mano, dal peso massimo di 7kg. Al prezzo di 50 euro è possibile aggiungere un bagaglio da imbarcare.')
                if saldo >= 50:
                    bagaglio2 = input('\nAggiungere un bagaglio da imbarcare? si/no ')
                    if bagaglio2 == 'si':
                        saldo -=50
                        print('\nBagaglio aggiunto.')
                        biglietti[1].append(bagaglio2)
                    else:
                        biglietti[1].append(bagaglio2)
                else:
                    print('Saldo insufficiente. Non è possibile acquistare un bagaglio da imbarcare.')
                    
                break
            
    # procediamo con l'acquisto dei biglietti
    print('\nI biglietti selezionati sono: ')
    
    j = 1   
    for i in biglietti:
        print(f'\n{j})Giorno: {i[0]}, mese: {i[1]}, anno: {i[2]}, orario di partenza: {i[3][1]}, prezzo: {i[3][0]} euro, durata del volo: {i[3][2]}, compagnia: {i[3][3]}', end = ' ')
        if len(i) == 6:
            if i[5] == 'si':
                print('+ BAGAGLIO\n')
        j+=1
    
    while True:
        if len(biglietti) == 0:
            print('\nNessun biglietto selezionato, ricompilare il programma.')       
            sys.exit()
          
        if input('\nProcedere con l\'acquisto dei/del biglietto? si/no ') == 'si':
            
            # inseriamo dati personali 
            print("Inserire i dati personali. \n")
            nome = input('Inserire nome: ')
            cognome = input('Inserire cognome: ')
            
            while True:
                sesso = input('Inserire sesso (M o F): ')
                if sesso in ['M', 'F', 'm', 'f']:
                    break
                print('Errore ripetere!')
            
            data_nascita = input('Inserire data di nascita: ')
            luogo_nascita = input('Inserire il luogo di nascita: ')
            
            print(f'\nAttendere...')
            time.sleep(3)
            print('\nPrenotazione effettuata con successo.')
            
            # stampa biglietti
            print(f'\nL\'utente {nome} {cognome} nato a {luogo_nascita} il {data_nascita} ha acquistato i seguenti biglietti: ')
            j = 1
            for i in biglietti:
                print(f'\n{j})Giorno: {i[0]}, mese: {i[1]}, anno: {i[2]}, orario di partenza: {i[3][1]}, prezzo: {i[3][0]} euro, durata del volo: {i[3][2]}, compagnia: {i[3][3]}', end = ' ')
                if len(i) == 6:
                    if i[5] == 'si':
                        print('+ BAGAGLIO\n')
                j+=1
            print(f'\nSaldo finale {round(saldo,2)} euro.')
                        
            # aggiungiamo il/i volo/i pagato/i nel database
            with open('voli_prenotati.txt', 'a') as file:
                for i in biglietti:
                    if len(i) == 6:
                        file.write(f"\n{nome}, {cognome}, {partenza}, {destinazione}, {i[0]}, {i[3][0]}, {i[4]}, {i[1]}, {i[2]}, {i[3][1]}, {i[3][2]}, {i[3][3]}, {i[5]}")
                    else:
                        file.write(f"\n{nome}, {cognome}, {partenza}, {destinazione}, {i[0]}, {i[3][0]}, {i[4]}, {i[1]}, {i[2]}, {i[3][1]}, {i[3][2]}, {i[3][3]}, no")
                                    
            # verifica carta fedeltà
            b = input('\nPossiede una carta fedeltà? si/no ')
            
            if b == 'si':
                while True:
                    c = input('\nInserire codice carta fedeltà (5 cifre): ')
                    
                    # il programma accetterà qualsiasi inserimento, l'unica verifica è la lunghezza 
                    if len(c) < 5 or len(c) > 5:
                        print('Inserire codice corretto!')
                        continue
                    
                    print('\nAttendere...\n')
                    time.sleep(2)
                    
                    spesa_biglietti = 0
                    for i in biglietti:
                        spesa_biglietti += i[3][0]
                        
                    punti = int(spesa_biglietti * 100)
                    
                    print(f'\nCarta riconosciuta!\
                           \nOgni euro corrisponderà a 100 punti.\
                           \nIl prezzo dei biglietti acquistati verrà convertito in punti spendibili nei nostri aeroporti! \
                           \nSpesa totale: {spesa_biglietti}\
                           \nTotale punti accumulati: {punti}')
                    break
                
            print(f'\nGrazie di tutto. Arrivederci {nome} {cognome}!')
            sys.exit()
            
        else:
            if input('Desidera cancellare una prenotazione? si/no ') == 'si':
                print('Le sue prenotazioni: ')
                j = 1
                for i in biglietti:
                    print(f'\n{j})Giorno: {i[0]}, mese: {i[1]}, anno: {i[2]}, orario di partenza: {i[3][1]}, prezzo: {i[3][0]} euro, durata del volo: {i[3][2]}, compagnia: {i[3][3]}', end = ' ')
                    if len(i) == 6:
                        if i[5] == 'si':
                            print('+ BAGAGLIO\n')
                    j+=1
                a = int(input('\nQuale prenotazione desidera annullare? '))
                
                if len(biglietti[a-1]) == 6:
                    if biglietti[a-1][5] == 'si':
                        saldo += 50
                saldo += biglietti[a-1][3][0]
                biglietti.pop(a-1)
                
                print('\nAttendere...')
                time.sleep(2)
                print('\nPrenotazione rimossa con successo!')
    
    
else:
    while True:
        autenticazione = input('Inserire la password: ')
        if autenticazione == 'password':
            break 
        print('Password errata! Riprova')
    
    print('Benvenuto \'admin\'!')
    print('Cosa desideri fare? ')
    azione_admin = input('''-Digitare \'1\' per cancellare un volo\n-Digitare \'2\' per aggiungere un volo\n''')
    
    # azioni admin
    if azione_admin == '1':
        # dati da inserire
        while True:
            aeroporto_partenza = input('Inserire aeroporto di partenza: ')
            aeroporto_partenza = aeroporto_partenza.lower()
            if aeroporto_partenza in ['napoli', 'roma', 'milano']:
                break 
            print('Inserire un aeroporto tra Napoli, Roma e Milano')
        
        while True:
            aeroporto_arrivo = input('Inserire aeroporto di arrivo: ')
            aeroporto_arrivo = aeroporto_arrivo.lower()
            if aeroporto_arrivo in ['napoli', 'roma', 'milano']:
                break 
            print('Inserire un aeroporto tra Napoli, Roma e Milano')
        
        while True:
            anno = int(input('Inserire l\'anno: '))
            if anno >= 2023:
                break
            print('Anno errato!')
            continue
                        
        while True:
            mese = input('Inserire il mese: ')
            mese = mese.lower()
            if mese in mesi:
                break 
            print('Mese errato!')
            
        while True:
            giorno = int(input('Inserire il giorno: '))
            if mese == 'febbraio' and giorno in giorni and giorno in [giorni[-1], giorni[-2],giorni[-3]]:
                print('Giorno errato!')
                continue 
            elif mese in ['aprile', 'giugno', 'settembre', 'novembre'] and giorno in giorni and giorno == giorni[-1]:
                print('Giorno errato!')
                continue 
            elif giorno in giorni:
                break 
            print('Giorno errato!')  
            
        while True:  
            while database_voli[aeroporto_partenza][aeroporto_arrivo][giorno] == []:
                    print('Non ci sono voli disponibili per quel giorno, selezionare un giorno diverso')
                    giorno = int(input('Inserire un nuovo giorno: '))
                    continue
            
            print(f'\nVoli disponibili il {giorno} {mese} {anno} sono: ')
                
            j = 1
            for i in database_voli[aeroporto_partenza][aeroporto_arrivo][giorno]:
                print(f'{j})Orario di partenza: {i[1]}, prezzo: {i[0]} euro, durata del volo: {i[2]}, compagnia: {i[3]}, posti disponibili in seconda classe {i[4]}, posti disponibili in prima classe {i[5]}')
                j+=1
                    
            b = int(input('\nQuale volo desideri cancellare? '))
            
            # verifichiamo chi ha prenotato un volo nel giorno selezionato
            with open("voli_prenotati.txt") as file:
                voli_pren = file.readlines()
                
            prenotati = []
            
            for i in voli_pren:
                prenotati.append(i.split(", ")) 
            
            prenotati_da_rimborsare = []
            
            orario = database_voli[aeroporto_partenza][aeroporto_arrivo][giorno][b-1][1]
            
            for i in prenotati:
                if i[2] == aeroporto_partenza and i[3] == aeroporto_arrivo and int(i[4]) == giorno and i[7] == mese and int(i[8]) == anno and i[9] == orario:
                    prenotati_da_rimborsare.append(i)
            
            if len(prenotati_da_rimborsare) == 0:
                print('Non ci sono clienti da rimborsare.')
            else:
                # non c'è bisogno di controllare se sono in prima o seconda classe in quanto il prezzo è già modificato 
                # in base alla loro scelta
                print('\nI clienti da rimborsare sono:\n')
                for i in prenotati_da_rimborsare:
                    print(f'{i[0]} {i[1]}, {i[2]} -> {i[3]} il {i[4]}/{i[7]}/{i[8]}, prezzo: {i[5]}, bagaglio: {i[-1][:]}')
            
            # conferma cancellazione volo e quindi rimborso dei biglietti prenotati (nel caso in cui ci fossero)
            c = input(f'\nSicuro di voler cancellare il volo {b} e rimborsare gli eventuali clienti? si/no ')
            
            if c == 'si':
                print('\nOperazione in corso...')
                time.sleep(2)
                
                # rimborsiamo i clienti
                for i in prenotati_da_rimborsare:
                    soldi = int(i[5])
                    if i[-1][:-1] == 'si':
                        soldi += 50
                    print(f"\nAccreditati {soldi} euro sul conto di {i[0]} {i[1]}")
                    
                    # cancelliamoli dalla lista dei prenotati
                    for j in prenotati:
                        if i == j:
                            prenotati.remove(j)
                
                # cancelliamo il volo
                del database_voli[aeroporto_partenza][aeroporto_arrivo][giorno][b-1]
                
                # aggiorniamo il documento "voli_prenotati.txt"
                with open("voli_prenotati.txt","w") as file:
                    for i in prenotati:
                        file.write(", ".join(i))          
                
                print('\nOperazione completata!')
                
                
                print('\nI voli disponibile nel giorno selezionato, dopo l\'aggiornamento saranno: ')
                j = 1
                for i in database_voli[aeroporto_partenza][aeroporto_arrivo][giorno]:
                    print(f'{j})Orario di partenza: {i[1]}, prezzo: {i[0]} euro, durata del volo: {i[2]}, compagnia: {i[3]}, posti disponibili in seconda classe {i[4]}, posti disponibili in prima classe {i[5]}')
                    j+=1
                      
                # aggiorniamo database voli
                k = str(database_voli)
                with open("database_voli.txt", "w") as file:
                    file.write(k)
                    
                print('\nARRIVEDERCI!')
                break
            elif c == 'no':
                continue
    else:
        while True:                
            print('\nInserire i dati del nuovo biglietto')
            
            while True:
                nuovo_aeroporto_di_partenza = input('Inserire aeroporto di partenza: ')
                nuovo_aeroporto_di_partenza = nuovo_aeroporto_di_partenza.lower()
                if nuovo_aeroporto_di_partenza in ['napoli', 'roma', 'milano']:
                    break 
                print('Inserire un aeroporto tra Napoli, Roma e Milano')
            
            while True:
                nuovo_aeroporto_di_arrivo = input('Inserire aeroporto di arrivo: ')
                nuovo_aeroporto_di_arrivo = nuovo_aeroporto_di_arrivo.lower()
                if nuovo_aeroporto_di_arrivo in ['napoli', 'roma', 'milano']:
                    break 
                print('Inserire un aeroporto tra Napoli, Roma e Milano')
            
            while True:
                nuovo_anno = int(input('Inserire l\'anno: '))
                if nuovo_anno >= 2023:
                    break
                print('Anno errato!')
                continue
                            
            while True:
                nuovo_mese = input('Inserire il mese: ')
                nuovo_mese = nuovo_mese.lower()
                if nuovo_mese in mesi:
                    break 
                print('Mese errato!')
                
            while True:
                nuovo_giorno = int(input('Inserire il giorno: '))
                if nuovo_mese == 'febbraio' and nuovo_giorno in giorni and nuovo_giorno in [giorni[-1], giorni[-2],giorni[-3]]:
                    print('Giorno errato!')
                    continue 
                elif nuovo_mese in ['aprile', 'giugno', 'settembre', 'novembre'] and nuovo_giorno in giorni and nuovo_giorno == giorni[-1]:
                    print('Giorno errato!')
                    continue 
                elif nuovo_giorno in giorni:
                    break 
                print('Giorno errato!')  
            
            prezzo = int(input('\nInserire il prezzo del biglietto: '))
            orario_partenza = input('Inserire l\'orario di partenza: ')
            durata_volo = input('Inserire la durata del volo: ')
            compagnia_aera = input('Inserire la compagnia aerea o le compagnie aeree: ')
            nuovo_posti_seconda = int(input('Inserire il numero dei posti disponibili in seconda classe: '))
            nuovo_posti_prima = int(input('Inserire il numero dei posti disponibili in prima classe: '))
        
            d = input(f'\nAggiungere il seguente volo? Orario di partenza: {orario_partenza}, prezzo: {prezzo} euro, durata del volo: {durata_volo}, compagnia: {compagnia_aera}, posti disponibili seconda classe {nuovo_posti_seconda}, posti disponibili prima classe {nuovo_posti_prima} si/no ')
            
            if d == 'si':
                print('\nOperazione in corso...')
                database_voli[nuovo_aeroporto_di_partenza][nuovo_aeroporto_di_arrivo][nuovo_giorno].append([prezzo,orario_partenza,durata_volo,compagnia_aera, nuovo_posti_seconda, nuovo_posti_prima])
                time.sleep(2)
                print('\nOperazione riuscita!')
                
                # andiamo a modificare il database dei voli 
                l = str(database_voli)
                with open("database_voli.txt", "w") as file:
                    file.write(l)
            
                print('\nI voli disponibile nel giorno selezionato, dopo l\'aggiornamento saranno: ')
                    
                j = 1
                for i in database_voli[nuovo_aeroporto_di_partenza][nuovo_aeroporto_di_arrivo][nuovo_giorno]:
                    print(f'{j})Orario di partenza: {i[1]}, prezzo: {i[0]} euro, durata del volo: {i[2]}, compagnia: {i[3]}, posti disponibili in seconda classe {i[4]}, posti disponibili in prima classe {i[5]}')
                    j+=1
            else:
                continue
            
            f = input('Desideri aggiungere un nuovo volo? si/no ')
            if f =='si':
                continue
            else:
                print('\nARRIVEDERCI!')
                break