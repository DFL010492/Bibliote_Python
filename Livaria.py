Livros = {
    8725: {'nome': 'O Vento Levou', 'autor': 'Margaret Mitchell', 'Disponivel': True},
    8724: {'nome': 'Senhor dos Anéis', 'autor': 'J.R.R. Tolkien', 'Disponivel': True},
    8723: {'nome': '1984', 'autor': 'George Orwell', 'Disponivel': True}
}

Usuarios = {
    1: {'id': 1, 'nome': 'Jorge Matos', 'livros': []},
    2: {'id': 2, 'nome': 'Ana Silva', 'livros': []},
    3: {'id': 3, 'nome': 'Carlos Pereira', 'livros': []}
}

Escolha = input("Digite '1' para listar livros ou '2' para adicionar usuário: ")

while True:
    if Escolha not in ['1', '2']:
        print("Escolha inválida. Digite '1' para listar livros ou '2' para adicionar usuário.")
        Escolha = input("Digite sua escolha: ")
    else:
        break

    if Escolha == '1':
        Livros_nome = [livro['nome'] for livro in Livros.values()]
        print(f"Livros Disponíveis: {Livros_nome}")
            
    elif Escolha == '2':
        nome_usuario = input("Digite o nome do usuário: ")
        usuario_id = len(Usuarios) + 1
        Usuarios[usuario_id] = {'id': usuario_id, 'nome': nome_usuario, 'livros': []}
        print(f"Usuário '{nome_usuario}' adicionado com sucesso com ID {usuario_id}.")
        print(Usuarios)

