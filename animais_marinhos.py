class AnimalMarinho:
    def __init__(self, nome, especie, tamanho_metros, eh_carnivoro, habitat):
        self.nome = nome                        
        self.especie = especie                 
        self.tamanho_metros = tamanho_metros    
        self.eh_carnivoro = eh_carnivoro        
        self.habitat = habitat                  

    def emitir_som(self):
        print(f"{self.nome} está emitindo um som característico.")

    def nadar(self):
        print(f"{self.nome} está nadando rapidamente pelo {self.habitat}.")

    def alimentar(self):
        if self.eh_carnivoro:
            print(f"{self.nome} está caçando sua presa.")
        else:
            print(f"{self.nome} está se alimentando de plantas marinhas.")

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Tamanho: {self.tamanho_metros:.2f} metros")
        print(f"Carnívoro: {'Sim' if self.eh_carnivoro else 'Não'}")
        print(f"Habitat: {self.habitat}")

    def crescer(self, crescimento):
        self.tamanho_metros += crescimento
        print(f"{self.nome} cresceu e agora tem {self.tamanho_metros:.2f} metros.")
