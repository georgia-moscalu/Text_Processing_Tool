def read_file(name):
    with open(name,'r') as f: #deschide fisierul si automat il inchide
        return f.read() #ia toate caracterele si spatiile din fisier si returneaza un sir lung de car


text_init=read_file('input.txt')
print (text_init)