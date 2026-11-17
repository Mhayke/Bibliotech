import os
import monitoramento

usuarios = []


def cadastrar_usuario(lista_de_usuarios):
    print(" ---------------------------------------------------")
    print("                CADASTRO DE USUÁRIO")
    print(" ---------------------------------------------------")

    nome = input("\n Nome do usuário: ")
    identificador = input(" Identificador do usuário: ")

    # Verifica se o identificador já existe
    for usuario in lista_de_usuarios:
        if usuario["identificador"] == identificador:
            print("\n Erro: já existe um usuário com esse identificador.")
            monitoramento.registrar_cadastro_usuario(sucesso=False)
            return

    usuario = {
        "nome": nome,
        "identificador": identificador
    }

    lista_de_usuarios.append(usuario)
    monitoramento.registrar_cadastro_usuario(sucesso=True)
    monitoramento.atualizar_metricas_usuarios(lista_de_usuarios)

    print("\n Usuário cadastrado com sucesso!")


def listar_usuarios(lista_de_usuarios):
    print(" ---------------------------------------------------")
    print("                USUÁRIOS CADASTRADOS")
    print(" ---------------------------------------------------")

    if not lista_de_usuarios:
        print("\n Nenhum usuário cadastrado.")
        monitoramento.registrar_operacao("listar_usuarios", "vazio")
        monitoramento.atualizar_metricas_usuarios(lista_de_usuarios)
        return

    for usuario in lista_de_usuarios:
        print(f" Nome: {usuario['nome']} | Identificador: {usuario['identificador']}")

    monitoramento.registrar_operacao("listar_usuarios", "sucesso")
    monitoramento.atualizar_metricas_usuarios(lista_de_usuarios)


def buscar_usuario(lista_de_usuarios):
    print(" ---------------------------------------------------")
    print("                   BUSCAR USUÁRIO")
    print(" ---------------------------------------------------")

    identificador = input("\n Digite o identificador do usuário: ")

    for usuario in lista_de_usuarios:
        if usuario["identificador"] == identificador:
            print(f"\n Nome: {usuario['nome']} | Identificador: {usuario['identificador']}")
            monitoramento.registrar_busca_usuario(encontrado=True)
            return

    print("\n Usuário não encontrado.")
    monitoramento.registrar_busca_usuario(encontrado=False)


def deletar_usuario(lista_de_usuarios):
    print(" ---------------------------------------------------")
    print("            DELETAR USUÁRIO POR IDENTIFICADOR")
    print(" ---------------------------------------------------")

    identificador = input("\n Digite o identificador do usuário: ")

    for usuario in lista_de_usuarios:
        if usuario["identificador"] == identificador:
            lista_de_usuarios.remove(usuario)
            print("\n Usuário deletado com sucesso!")
            monitoramento.registrar_delecao_usuario(sucesso=True)
            monitoramento.atualizar_metricas_usuarios(lista_de_usuarios)
            return

    print("\n Usuário não encontrado.")
    monitoramento.registrar_delecao_usuario(sucesso=False)


def gestao_usuarios(lista_de_usuarios):

    sair = True  # variável para controlar o loop
    while sair:  # condição de loop para continuar o programa

        print(" ---------------------------------------------------")
        print("                  GESTÃO DE USUÁRIOS")
        print(" ---------------------------------------------------")
        print(" [1] Cadastrar Usuário  [2] Listar Usuários")
        print(" [3] Buscar Usuário     [4] Deletar Usuário")
        print(" [5] Voltar")

        opt = input("\n Digite uma opção: ")

        try:
            opt = int(opt)
        except ValueError:
            opt = 0  # valor inválido, cai no else implícito (nenhuma opção é executada)

        os.system("cls" if os.name == "nt" else "clear")  # nosec B605

        if opt == 1:
            cadastrar_usuario(lista_de_usuarios)

        elif opt == 2:
            listar_usuarios(lista_de_usuarios)

        elif opt == 3:
            buscar_usuario(lista_de_usuarios)

        elif opt == 4:
            deletar_usuario(lista_de_usuarios)

        elif opt == 5:
            os.system("cls" if os.name == "nt" else "clear")  # nosec B605
            sair = False
            break


if __name__ == "__main__":

    gestao_usuarios(usuarios)
