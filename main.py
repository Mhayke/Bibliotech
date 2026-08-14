import os # acesso a funções que interagem com o sistema operacional (Windows, Linux, Mac).
 
class Biblioteca:
    def __init__(self, metodos):
        self.m = metodos
 
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
                pass
               
            elif opt == 2:  # opção para listar todos os livros disponíveis
                pass
              
            elif opt == 3:  # opção para buscar um livro
                pass
 
            elif opt == 4:  # opção para emprestar um livro
                pass
               
            elif opt == 5:  # opção para devolver um livro
                pass
 
            elif opt == 6:  # opção para deletar um livro
                pass

            elif opt == 7: # opção para gerenciar usuarios
                pass
 
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