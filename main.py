from tabelas import SessionLocal, Usuario, Nota

db = SessionLocal()

def criar_novo_usuario_e_nota():
    """Exemplo de como CRIAR dados."""
    novo_usuario = Usuario( 
        nome="Vitória Isabelly",
        email="Vitoriaisabelly21107@email.com",
        senha_hash="hash_super_seguro"
    )  

    db.add(novo_usuario) 
    db.commit()

    print(f"Usuário '{novo_usuario.nome}' criado com ID: {novo_usuario.id}")

    nova_nota = Nota(
        titulo="Minha Primeira Nota com SQLAlchemy",
        conteudo="É muito mais fácil do que escrever SQL na mão!",
        autor = novo_usuario
    )

    db.add(nova_nota)
    db.commit()
    print (f"Nota '{nova_nota.titulo}' criada para {novo_usuario.nome}.")

def ler_dados (nome):
    """Exemplo de como LER dados."""

    user = db.query(Usuario).filter(Usuario.nome == nome).first()

    if user:
        print(f"Encontrei o(a): {user.nome} (Email: {user.email})")
    
        print("Notas do user:")
        for nota in user.notas :
            print(f" - Título: {nota.titulo} (ID: {nota.id})")
    else:
        print("Usuário(a) não encontrado.")

def atualizar_nota(id_nota):
    """Exemplo de como ATUALIZAR dados."""

    nota_para_editar = db.query(Nota).filter(Nota.id == id_nota).first()

    if nota_para_editar:
        print(f"Título original: '{nota_para_editar.titulo}'")

        nota_para_editar.titulo = "Lista de anotações ATULIZADA!"

        db.commit()
        print(f"Título novo: '{nota_para_editar.titulo}'")

    else:
        print("Nota com ID %d nçao encontrada." % id_nota)