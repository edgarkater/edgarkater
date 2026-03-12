from check_pw import *

######### Stufe 2: Vorübung in Python zu For-Schleife und Bedingung
def stufe2():
    for zahl in range (100):
        print (zahl, end=" ")
        if (zahl %7 == 0):
            print("ist teilbar durch sieben")
        else:
            print("ist nicht durch sieben teilbar")


######### Stufe 3 ohne Generierung führender Nullen:
def check_zahl():
    for zahl in range(10000):
        if check(zahl):
            print(zahl)
            return
    return    

        
######### Stufe 3.5 mit Generierung führender Nullen:
def check_zahl_mit_Nullen():
    for zahl in range(10000):
        #if check(zahl):
        n = ""
        if (zahl<10):
            n = ("000")
        elif (zahl<100):
            n = ("00")
        elif (zahl < 1000):
            n = ("0")
        checkz = n+str(zahl)
        if (check (checkz)):
            print("password =  ", checkz)
            return
        
    return


########## Stufe 4 (Kleinbuchstaben)
def check_wort():
    alphabet = string.ascii_lowercase
    #alphabet = string.ascii_uppercase
    #alphabet = string.ascii_letters
    
    for letter1 in alphabet:
        for letter2 in alphabet:
            for letter3 in alphabet:
                for letter4 in alphabet:
                    guess = letter1+letter2+letter3+letter4
                    if check(guess):
                        print("password = ", guess)    
                        return
    print("fehlgeschlagen")
    return 

########## Stufe 5 (Wörterbuchvergleich)                    
def check_Worterbuch():
    with open("pw_word_list.txt") as temp:
        tempList = temp.read().splitlines()
        
    for word in tempList:
        if (check(str(word))):
             print(word)
             return
    print("fehlgeschlagen, ")
    return
    

########## Stufe 6 (Wörterbuchvergleich = Mehrstellig)                    



def check_wortList():
    
    with open("pw_word_list.txt") as temp:
        tempList = temp.read().splitlines()
    
    #x = 0  dieses index wird nur fuer laufzeit/versuche
    for word1 in tempList:
        for word2 in tempList:
            for word3 in tempList:
                checkWord = word1 + word2 + word3
                #x += 1     # index incrementiert
                if (check(str(checkWord))):
                    #print(checkWord, "  |   x = ", x)
                    print(checkWord)
                    return
                
    print("fehlgeschlagen :   # Versuche = ", x)                
    return

########## Stufe 5a (Stichwörter aus sozialen Profilen durchprobieren)
# Ergänze Wörterbuchdatei am Anfang um neue Stichwörter; Abspeichern.
# Rufe dann wcheck() auf
# Zum Testen muss die Passwortdatei im Notepad++ überschrieben werden.
# ACHTUNG: NICHT MS WORD ALS EDITOR BENUTZEN
    


### Programmaufrufe zum Testen: -------------------

#stufe2()
#check_zahl()
#check_zahl_mit_Nullen()
#reset_wort()
#check_wort()
#check_woerterbuch()
#reset_zahl()

for i in range (10):
    #reset_zahl()
    #reset_wort()
    #check_wort()
    #check_zahl()
    #check_zahl_mit_Nullen()
    reset_wortList(3)
    #check_zahl()
    check_wortList()
    #check_Worterbuch()


### In der Shell neues Passwort erzeugen:  ----------------------

# reset_letters(n)  # erzeugt Zufallspasswort aus n Kleinbuchstaben (0<n<4)
# reset_zahl(n)     # erzeugt Zufallspasswort aus n Ziffern 0..9 (0<n<4)

print("beep boop fertig")

        
        
 
