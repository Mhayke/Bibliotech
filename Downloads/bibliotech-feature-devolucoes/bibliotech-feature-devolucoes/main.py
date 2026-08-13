from features.devolucoes import devolver_livro


def main():
    while True:
        print("\n===== SISTEMA DE BIBLIOTECA =====")
        print("1 - Cadastrar usuário")
        print("2 - Cadastrar livro")
        print("3 - Emprestar livro")
        print("4 - Devolver livro")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            pass

        elif opcao == "2":
            pass

        elif opcao == "3":
            pass

        elif opcao == "4":
            devolver_livro()

        elif opcao == "5":
            print("Sistema encerrado.")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()