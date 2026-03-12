import string
import random 

pwG = False  # Dies wird als Globale Variable / Flagge um die Password neu zu lesen benutzt


#-----    random_zahl

def random_zahl(stellen):
    ret= "".join(random.choice(string.digits) for i in range(stellen))
    return ret

def random_string(stellen = 4, dictionary = string.ascii_lowercase):
    ret = "".join(str(random.choice(dictionary)) for i in range (stellen))
    return ret


#----------- FETCH password 
#----------- Lies Passwort aus Datei passworddatei.txt
#----------- und schreibe es in Variable pw


def fetch_pw():
    f=open("passwortdatei.txt", "r")
    pwG = str(f.readline())
    f.close()
    return (pwG)


#-------------- CHECK-Funktion: Input = Password?

def check(inp):
    global pwG
    
    if (not pwG):
        pwG= fetch_pw()
    if (type(inp) == int):
        try:
            pwG = int(pwG)
        except:
            pwG = pwG
    if (inp == pwG):
        print("Hurra, du hast das Passwort geknackt: ")
        return(True)
    else:
        return(False)

    
#---------- RESET-Funktionen erzeugen neues Zufalls-Password in passworddatei.txt
#---------- In der Shell eingeben:
#---------- DEFAULT: reset_zahl() erzeugt Zahl aus vier Ziffern
#----------          reset_wort() erzeugt Wort aus vier Buchstaben
#----------          reset_wortlist() erzeugt Wort aus vier Worter von Wortlist Datei    
def reset_zahl(stellen = 4):
    global pwG
    pwG = False
    f=open("passwortdatei.txt", "w")
    pw = random_zahl(stellen)
    f.write(pw)
    f.close()
    print("Zahlen-Passwort der Länge {} wurde erstellt!".format(stellen))
    #print(pw)
    

def reset_wort(stellen = 4, dictionary = string.ascii_lowercase):
    global pwG
    pwG = False
    pw=random_string(stellen, dictionary)
    f=open("passwortdatei.txt", "w")
    f.write(pw)
    f.close()
    print("Buchstaben-Passwort der Länge {} wurde erstellt!".format(stellen))
    print(pw)
    

def reset_wortList(stellen=3):
    global pwG
    pwG = False
    
    with open("pw_word_list.txt") as temp:
        wordList = temp.read().splitlines() 
    
    #pw = random_wortlist(stellen, wordList)
    pw = random_string(stellen, wordList)
    f=open("passwortdatei.txt","w")
    f.write(pw)
    f.close()
    print("Worter-Passwort der Länge {} wurde erstellt!".format(stellen))
    #print("neu erstelltes Password : ", pw)
    


