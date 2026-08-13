# Sistema de Biblioteca
# Execução pelo terminal

usuarios = []


def cadastrar_usuario():
    print("\n--- Cadastro de Usuário ---")

    nome = input("Nome do usuário: ")
    identificador = input("Identificador do usuário: ")

    # Verifica se o identificador já existe
    for usuario in usuarios:
        if usuario["identificador"] == identificador:
            print("Erro: já existe um usuário com esse identificador.")
            return

    usuario = {
        "nome": nome,
        "identificador": identificador
    }

    usuarios.append(usuario)

    print("Usuário cadastrado com sucesso!")
