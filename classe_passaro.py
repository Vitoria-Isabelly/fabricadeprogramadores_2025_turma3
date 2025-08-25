class Pássaro():

    def __init__(self, tamanho, cores, espécie, sexo):
        self.tamanho = tamanho
        self.cores = cores
        self.espécie = espécie
        self.sexo = sexo

    def cantar(self):
        return print(f'Sou um {self.espécie} cantando uma bela canção')
                    
    def voar(self):
        return print('Batendo as asas e: voando...')

pássaro1 = Pássaro(0.14, ['Marrom', 'Branco', 'Cinza'], 'Pardal', 'M')
pássaro1.cantar()

