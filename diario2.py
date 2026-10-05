with open("diario2.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("teste 1\n")
    arquivo.write("teste 2\n")
    arquivo.write("teste 3\n")
    
with open("diario2.txt", "a", encoding="utf-8") as arquivo:
    arquivo.write("teste 4\n")
    arquivo.write("teste 5\n")

with open("diario2.txt", "r", encoding="utf-8") as arquivo:
    for numero, linha in enumerate(arquivo, start=1):
        print(f"{numero}: {linha.strip()}")
        


contador = 0
with open("diario2.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        contador += 1
        print (contador,linha.strip())