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
<<<<<<< HEAD

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
=======
>>>>>>> c322f695f648648ba9de25c1e26fa67c3e3c883d
