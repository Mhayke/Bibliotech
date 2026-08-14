from features.livros import livros


def devolver_livro():
    identificador = input("Digite o identificador do livro: ")

    for livro in livros:
        if livro["id"] == identificador:

            if livro["disponivel"]:
                print("Este livro já está disponível.")
                return

            livro["disponivel"] = True
            print("Livro devolvido com sucesso!")
            return

    print("Livro não encontrado.")