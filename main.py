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
def to_upper(text):
    rezultat=""
    for caracter in text:
        cod=ord(caracter)
        if 97<= cod <= 122:
            rezultat+=chr(cod-32)
        else:
            rezultat+=caracter
    return rezultat
def elimina_spatii_multiple(text):
    rezultat=""
    ultimul_caracter=""

    for caracter in text:
        if caracter==" " and ultimul_caracter==" ":
            #ultimu caracter ex" A  B-> A e this caracter last e "" iar la a doua iteratie
            #last e "A" this carac e "" etc
             continue #caracterul curent e aruncat si trece mai departe
        rezultat+=caracter
        ultimul_caracter=caracter
    return rezultat.strip() #sterge spatiu dininte si dupa cuvant
def left_allign(text):
    #impartim textul in randuri
    randuri=text.split("\n")
    randuri_curate=[]

    for rand in randuri:
        #cautam poz primei litere care nu e spatiu
        index_prima_litera=0
        while index_prima_litera<len(rand) and rand[index_prima_litera]==" ":
            index_prima_litera+=1
        rand_aliniat=rand[index_prima_litera:]
        randuri_curate.append(rand_aliniat)
    return "\n".join(randuri_curate)
#testing

text_init=read_file('input.txt')
print(text_init)
text_fara_punct=elim_punct(text_init)
text_litere_mici=to_lower(text_fara_punct)
text_litere_mari=to_upper(text_fara_punct)
text_fara_spatii_duble=elimina_spatii_multiple(text_fara_punct)

print(text_fara_spatii_duble)
text_aliniat=left_allign(text_fara_spatii_duble)
print(text_aliniat)