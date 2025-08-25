import csv

# Lista de termos a contar
termos = [
    "carabina", "carabina/cartucheira", "carabina/espingarda", "carabina/fuzil",
    "espingarda", "fuzil", "garrucha", "garruchão",
    "pistola", "pistolão", "revolvcer", "rifler"
]

# Inicializa o contador para cada termo
contagem = {termo: 0 for termo in termos}

# Lê o arquivo CSV linha por linha
with open("OCORRENCIAS_2025.csv", encoding="latin1") as arquivo:
    leitor = csv.reader(arquivo, delimiter=';')
    cabecalho = next(leitor)
    indice_coluna = cabecalho.index("ESPECIE_ARMA")

    for linha in leitor:
        if len(linha) <= indice_coluna:
            continue
        texto = linha[indice_coluna].lower()
        for termo in termos:
            if termo in texto:
                contagem[termo] += 1

# Mostra o resultado
for termo, qtd in contagem.items():
    print(f"{termo}: {qtd}")

