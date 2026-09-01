import os # acesso a funções que interagem com o sistema operacional (Windows, Linux, Mac).
 
class Biblioteca:
    def __init__(self, metodos):
        self.m = metodos
        self.lista_de_livros = metodos.livros.livros      # usa a lista fixa já definida em livros.py
        self.lista_de_usuarios = []    # lista compartilhada de usuários
 
    def iniciar_biblioteca(self):

        sair = True  # variável para controlar o loop
        while sair:  # condição de loop para continuar o programa
 
            print(" -------------------------------------------------------------")
            print("                      B I B L I O T E C H                     ")
            print(" -------------------------------------------------------------")
            print(" [1] Cadastrar Livro [2] Livros Disponíveis [3] Buscar Livro  ")
            print(" [4] Emprestar livro [5] Devolver livro     [6] Deletar Livro ")
            print(" [7] Gestão Usuarios [8] Sair                                 ")
 
            opt = input("\n Digite uma opção: ")  # opção digitada pelo usuário
            try:
                opt = int(opt)
            except ValueError:
                opt = 0  # valor inválido, cai no else implícito (nenhuma opção é executada)
 
            os.system("cls" if os.name == "nt" else "clear")  # limpa a tela (Windows ou Linux/Mac)
 
            if opt == 1:  # Opção para cadastrar livro
                self.m.livros.cadastrar_livro(self.lista_de_livros)
               
            elif opt == 2:  # opção para listar todos os livros disponíveis
                self.m.livros.listar_livros_disp(self.lista_de_livros)
              
            elif opt == 3:  # opção para buscar um livro
                self.m.livros.buscar_livro(self.lista_de_livros)
 
            elif opt == 4:  # opção para emprestar um livro
                self.m.emprestimos.emprestar_livro(self.lista_de_livros)
               
            elif opt == 5:  # opção para devolver um livro
                self.m.devolucoes.devolver_livro(self.lista_de_livros)
 
            elif opt == 6:  # opção para deletar um livro
                self.m.livros.deletar_livro(self.lista_de_livros)

            elif opt == 7: # opção para gerenciar usuarios
                self.m.usuarios.gestao_usuarios(self.lista_de_usuarios)
 
            elif opt == 8:  # opção para sair do programa
 
                os.system("cls" if os.name == "nt" else "clear")

                print(" ---------------------------------------------------")
                print("        OBRIGADO POR USAR NOSSA BIBLIOTECH!         ")
                print(" ---------------------------------------------------")
                sair = False
                break # finaliza o loop do programa

 
if __name__ == "__main__":

    import metodos
 
    biblioteca = Biblioteca(metodos)
    biblioteca.iniciar_biblioteca()