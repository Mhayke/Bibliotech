# Bibliotech

O **Bibliotech** é um sistema interativo em linha de comando (CLI) desenvolvido em Python para o gerenciamento de biblioteca, incluindo controle de acervo de livros, empréstimos, devoluções e gestão de usuários.

O projeto conta com esteira de CI/CD automatizada (GitHub Actions), conteinerização (Docker & Docker Compose), automação de provisionamento e configuração de ambiente (Ansible) e testes de infraestrutura (Molecule com Testinfra).

---

## 🚀 Funcionalidades

### 📚 Gestão de Livros
- **Cadastrar Livro**: Adiciona novos livros ao acervo garantindo IDs únicos.
- **Livros Disponíveis**: Lista todos os livros cadastrados disponíveis para empréstimo.
- **Buscar Livro**: Exibe informações detalhadas de um livro pesquisando pelo ID.
- **Deletar Livro**: Remove um livro do acervo através do seu ID.

### 🔄 Empréstimos e Devoluções
- **Emprestar Livro**: Registra o empréstimo de um livro disponível e atualiza seu status para indisponível.
- **Devolver Livro**: Processa a devolução de um livro emprestado e restaura sua disponibilidade.

### 👤 Gestão de Usuários
- **Cadastrar Usuário**: Registra novos usuários com Nome e Identificador único.
- **Listar Usuários**: Exibe todos os usuários cadastrados no sistema.
- **Buscar Usuário**: Localiza um usuário pelo seu identificador.
- **Deletar Usuário**: Remove um usuário do sistema.

---

## 📋 Menus da Aplicação

### Menu Principal
| Opção | Ação |
| :---: | :--- |
| **1** | Cadastrar livro |
| **2** | Listar livros disponíveis |
| **3** | Buscar livro |
| **4** | Emprestar livro |
| **5** | Devolver livro |
| **6** | Deletar livro |
| **7** | Abrir gestão de usuários |
| **8** | Sair |

### Gestão de Usuários
| Opção | Ação |
| :---: | :--- |
| **1** | Cadastrar usuário |
| **2** | Listar usuários |
| **3** | Buscar usuário |
| **4** | Deletar usuário |
| **5** | Voltar ao menu principal |

---

## 📁 Estrutura do Projeto

```text
Bibliotech/
├── .github/
│   └── workflows/
│       └── pipeline.yml          # Pipeline CI/CD no GitHub Actions
├── Ansible/
│   ├── inventory.ini             # Inventário Ansible para execução local
│   ├── playbook.yml              # Playbook principal de execução da Role
│   └── roles/
│       └── bibliotech/           # Role Ansible para preparação do ambiente
│           ├── defaults/
│           │   └── main.yml      # Variáveis padrão (app_dir, venv_dir)
│           ├── tasks/
│           │   └── main.yml      # Tarefas de provisionamento e testes
│           └── molecule/
│               └── default/      # Cenário de testes de infraestrutura
│                   ├── molecule.yml
│                   ├── converge.yml
│                   └── tests/
│                       └── test_default.py  # Testes com Testinfra
├── docs/
│   └── baseline-v1.0.0.md        # Documentação e baseline da versão v1.0.0
├── tests/                        # Testes unitários da aplicação (unittest)
│   ├── test_cadastro_livro.py
│   ├── test_cadastro_usuario.py
│   ├── test_devolucao.py
│   └── test_automatizado_emprestimo_python.py
├── compose.yml                   # Orquestração de contêineres Docker Compose
├── Dockerfile                    # Receita de build da imagem Docker
├── devolucoes.py                 # Módulo de devoluções
├── emprestimos.py                # Módulo de empréstimos
├── livros.py                     # Módulo de acervo de livros
├── main.py                       # Ponto de entrada interativo da aplicação
├── metodos.py                    # Unificador das rotinas do sistema
├── requirements.txt              # Dependências e ferramentas de segurança
├── usuarios.py                   # Módulo de gestão de usuários
└── README.md                     # Documentação geral do projeto
```

