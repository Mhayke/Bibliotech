import os

emprestimos = []  # lista para armazenar os empréstimos realizados

def emprestar_livro(livros):

    sair = True  # variável para controlar o loop
    while sair:  # condição de loop para continuar o programa
        
        print(" ---------------------------------------------------")
        print("                EMPRÉSTIMO DE LIVRO")
        print(" ---------------------------------------------------")
        print("           [1] Emprestar Livro [2] Voltar           ")
        
        opt = input("\n Digite uma opção: ")  # opção digitada pelo usuário

        try:
            opt = int(opt)
        except ValueError:
            opt = 0  # valor inválido, cai no else implícito (nenhuma opção é executada)

        os.system("cls" if os.name == "nt" else "clear")  # limpa a tela (Windows ou Linux/Mac)

        if opt == 1:  # Opção para emprestar livro

            print(" ---------------------------------------------------")
            print("                EMPRÉSTIMO DE LIVRO")
            print(" ---------------------------------------------------")

            livro_id = input("\n Digite o ID do livro: ")

            # Procura o livro na lista pelo ID
            livro_encontrado = None
            for livro in livros:
                if livro["id"] == livro_id:
                    livro_encontrado = livro
                    break

            if livro_encontrado is None:
                print("\n Erro: livro não encontrado.")
                continue

            if not livro_encontrado["disponivel"]:
                print(f"\n Erro: o livro |{livro_encontrado['titulo']}| já está emprestado.")
                continue

            # Marca o livro como indisponível
            livro_encontrado["disponivel"] = False

            # Registra o empréstimo
            emprestimo = {
                "livro_id": livro_encontrado["id"],
                "titulo": livro_encontrado["titulo"],
            }

            emprestimos.append(emprestimo)

            print(f"\n Empréstimo realizado com sucesso! | {livro_encontrado['titulo']} | {livro_encontrado['id']} |")

        elif opt == 2:
            os.system("cls" if os.name == "nt" else "clear")

            sair = False
            break 


if __name__ == "__main__":

    import livros

    emprestar_livro(livros.livros)

