import csv

nome_do_arquivo = 'produtos.csv'

try:
    exemplo_arquivo = open(nome_do_arquivo)
    exemplo_leitor = csv.reader(exemplo_arquivo, delimiter=',', dialect='excel')

    for linha in exemplo_leitor:
        print('Linha #%s <%s>' % (exemplo_leitor.line_num, linha))

    exemplo_arquivo.close()

except FileNotFoundError:
    print('Arquivo não encontrado')
