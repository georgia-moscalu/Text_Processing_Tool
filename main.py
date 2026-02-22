def read_file(name):
    with open(name,'r') as f: #deschide fisierul si automat il inchide
        return f.read() #ia toate caracterele si spatiile din fisier si returneaza un sir lung de car

def elim_punct(text):
    semne='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    text_curat="".join(caracter for caracter in text if caracter not in semne)
    #'h' 'e' 'l' 'l' 'o' join->le lipseste cu un sir vid ""
    return text_curat

#testing
text_init=read_file('input.txt')
print (text_init)
text_fara_punct=elim_punct(text_init)
print(text_fara_punct)