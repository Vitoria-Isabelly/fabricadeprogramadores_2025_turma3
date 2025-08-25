from animais_marinhos import AnimalMarinho

animais = [
    AnimalMarinho("Golfinho", "Delphinus delphis", 2.5, True, "oceano"),
    AnimalMarinho("Tubarão Branco", "Carcharodon carcharias", 6.0, True, "oceano"),
    AnimalMarinho("Baleia Azul", "Balaenoptera musculus", 24.0, False, "oceano"),
    AnimalMarinho("Cavalo-Marinho", "Hippocampus", 0.1, False, "recifes"),
    AnimalMarinho("Polvo", "Octopus vulgaris", 1.2, True, "fundo do mar"),
    AnimalMarinho("Estrela-do-mar", "Asteroidea", 0.3, False, "recifes"),
    AnimalMarinho("Orca", "Orcinus orca", 8.0, True, "oceano"),
    AnimalMarinho("Lula Gigante", "Architeuthis", 12.0, True, "profundezas do oceano"),
    AnimalMarinho("Foca", "Phocidae", 1.8, True, "águas geladas"),
    AnimalMarinho("Leão-marinho", "Otariinae", 2.4, True, "costa"),
    AnimalMarinho("Caranguejo", "Brachyura", 0.2, False, "praias rochosas"),
    AnimalMarinho("Tartaruga Marinha", "Cheloniidae", 1.5, False, "oceano"),
    AnimalMarinho("Peixe-palhaço", "Amphiprioninae", 0.2, False, "recifes de coral"),
    AnimalMarinho("Narval", "Monodon monoceros", 4.5, True, "águas árticas"),
    AnimalMarinho("Peixe-boi", "Trichechus", 3.0, False, "rios costeiros"),
    AnimalMarinho("Água-viva", "Cnidaria", 0.5, False, "mar aberto"),
    AnimalMarinho("Enguia", "Anguilliformes", 1.0, True, "rios e mares"),
    AnimalMarinho("Raia", "Batoidea", 2.5, True, "fundo do mar"),
    AnimalMarinho("Coral", "Anthozoa", 0.05, False, "recifes"),
    AnimalMarinho("Linguado", "Pleuronectiformes", 0.4, True, "fundo do mar"),
]

for animal in animais:
    animal.exibir_dados()
    animal.emitir_som()
    animal.nadar()
    animal.alimentar()
    animal.crescer(0.1)
    print("-" * 40)
