import os

livros = [
    {
        "id": "1",
        "titulo": "Senhor dos Anéis",
        "disponivel": True
    },
    {
        "id": "2",
        "titulo": "O Hobbit",
        "disponivel": True
    },
    {
        "id": "3",
        "titulo": "Death Note",
        "disponivel": True
    }
]


def cadastrar_livro(lista_de_livros):
    print(" ---------------------------------------------------")
    print("                  CADASTRO DE LIVRO")
    print(" ---------------------------------------------------")

    novo_id = input("\n Digite o ID do livro: ")

    # Verifica se o ID já existe
    for livro in lista_de_livros:
        if livro["id"] == novo_id:
            print("\n Erro: já existe um livro com esse ID.")
            return

    titulo = input("\n Digite o título do livro: ")

    novo_livro = {
        "id": novo_id,
        "titulo": titulo,
        "disponivel": True
    }

    lista_de_livros.append(novo_livro)

    print(f"\n Livro '{titulo}' cadastrado com sucesso!")


def buscar_livro(lista_de_livros):
    print(" ---------------------------------------------------")
    print("                    BUSCA DE LIVRO")
    print(" ---------------------------------------------------")

    identificador = input("\n Digite o ID do livro: ")

    for livro in lista_de_livros:
        if livro["id"] == identificador:
            status = "Disponível" if livro["disponivel"] else "Emprestado"
            print(f"\n ID: {livro['id']} | Título: {livro['titulo']} | Status: {status}")
            return

    print("\n Livro não encontrado.")


def deletar_livro(lista_de_livros):
    print(" ---------------------------------------------------")
    print("                DELETAR LIVRO POR ID")
    print(" ---------------------------------------------------")

    identificador = input("\n Digite o ID do livro: ")

    for livro in lista_de_livros:
        if livro["id"] == identificador:
            lista_de_livros.remove(livro)
            print(f"\n Livro '{livro['titulo']}' deletado com sucesso!")
            return

    print("\n Livro não encontrado.")


def listar_livros_disp(lista_de_livros):
    print(" ---------------------------------------------------")
    print("                  LIVROS DISPONÍVEIS")
    print(" ---------------------------------------------------")

    algum_disponivel = False

    for livro in lista_de_livros:
        if livro["disponivel"]:
            print(f" ID: {livro['id']} | Título: {livro['titulo']}")
            algum_disponivel = True

    if not algum_disponivel:
        print("\n Nenhum livro disponível no momento.")


if __name__ == "__main__":
    cadastrar_livro(livros)
    buscar_livro(livros)
    deletar_livro(livros)