import os


def devolver_livro(livros):

    sair = True  # variável para controlar o loop
    while sair:  # condição de loop para continuar o programa

        print(" ---------------------------------------------------")
        print("                  DEVOLUÇÃO DE LIVRO")
        print(" ---------------------------------------------------")
        print("           [1] Devolver Livro [2] Voltar            ")

        opt = input("\n Digite uma opção: ")  

        try:
            opt = int(opt)
        except ValueError:
            opt = 0  # valor inválido, cai no else implícito (nenhuma opção é executada)

        os.system("cls" if os.name == "nt" else "clear")  # limpa a tela (Windows ou Linux/Mac)

        if opt == 1:  # Opção para devolver livro

            print(" ---------------------------------------------------")
            print("                  DEVOLUÇÃO DE LIVRO")
            print(" ---------------------------------------------------")

            identificador = input("\n Digite o ID do livro: ")

            livro_encontrado = False

            for livro in livros:
                if livro["id"] == identificador:
                    livro_encontrado = True

                    if livro["disponivel"]:
                        print("\n Este livro já está disponível.")
                        continue

                    livro["disponivel"] = True
                    print(f"\n Devolução realizado com sucesso! | {livro['titulo']} | {livro['id']} |")
                    continue

            if not livro_encontrado:
                print("\n Erro: livro não encontrado.")
                continue

            # Marca o livro como disponivel
            livro["disponivel"] = True

        elif opt == 2:  # Opção para voltar
            os.system("cls" if os.name == "nt" else "clear")

            sair = False
            break

if __name__ == "__main__":

    import livros

    devolver_livro(livros.livros)