---

## 🛠️ Formas de Execução

### 1. Execução Local (Python)
Requer Python 3.x instalado:

```bash
python main.py
```

### 2. Execução com Docker
Você pode empacotar e executar a aplicação em um contêiner isolado:

```bash
# Construir a imagem Docker
docker build -t bibliotech .

# Executar o contêiner interativo
docker run -it --rm bibliotech
```

### 3. Execução com Docker Compose
Para subir o ambiente via Docker Compose com volume dedicado e rede isolada:

```bash
# Iniciar o serviço interativo
docker compose run --rm biblioteca
```

---

## 🧪 Testes Automatizados da Aplicação

Os testes unitários da aplicação foram implementados utilizando o módulo nativo `unittest` do Python.

Para executar todos os testes automatizados:

```bash
python -m unittest discover -s tests -v
```

---

## ⚙️ Automação com Ansible

O projeto possui uma **Role Ansible** (`roles/bibliotech`) desenvolvida para preparar e validar automaticamente o ambiente de execução da aplicação.

### O que a Role executa:
1. **Verificação do Python 3**: Checa se o Python 3 está instalado.
2. **Exibição da versão**: Mostra no console a versão encontrada.
3. **Criação do diretório**: Cria a pasta `/tmp/bibliotech`.
4. **Cópia da aplicação**: Copia seletivamente os arquivos Python do projeto via `role_path`.
5. **Cópia do `requirements.txt`**: Transfere o arquivo de dependências.
6. **Cópia dos testes**: Copia a pasta `tests/` para o ambiente.
7. **Ambiente Virtual**: Cria um ambiente virtual Python em `/tmp/bibliotech/venv`.
8. **Instalação de Dependências**: Instala as dependências via módulo `pip`.
9. **Execução dos Testes**: Executa a suíte de testes com o interpretador do ambiente virtual.
10. **Resultado dos Testes**: Exibe a saída detalhada dos testes.

### Como executar o Playbook:

```bash
cd Ansible
ansible-playbook -i inventory.ini playbook.yml
```

---

## 🔬 Testes de Infraestrutura com Molecule & Testinfra

O cenário de testes do **Molecule** valida se a automação do Ansible é idempotente e se prepara o ambiente corretamente.

- **Driver**: `default` (execução local).
- **Provisionador**: Ansible (`converge.yml`).
- **Verificador**: Testinfra (`test_default.py`).

### Como executar o ciclo de testes do Molecule:

```bash
cd Ansible/roles/bibliotech
export ANSIBLE_ROLES_PATH="$(pwd)/.."
molecule test
```

Etapas validadas pelo Molecule:
- **Syntax**: Validação da sintaxe dos playbooks da role.
- **Converge**: Execução da role aplicando o estado desejado.
- **Idempotence**: Segunda execução para garantir que nenhuma tarefa sofra alterações inesperadas (`changed=0`).
- **Verify**: Execução dos testes automatizados com **Testinfra** validando a integridade dos diretórios, executável do venv, dependências e testes.

---

## 🔄 Pipeline CI/CD (GitHub Actions)

A esteira de integração contínua (`.github/workflows/pipeline.yml`) é disparada automaticamente a cada `push` na branch `main`:

1. **Checkout**: Obtém o código-fonte do repositório.
2. **Setup Python**: Configura o runtime do Python 3.13.
3. **Build**: Realiza a compilação prévia do código (`python -m compileall .`).
4. **Segurança**:
   - **SAST**: Análise estática com **Bandit** (`bandit -r .`).
   - **SCA**: Análise de vulnerabilidades em dependências com **pip-audit**.
5. **Testes Automatizados**: Execução de todos os testes unitários com o `unittest`.
6. **Deploy**: Etapa simulada de entrega contínua.
