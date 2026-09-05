# Bibliotech

O **Bibliotech** é uma aplicação de linha de comando (CLI), desenvolvida em
Python, para o gerenciamento básico de livros, empréstimos, devoluções e
usuários de uma biblioteca.

## 🚀 Funcionalidades 

### 📚 Gestão de Livros

- Cadastrar livros com ID, título e status de disponibilidade.
- Listar somente os livros disponíveis.
- Buscar um livro por ID e consultar seu status.
- Excluir um livro por ID.
- Impedir o cadastro de dois livros com o mesmo ID.

O catálogo inicial contém:

| ID | Título | Status inicial |
| --- | --- | --- |
| 1 | Senhor dos Anéis | Disponível |
| 2 | O Hobbit | Disponível |
| 3 | Death Note | Disponível |

### 🔄 Empréstimos e devoluções

- Emprestar um livro existente e disponível.
- Impedir o empréstimo de um livro que já esteja emprestado.
- Devolver um livro pelo ID e torná-lo disponível novamente.
- Informar quando o livro não existe ou já está disponível.

Os empréstimos são registrados em memória com o ID e o título do livro. O
fluxo atual não solicita nem associa o empréstimo a um usuário.

### 👤 Gestão de Usuários

- Cadastrar usuários com nome e identificador.
- Listar usuários cadastrados.
- Buscar um usuário por identificador.
- Excluir um usuário por identificador.
- Impedir identificadores de usuário duplicados.

## 🛠️ Como executar

Requisitos:

- Python 3.x instalado. A baseline do projeto foi validada com Python 3.14.7.
- Nenhuma dependência externa ou framework é necessária.

No terminal, execute:

```bash
python main.py
```

O programa limpa a tela automaticamente usando o comando apropriado para
Windows, Linux ou macOS.

## Menus da aplicação

### Menu principal

| Opção | Ação |
| --- | --- |
| 1 | Cadastrar livro |
| 2 | Listar livros disponíveis |
| 3 | Buscar livro |
| 4 | Emprestar livro |
| 5 | Devolver livro |
| 6 | Deletar livro |
| 7 | Abrir gestão de usuários |
| 8 | Sair |

### Gestão de usuários

| Opção | Ação |
| --- | --- |
| 1 | Cadastrar usuário |
| 2 | Listar usuários |
| 3 | Buscar usuário |
| 4 | Deletar usuário |
| 5 | Voltar ao menu principal |

Os menus de empréstimo e devolução também oferecem a opção de voltar:

- `1`: executar a operação;
- `2`: voltar ao menu principal.

## 📁 Estrutura do projeto

- [`main.py`](main.py): ponto de entrada e menu principal da aplicação.
- [`livros.py`](livros.py): catálogo inicial e operações de cadastro, busca, listagem e exclusão de livros.
- [`emprestimos.py`](emprestimos.py): fluxo de empréstimos e registro em memória.
- [`devolucoes.py`](devolucoes.py): fluxo de devoluções e atualização da disponibilidade.
- [`usuarios.py`](usuarios.py): cadastro, listagem, busca, exclusão e menu de usuários.
- [`metodos.py`](metodos.py): importa e reúne os módulos usados pela aplicação.
- [`tests/`](tests/): diretório reservado para testes automatizados; atualmente contém apenas `.gitkeep`.
- [`docs/baseline-v1.0.0.md`](docs/baseline-v1.0.0.md): registro da baseline da versão 1.0.0.
- [`.gitlab-ci.yml`](.gitlab-ci.yml): pipeline de build, testes e deploy simulado.

## 🔄 Testes e integração contínua

Para executar a descoberta de testes localmente:

```bash
python -m unittest discover -s tests -v
```

O pipeline do GitLab usa Python 3.11 e possui três etapas: build, testes com
`unittest` e deploy simulado. Não há testes automatizados implementados no
diretório `tests/` no estado atual do projeto.

## ⚠️ Limitações conhecidas

- Os dados de livros, usuários e empréstimos ficam somente em memória e são
	perdidos quando o programa é encerrado.
- Não há banco de dados nem persistência em arquivos.
- Empréstimos não são vinculados a usuários e não há autenticação ou controle
	de permissões.
- O registro de empréstimos não é removido nem atualizado durante a devolução.
- É possível excluir um livro que esteja emprestado, deixando o registro do
	empréstimo inconsistente.
- Não há validação específica para IDs, identificadores ou títulos vazios.
- Opções de menu inválidas não exibem uma mensagem de erro específica.
- A interface está disponível somente no terminal.
- O módulo de livros não possui operação de atualização; as operações
	disponíveis são cadastro, listagem, busca e exclusão.
