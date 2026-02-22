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

def filtru_lungime(text,limita_litere):
    randuri=text.split('\n')
    randuri_noi=[]
    for rand in randuri:
        cuvinte=rand.split()
        cuvinte_filtrate=[c for c in cuvinte if len(c)>=limita_litere]
        randuri_noi.append(" ".join(cuvinte_filtrate))
    return "\n".join(randuri_noi)
#testing

text_init=read_file('input.txt')
text = read_file('input.txt')
text = elim_punct(text)
text = to_upper(text)
text = elimina_spatii_multiple(text)
text = left_allign(text)

text_final = filtru_lungime(text, 6)
print(text_final)