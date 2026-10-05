nome_arquivo = "diario.txt"
 
modo = input('Modo ("r" ler, "w" escrever, "a" acrescentar, "x" criar novo): ')
 
if modo not in ("r", "w", "a", "x"):
    print("Modo inválido. Use r, w, a ou x.")
else:
    if modo != "r":
        quantidade = int(input("Quantas frases deseja gravar? "))
        with open(nome_arquivo, modo, encoding="utf-8") as arquivo:
            for i in range(quantidade):
                frase = input(f"Frase {i + 1}: ")
                arquivo.write(frase + "\n")
 
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for numero, linha in enumerate(arquivo, start=1):
            print(f"{numero}: {linha.strip()}")