def read_file(name):
    with open(name,'r') as f: #deschide fisierul si automat il inchide
        return f.read() #ia toate caracterele si spatiile din fisier si returneaza un sir lung de car

def elim_punct(text):
    semne='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    text_curat="".join(caracter for caracter in text if caracter not in semne)
    #'h' 'e' 'l' 'l' 'o' join->le lipseste cu un sir vid ""
    return text_curat
def to_lower(text):
    rezultat=""
    for caracter in text:
        cod=ord(caracter) #primeste caracter A si returneaza ord 65
        if 65 <= cod <= 90:
            rezultat+=chr(cod+32) #chr - de la nr la litera
        else:
            rezultat+=caracter
    return rezultat

#testing
text_init=read_file('input.txt')
text_fara_punct=elim_punct(text_init)
text_litere_mici=to_lower(text_fara_punct)
print(text_litere_mici)