import partenze
import sys
import time 

print('\nBenvenuto!\nSei un \"user\" o un \"admin\"? ', end='')
while True:
    utente = input()
    if utente.lower() == 'user' or utente.lower() == 'admin':
        break
    print('Inserire o \'user\' o \'admin\'')

if utente.lower() == 'user':
    
    mesi = ['gennaio', 'febbraio', 'marzo', 'aprile', 'maggio', 'giugno', 'luglio', 'agosto', 'settembre', 'ottobre', 'novembre', 'dicembre']
    giorni = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    
    
    # inseriamo dati utente
    nome = input('Inserire nome: ')
    cognome = input('Inserire cognome: ')
    sesso = input('Inserire sesso: ')
    data_nascita = input('Inserire data di nascita: ')
    luogo_nascita = input('Inserire il luogo di nascita: ')

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
        mese_partenza = input('In quale mese desideri partire? ')
        mese_partenza = mese_partenza.lower()
        if mese_partenza in mesi:
            break 
        print('Mese errato!')
        
    while True:
        mese_arrivo = input('In quale mese desideri arrivare? ')
        mese_arrivo = mese_arrivo.lower()
        if mese_arrivo in mesi:
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
        giorno_arrivo = int(input('In quale giorno desideri arrivare? '))
        if mese_arrivo == 'febbraio' and giorno_arrivo in giorni and giorno_arrivo  in [giorni[-1], giorni[-2],giorni[-3]]:
            print('Giorno errato!')
            continue  
        elif mese_arrivo in ['aprile', 'giugno', 'settembre', 'novembre'] and giorno_arrivo in giorni and giorno_arrivo == giorni[-1]:
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
    print(f'\nI voli disponibili nel giorno {giorno_partenza} {mese_partenza} sono: ')
    
    if len(partenze.partenze[partenza][destinazione][giorno_partenza]) == 0:
        print('Non ci sono voli disponibili per quel giorno, ricompilare il modulo')
        sys.exit()
        
    j = 1
    for i in partenze.partenze[partenza][destinazione][giorno_partenza]:
        print(f'{j})Orario di partenza: {i[1]}, prezzo: {i[0]} euro, durata del volo: {i[2]}, compagnia: {i[3]}')
        j+=1
        
    saldo_minimo = min(partenze.partenze[destinazione][partenza][giorno_partenza])  
          
    # qui verifichiamo che il saldo sia sufficiente per acquistare un volo
    if saldo < saldo_minimo[0]:
        print('\nSaldo insufficiente. Non è possibile prenotare alcun biglietto. Ricompilare il modulo e depositare più soldi.')   
        sys.exit()
        
    print('\nQuale biglietto desideri acquistare? ', end= ' ')
    
    # controllo saldo         
    while True:
        numero_biglietto = int(input())
        if partenze.partenze[partenza][destinazione][giorno_partenza][numero_biglietto-1][0] <= saldo:
            break
        print('Saldo insufficiente. Selezionare un nuovo volo.')
    
    saldo -= partenze.partenze[partenza][destinazione][giorno_partenza][numero_biglietto-1][0] 
    
    biglietti = []
    biglietti.append([giorno_partenza, partenze.partenze[partenza][destinazione][giorno_partenza][numero_biglietto-1]])
    
    # acquisto bagaglio 
    print('\nNel biglietto è previsto un bagaglio a mano, dal peso massimo di 7kg. Al prezzo di 50 euro è possibile aggiungere un bagaglio da imbarcare.')
    if saldo >= 50:
        bagaglio1 = input('\nAggiungere un bagaglio da imbarcare? si/no ')
        if bagaglio1 == 'si':
            saldo -=50
            biglietti[0].append(bagaglio1)
            print('\nBagaglio aggiunto.')
        else:
            biglietti[0].append(bagaglio1)
    else:
        print('Saldo insufficiente. Non è possibile acquistare un bagaglio da imbarcare.')
        
        
    print(f'\nIl saldo aggiornato è {saldo} euro.')
    
    # ricerca voli disponibili ritorno
    if input('\nNel caso in cui si volesse acquistare anche il biglietto di ritorno si avrà uno sconto, sul secondo biglietto, del 30%!\
        \nDesideri acquistare anche il volo del ritorno? si/no ') == 'si':
    
        print(f'\nI voli disponibili il giorno {giorno_arrivo} sono: ')

        if len(partenze.partenze[destinazione][partenza][giorno_arrivo]) == 0:
            print('Non ci sono voli disponibili per quel giorno, ricompilare il modulo')
            sys.exit()
            
        j = 1
        for i in partenze.partenze[destinazione][partenza][giorno_arrivo]:
            print(f'{j})Orario di partenza: {i[1]}, prezzo: {i[0]} euro, durata del volo: {i[2]}, compagnia: {i[3]}')
            j+=1
        
        saldo_minimo = min(partenze.partenze[destinazione][partenza][giorno_arrivo])
        
        # qui verifichiamo che il saldo sia sufficiente per acquistare il volo del ritorno
        while True:
            if saldo < saldo_minimo[0]:
                print('\nSaldo insufficiente. Non è possibile prenotare alcun biglietto per il ritorno.')
                break
            else:
                numero_biglietto = int(input('\nQuale biglietto desideri acquistare? '))
                if partenze.partenze[destinazione][partenza][giorno_arrivo][numero_biglietto-1][0] > saldo:
                    print('Saldo insufficiente selezionare un nuovo biglietto! ')
                    continue
                sconto_biglietto = (partenze.partenze[destinazione][partenza][giorno_arrivo][numero_biglietto-1][0] * 30) / 100
                partenze.partenze[destinazione][partenza][giorno_arrivo][numero_biglietto-1][0] -= sconto_biglietto
                biglietti.append([giorno_arrivo,partenze.partenze[destinazione][partenza][giorno_arrivo][numero_biglietto-1]])
                print(f'\nIl prezzo del volo scontato è {partenze.partenze[destinazione][partenza][giorno_arrivo][numero_biglietto-1][0]} ')
                saldo = saldo - partenze.partenze[destinazione][partenza][giorno_arrivo][numero_biglietto-1][0]
                print(f'\nIl saldo aggiornato è {saldo}.')
                
                # acquisto bagaglio
                print('\nNel biglietto è previsto un bagaglio a mano, dal peso massimo di 7kg. Al prezzo di 50 euro è possibile aggiungere un bagaglio da imbarcare.')
                if saldo >= 50:
                    bagaglio2 = input('\nAggiungere un bagaglio da imbarcare? si/no ')
                    if bagaglio2 == 'si':
                        saldo -=50
                        print('\nBagaglio aggiunto.')
                        biglietti[1].append(bagaglio1)
                    else:
                        biglietti[1].append(bagaglio1)
                else:
                    print('Saldo insufficiente. Non è possibile acquistare un bagaglio da imbarcare.')
                    
                break

    # procediamo con l'acquisto dei biglietti
    print('\nI biglietti selezionati sono: ')
    
    j = 1    
    for i in biglietti:
        print(f'\n{j})Giorno: {i[0]}, orario di partenza: {i[1][1]}, prezzo: {i[1][0]} euro, durata del volo: {i[1][2]}, compagnia: {i[1][3]}', end = ' ')
        if i[2] == 'si':
            print('+ BAGAGLIO\n')
        j+=1
    
    while True:
        if len(biglietti) == 0:
            print('\nNessun biglietto selezionato, ricompilare il programma.')       
            sys.exit()
          
        if input('\nProcedere con l\'acquisto dei/del biglietto? si/no ') == 'si':
            print(f'\nAttendere...')
            time.sleep(3)
            print('\nPrenotazione effettuata con successo.')
            
            # stampa biglietti
            print(f'\nL\'utente {nome} {cognome}, nato a {luogo_nascita} il {data_nascita} ha acquistato i seguenti biglietti: ')
            j = 1
            for i in biglietti:
                print(f'\n{j})Giorno: {i[0]}, orario di partenza: {i[1][1]}, prezzo: {i[1][0]} euro, durata del volo: {i[1][2]}, compagnia: {i[1][3]}', end = ' ')
                if i[2] == 'si':
                    print('+ BAGAGLIO\n')
                j+=1
            print(f'\nSaldo finale {saldo} euro.')
            
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
                        spesa_biglietti += i[1][0]
                        
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
                    print(f'\n{j})Giorno: {i[0]}, orario di partenza: {i[1][1]}, prezzo: {i[1][0]} euro, durata del volo: {i[1][2]}, compagnia: {i[1][3]}')
                    j+=1
                a = int(input('Quale prenotazione desidera annullare? '))
                
                if biglietti[a-1][2] == 'si':
                    saldo += 50
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
    
    # dati da inserire
    aeroporto_partenza = input('\nInserire aeroporto di partenza: ')
    aeroporto_arrivo = input('Inserire aeroporto di arrivo: ')
    giorno = int(input('Inserire il giorno: '))
    
    # azioni admin
    if azione_admin == '1':
        while True:  
            while partenze.partenze[aeroporto_partenza][aeroporto_arrivo][giorno] == []:
                    print('Non ci sono voli disponibili per quel giorno, selezionare un giorno diverso')
                    giorno = int(input('Inserire un nuovo giorno: '))
                    continue
            
            print('\nVoli disponibili nel giorno selezionato: ')
                
            j = 1
            for i in partenze.partenze[aeroporto_partenza][aeroporto_arrivo][giorno]:
                print(f'\n{j})Orario di partenza: {i[1]}, prezzo: {i[0]} euro, durata del volo: {i[2]}, compagnia: {i[3]}')
                j+=1
                    
            b = int(input('\nQuale volo desideri cancellare? '))
            c = input(f'\nSicuro di voler cancellare il volo {b}? si/no ')
            
            if c == 'si':
                print('\nOperazione in corso...')
                del partenze.partenze[aeroporto_partenza][aeroporto_arrivo][giorno][b-1]
                time.sleep(2)
                print('\nOperazione completata!')
                print('\nI voli disponibile nel giorno selezionato, dopo l\'aggiornamento saranno: ')
                
                j = 1
                for i in partenze.partenze[aeroporto_partenza][aeroporto_arrivo][giorno]:
                    print(f'\n{j})Orario di partenza: {i[1]}, prezzo: {i[0]} euro, durata del volo: {i[2]}, compagnia: {i[3]}')
                    j+=1
                print('\nARRIVEDERCI!')
                break
            elif c == 'no':
                continue
    else:
        while True:
            
            print('\nI voli disponibile nel giorno selezionato sono: ')
                
            j = 1
            for i in partenze.partenze[aeroporto_partenza][aeroporto_arrivo][giorno]:
                print(f'\n{j})Orario di partenza: {i[1]}, prezzo: {i[0]} euro, durata del volo: {i[2]}, compagnia: {i[3]}')
                j+=1
                
            print('\nInserire i dati del nuovo biglietto')
            
            prezzo = int(input('\nInserire il prezzo del biglietto: '))
            orario_partenza = input('Inserire l\'orario di partenza: ')
            durata_volo = input('Inserire la durata del volo: ')
            compagnia_aera = input('Inserire la compagnia aerea o le compagnie aeree: ')
        
            d = input(f'\nAggiungere il seguente volo? Orario di partenza: {orario_partenza}, prezzo: {prezzo} euro, durata del volo: {durata_volo},\
 compagnia: {compagnia_aera} si/no ')
            
            if d == 'si':
                print('\nOperazione in corso...')
                partenze.partenze[aeroporto_partenza][aeroporto_arrivo][giorno].append([prezzo,orario_partenza,durata_volo,compagnia_aera])
                time.sleep(2)
                print('\nOperazione riuscita!')
            
                print('\nI voli disponibile nel giorno selezionato, dopo l\'aggiornamento saranno: ')
                    
                j = 1
                for i in partenze.partenze[aeroporto_partenza][aeroporto_arrivo][giorno]:
                    print(f'\n{j})Orario di partenza: {i[1]}, prezzo: {i[0]} euro, durata del volo: {i[2]}, compagnia: {i[3]}')
                    j+=1
                print('\nARRIVEDERCI!')
                break
            else:
                continue