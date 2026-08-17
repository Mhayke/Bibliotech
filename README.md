# Bibliotech

O **Bibliotech** é um sistema interativo em linha de comando (CLI) desenvolvido em Python para o gerenciamento básico de uma biblioteca, incluindo controle de acervo de livros, empréstimos, devoluções e gestão de usuários.

---

## 🚀 Funcionalidades

### 📚 Gestão de Livros
- **Cadastrar Livro**: Adiciona novos livros ao acervo garantindo IDs únicos.
- **Livros Disponíveis**: Lista todos os livros cadastrados no momento que estão disponíveis para empréstimo.
- **Buscar Livro**: Exibe informações detalhadas de um livro específico pesquisando pelo ID.
- **Deletar Livro**: Remove um livro do acervo através do seu ID.

### 🔄 Empréstimos e Devoluções
- **Emprestar Livro**: Registra o empréstimo de um livro disponível e altera seu status para indisponível.
- **Devolver Livro**: Processa a devolução de um livro emprestado e altera seu status de volta para disponível.

### 👤 Gestão de Usuários
- **Cadastrar Usuário**: Registra novos usuários com Nome e Identificador único.
- **Listar Usuários**: Exibe todos os usuários cadastrados no sistema.
- **Buscar Usuário**: Procura um usuário pelo seu identificador.
- **Deletar Usuário**: Remove um usuário do sistema.

---

## 📁 Estrutura do Projeto

- **`main.py`**: Ponto de entrada da aplicação, onde fica o menu principal interativo.
- **`livros.py`**: Módulo com a lista base de livros e funções de CRUD para livros.
- **`emprestimos.py`**: Módulo para tratamento e registro das solicitações de empréstimo.
- **`devolucoes.py`**: Módulo para processamento de devolução de livros.
- **`usuarios.py`**: Módulo para cadastro e gerenciamento de usuários.
- **`metodos.py`**: Módulo unificador das funcionalidades dos outros módulos.

---

## 🛠️ Como Executar

1. Certifique-se de ter o Python instalado (versão 3.x).
2. Execute o script principal no terminal:

```bash
python main.py
```
