#BLACKJACK V2.1

import random
import time

print("!!BENVENUTO NEL CASINO P3PPE!!\n!OGGI SI GIOCA A BLACKJACK!")


#spiegazione regole gioco
spiegazione = str(input("sai giocare a blackjack? (s/n)\n"))
regole = False
while not regole:
    if spiegazione == str("s"):
        regole = True
        break
    else:
        print("ecco a te le regole per giocare\nleggile attentamente prima di iniziare:\nregole_testo"
    "BLACKJACK - Regole base:\n"
    "- Si gioca contro il banco (il mazziere).\n"
    "- Ogni giocatore riceve 2 carte iniziali.\n"
    "- Obiettivo: avvicinarsi il più possibile a 21\n"
    "  senza superarlo.\n"
    "- Le carte da 2 a 10 valgono il loro numero.\n"
    "- Le figure (J, Q, K) valgono 10.\n"
    "- L'Asso vale 1 oppure 11, a seconda della mano.\n"
    "- Dopo le prime 2 carte, puoi:\n"
    "  - Chiedere carta (Hit)\n"
    "  - Stare (Stand)\n"
    "- Se superi 21, hai perso (Bust).\n"
    "- Il banco deve pescare fino a 17 o più.\n"
    "- Vince chi ha il punteggio più alto senza bustare.\n"
)
        str(input("premi invio per continuare:"))
        regole = True
        break

while True:
    print("mischiando le carte...", end="\r")
    time.sleep(5)
    print(" " * 20, end="\r")  # Cancella il messaggio precedente
    print("Pronto!") 

    valori_carte = {
        "A": 11,
        "2": 2, "3": 3, "4": 4, "5": 5,
        "6": 6, "7": 7, "8": 8, "9": 9,
        "10": 10, "J": 10, "Q": 10, "K": 10
    }
    semi = ["♠", "♥", "♦", "♣"]  # Picche, Cuori, Quadri, Fiori
    valori = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    mazzo = [f"{valore}{seme}" for seme in semi for valore in valori]

    while True:
        
        pesca = str(input("premi P per pescare le tue carte:\n"))
        if pesca == str("p") or str("P"):
            carta_1 = random.choice(mazzo)
            mazzo.remove(carta_1)
            carta_2 = random.choice(mazzo)
            mazzo.remove(carta_2)
            print(carta_1, carta_2)
            break
        else:
            print("input non valido, riprova.")
            continue

    print("ecco le carte del dealer: ")
    print("...", end="\r")
    time.sleep(1)
    print(" " * 40, end="\r")  # Cancella il messaggio precedente
    carta_1_dealer = random.choice(mazzo)
    mazzo.remove(carta_1_dealer)
    carta_2_dealer = random.choice(mazzo)
    mazzo.remove(carta_2_dealer)
    print(carta_1_dealer, "--")   

    #calcolo valori carte e somma
    valore_carta_1 = carta_1[:-1]
    valore_carta_2 = carta_2[:-1]
    valore_carta_1_dealer = carta_1_dealer[:-1]
    valore_carta_2_dealer = carta_2_dealer[:-1]
    totale_player = valori_carte[valore_carta_1] + valori_carte[valore_carta_2]
    totale_dealer = valori_carte[valore_carta_1_dealer] + valori_carte[valore_carta_2_dealer]

    #nuovo tentativo e pesca carte
    if valori_carte[valore_carta_1] + valori_carte[valore_carta_2] > 21:
        tentativo = str(input("hai sballato, vuoi tentare ancora?: (s/n)\n"))
        if tentativo == str("s"):
            nuovo_tentativo = True
            continue
        elif tentativo == str("n"):
            exit
        else:
            print("input non valido, riavvio automatico")
            continue
    elif valori_carte[valore_carta_1_dealer] + valori_carte[valore_carta_2_dealer] > 21:
        tentativo = str(input("hai vinto!!, il dealer ha sballato\nvuoi tentare ancora?: (s/n)\n"))
        if tentativo == str("s"):
            continue
        elif tentativo == str("n"):
            exit
        else:
            print("input non valido, riavvio automatico")
            continue
        
        stand = False    
        totale_player = valori_carte[valore_carta_1] + valori_carte[valore_carta_2]
        if totale_player > 21:
            tentativo = str(input("hai sballato, vuoi tentare ancora?: (s/n)\n"))
            if tentativo == str("s"):
                nuovo_tentativo = True
                continue
            elif tentativo == str("n"):
                exit()
            else:
                print("input non valido, riprova")
                continue

    while totale_player < 21:
        pesca = str(input("hit o stand?  (h/s)"))
        if pesca.lower() == "h" :
            carta_nuova = random.choice(mazzo)
            mazzo.remove(carta_nuova)
            valore_carta_nuova = carta_nuova[:-1]
            totale_player += valori_carte[valore_carta_nuova]
            print("carta:", carta_nuova, "ecco il tuo punteggio:", totale_player)
            continue
        elif pesca.lower() == "s" :
            print("hai deciso di stare!")
            print("ecco il tuo punteggio:", totale_player, "\necco il punteggio del dealer:", totale_dealer)
            print(carta_1_dealer, carta_2_dealer)
            stand = True
            break
        else:
            print("input non valido, riprova")
            continue
    
    
    

        #decisione vittoria/sconfitta
    if totale_player > 21:
        tentativo = str(input("hai sballato, vuoi tentare ancora?: (s/n)\n"))
        if tentativo == str("s"):
            nuovo_tentativo = True
            continue
        elif tentativo == str("n"):
            exit()
        else:
            print("input non valido, riavvio automatico!")
            continue
        continue

    if totale_dealer > 21:
        tentativo = str(input("!!HAI VINTO!!\nil dealer ha sballato, vuoi tentare ancora?: (s/n)\n"))
        if tentativo == str("s"):
            continue
        elif tentativo == str("n"):
            exit()
        else:
            print("input non valido, riavvio automatico!")
            continue
        continue


    while totale_dealer < 17:
        carta_3_dealer = random.choice(mazzo)
        mazzo.remove(carta_3_dealer)
        valore_carta_3_dealer = carta_3_dealer[:-1]
        totale_dealer += valori_carte[valore_carta_3_dealer]
        print("il dealer ha pescato:\n", carta_1_dealer, carta_2_dealer, carta_3_dealer, "\n il totale del dealer è:", totale_dealer, "\n il tuo totale è:", totale_player)
        break
    if totale_player > totale_dealer :
        print("HAI VINTO!!!")
        continue
    else:
        print("hai perso")
        continue




        
