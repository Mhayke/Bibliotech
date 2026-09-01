# Baseline v1.0.0 — Bibliotech

## 1. Identificação

* **Nome do sistema:** Bibliotech
* **Identificação da baseline:** BL-BIBLIOTECH-1.0.0
* **Versão:** 1.0.0
* **Data:** 17/08/2026
* **Status:** Em preparação para aprovação
* **Tipo:** Baseline de versão

### Integrantes responsáveis

* Vanessa Carolina Ramos
* Matheus Danilo José da Cruz
* Diego José da Silva Gomes
* Caio Pacifico Alves Cabral

---

## 2. Itens de Configuração

| Nome                       | Tipo               | Estado/versão             | Justificativa                                                                                                          |
| -------------------------- | ------------------ | ------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Código-fonte do Bibliotech | Código             | Estado atual da `develop` | Contém a implementação das funcionalidades do sistema e deve ser controlado para garantir a rastreabilidade da versão. |
| `README.md`                | Documentação       | Estado atual              | Contém as informações necessárias para compreender o sistema, sua estrutura e forma de execução.                       |
| `.gitignore`               | Configuração       | Estado atual              | Define arquivos e diretórios que não devem ser versionados, evitando a inclusão de artefatos desnecessários.           |
| Python                     | Ambiente           | 3.14.7                    | Versão utilizada para executar e validar o sistema durante a preparação da baseline.                                   |
| `docs/baseline-v1.0.0.md`  | Documentação       | v1.0.0                    | Registra a identificação, o conteúdo, o ambiente e as limitações conhecidas da baseline.                               |
| Repositório Git            | Controle de versão | Estado aprovado da v1.0.0 | Permite controlar o histórico de alterações e identificar exatamente o estado do sistema associado à baseline.         |

---

## 3. Funcionalidades incluídas

A versão 1.0.0 contempla as seguintes funcionalidades:

### Cadastro de usuários

Permite cadastrar usuários contendo nome e identificador único.

### Cadastro de livros

Permite cadastrar livros contendo título, identificador e disponibilidade.

### Empréstimo de livros

Permite emprestar livros disponíveis para usuários cadastrados e impede o empréstimo de livros que já estejam emprestados.

### Devolução de livros

Permite registrar a devolução de livros emprestados, tornando-os novamente disponíveis.

### Funcionalidades adicionais

O sistema também possui funcionalidades complementares de gerenciamento de livros e usuários, incluindo busca, listagem e exclusão.

---

## 4. Ambiente

* **Linguagem:** Python
* **Versão utilizada nos testes:** Python 3.14.7
* **Execução:** Terminal/CLI
* **Sistema operacional utilizado na validação:** Windows
* **Dependências externas:** Não possui
* **Banco de dados:** Não utilizado
* **Frameworks:** Não utilizados

O sistema mantém os dados em memória durante a execução. Dessa forma, os dados cadastrados não são persistidos após o encerramento do programa.

Para executar o sistema:

```bash
python main.py
```

---

## 5. Verificação do estado do sistema

Antes da preparação da baseline, foram realizadas verificações do funcionamento do sistema.

As quatro funcionalidades obrigatórias foram testadas:

* cadastro de usuários;
* cadastro de livros;
* empréstimo de livros;
* devolução de livros.

Também foi verificado que:

* livros disponíveis são listados corretamente;
* livros emprestados deixam de ser considerados disponíveis;
* o sistema impede o empréstimo de um livro que já esteja emprestado;
* livros devolvidos voltam a ficar disponíveis;
* o sistema pode ser executado em outra máquina após a instalação do Python.

O repositório também foi verificado com relação aos arquivos versionados e ao estado do diretório de trabalho.

---

## 6. Problemas encontrados e correções

Durante a verificação do estado do sistema, foram identificados arquivos gerados automaticamente pelo Python (`__pycache__` e arquivos `.pyc`) sendo rastreados pelo Git.

### Correção realizada

Foi criado o arquivo `.gitignore` contendo regras para ignorar:

```text
__pycache__/
*.pyc
```

Os arquivos `.pyc` que estavam sendo rastreados foram removidos do controle de versão.

A correção foi registrada no commit:

```text
055be49 — chore: add gitignore and remove Python cache files
```

Após a correção, foi verificado que nenhum arquivo `.pyc` permanece rastreado no estado atual da `develop`.

---

## 7. Limitações conhecidas

* Os dados são mantidos somente em memória durante a execução do programa.
* Não existe persistência em banco de dados ou arquivos.
* Os dados cadastrados são perdidos quando o programa é encerrado.
* A aplicação possui interface exclusivamente via terminal.
* Não são utilizados mecanismos externos de autenticação ou persistência.

Essas limitações não impedem o atendimento aos requisitos definidos para a versão 1.0.0 da atividade.

---

## 8. Status da Baseline

A versão **1.0.0** representa o estado conhecido e controlado do sistema após a integração das funcionalidades obrigatórias, realização das verificações e correção dos problemas identificados no repositório.

A baseline deverá ser considerada **aprovada após a revisão da versão na branch `release/1.0.0` e posterior aprovação do Merge Request para a branch `main`**.

A identificação técnica definitiva da versão será realizada por meio da tag Git:

```text
v1.0.0
```
