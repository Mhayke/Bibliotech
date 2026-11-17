"""
Módulo de monitoramento do sistema Bibliotech utilizando Prometheus.
Define métricas (Counters e Gauges) para observabilidade das operações
e inicia o servidor HTTP para exposição das métricas no endpoint /metrics.
"""

from prometheus_client import Counter, Gauge, start_http_server

# -------------------------------------------------------------
# Definição das Métricas Prometheus
# -------------------------------------------------------------

# Contador geral de operações
OPERANDO_OPERACOES_TOTAL = Counter(
    "bibliotech_operacoes_total",
    "Total de operações realizadas no sistema Bibliotech",
    ["operacao", "status"]
)

# Contadores específicos para livros
LIVROS_CADASTRADOS_TOTAL = Counter(
    "bibliotech_livros_cadastrados_total",
    "Total de livros cadastrados com sucesso"
)

LIVROS_DELETADOS_TOTAL = Counter(
    "bibliotech_livros_deletados_total",
    "Total de livros removidos do acervo"
)

LIVROS_CONSULTAS_TOTAL = Counter(
    "bibliotech_livros_consultas_total",
    "Total de buscas/consultas de livros realizadas"
)

# Contadores de empréstimos e devoluções
EMPRESTIMOS_TOTAL = Counter(
    "bibliotech_emprestimos_total",
    "Total de empréstimos de livros realizados"
)

DEVOLUCOES_TOTAL = Counter(
    "bibliotech_devolucoes_total",
    "Total de devoluções de livros realizadas"
)

# Contadores específicos para usuários
USUARIOS_CADASTRADOS_TOTAL = Counter(
    "bibliotech_usuarios_cadastrados_total",
    "Total de usuários cadastrados com sucesso"
)

USUARIOS_DELETADOS_TOTAL = Counter(
    "bibliotech_usuarios_deletados_total",
    "Total de usuários removidos do sistema"
)

USUARIOS_CONSULTAS_TOTAL = Counter(
    "bibliotech_usuarios_consultas_total",
    "Total de buscas/consultas de usuários realizadas"
)

# Contador de erros por módulo
ERROS_TOTAL = Counter(
    "bibliotech_erros_total",
    "Total de erros encontrados durante a execução",
    ["modulo"]
)

# Gauges para monitoramento do estado do acervo
LIVROS_TOTAL = Gauge(
    "bibliotech_livros_total",
    "Quantidade total de livros cadastrados no sistema"
)

LIVROS_DISPONIVEIS = Gauge(
    "bibliotech_livros_disponiveis",
    "Quantidade de livros disponíveis para empréstimo"
)

LIVROS_EMPRESTADOS = Gauge(
    "bibliotech_livros_emprestados",
    "Quantidade de livros atualmente emprestados"
)

# Gauge para monitoramento do total de usuários cadastrados
USUARIOS_TOTAL = Gauge(
    "bibliotech_usuarios_total",
    "Quantidade total de usuários cadastrados no sistema"
)

# Flag para garantir inicialização única do servidor
_servidor_iniciado = False


# -------------------------------------------------------------
# Inicialização do Servidor de Métricas
# -------------------------------------------------------------

def iniciar_monitoramento(porta=8000):
    """
    Inicializa o servidor HTTP do Prometheus para expor métricas na porta informada.
    """
    global _servidor_iniciado
    if not _servidor_iniciado:
        try:
            start_http_server(porta, addr="0.0.0.0")  # nosec B104
            _servidor_iniciado = True
            print(f"Servidor de monitoramento Prometheus ativo na porta {porta}.")
        except Exception as erro:
            print(f"Aviso: Não foi possível iniciar o servidor de monitoramento: {erro}")


# -------------------------------------------------------------
# Funções Utilitárias para Registro de Métricas
# -------------------------------------------------------------

def registrar_operacao(operacao, status="sucesso"):
    """Registra uma operação genérica no contador."""
    OPERANDO_OPERACOES_TOTAL.labels(operacao=operacao, status=status).inc()


def registrar_cadastro_livro(sucesso=True):
    """Registra tentativa ou sucesso de cadastro de livro."""
    if sucesso:
        LIVROS_CADASTRADOS_TOTAL.inc()
        registrar_operacao("cadastrar_livro", "sucesso")
    else:
        ERROS_TOTAL.labels(modulo="livros").inc()
        registrar_operacao("cadastrar_livro", "erro")


def registrar_delecao_livro(sucesso=True):
    """Registra tentativa ou sucesso de exclusão de livro."""
    if sucesso:
        LIVROS_DELETADOS_TOTAL.inc()
        registrar_operacao("deletar_livro", "sucesso")
    else:
        ERROS_TOTAL.labels(modulo="livros").inc()
        registrar_operacao("deletar_livro", "erro")


def registrar_busca_livro(encontrado=True):
    """Registra uma consulta/busca de livro."""
    LIVROS_CONSULTAS_TOTAL.inc()
    status = "sucesso" if encontrado else "nao_encontrado"
    registrar_operacao("buscar_livro", status)


def registrar_emprestimo(sucesso=True):
    """Registra tentativa ou sucesso de empréstimo de livro."""
    if sucesso:
        EMPRESTIMOS_TOTAL.inc()
        registrar_operacao("emprestimo", "sucesso")
    else:
        ERROS_TOTAL.labels(modulo="emprestimos").inc()
        registrar_operacao("emprestimo", "erro")


def registrar_devolucao(sucesso=True):
    """Registra tentativa ou sucesso de devolução de livro."""
    if sucesso:
        DEVOLUCOES_TOTAL.inc()
        registrar_operacao("devolucao", "sucesso")
    else:
        ERROS_TOTAL.labels(modulo="devolucoes").inc()
        registrar_operacao("devolucao", "erro")


def registrar_cadastro_usuario(sucesso=True):
    """Registra tentativa ou sucesso de cadastro de usuário."""
    if sucesso:
        USUARIOS_CADASTRADOS_TOTAL.inc()
        registrar_operacao("cadastrar_usuario", "sucesso")
    else:
        ERROS_TOTAL.labels(modulo="usuarios").inc()
        registrar_operacao("cadastrar_usuario", "erro")


def registrar_delecao_usuario(sucesso=True):
    """Registra tentativa ou sucesso de exclusão de usuário."""
    if sucesso:
        USUARIOS_DELETADOS_TOTAL.inc()
        registrar_operacao("deletar_usuario", "sucesso")
    else:
        ERROS_TOTAL.labels(modulo="usuarios").inc()
        registrar_operacao("deletar_usuario", "erro")


def registrar_busca_usuario(encontrado=True):
    """Registra uma consulta/busca de usuário."""
    USUARIOS_CONSULTAS_TOTAL.inc()
    status = "sucesso" if encontrado else "nao_encontrado"
    registrar_operacao("buscar_usuario", status)


def registrar_erro(modulo):
    """Registra um erro associado a um módulo específico."""
    ERROS_TOTAL.labels(modulo=modulo).inc()


def atualizar_metricas_livros(lista_de_livros):
    """
    Atualiza os medidores (Gauges) com a contagem de livros
    totais, disponíveis e emprestados.
    """
    if lista_de_livros is None:
        return

    total = len(lista_de_livros)
    disponiveis = sum(1 for livro in lista_de_livros if livro.get("disponivel", False))
    emprestados = total - disponiveis

    LIVROS_TOTAL.set(total)
    LIVROS_DISPONIVEIS.set(disponiveis)
    LIVROS_EMPRESTADOS.set(emprestados)


def atualizar_metricas_usuarios(lista_de_usuarios):
    """Atualiza o medidor (Gauge) com a contagem total de usuários."""
    if lista_de_usuarios is None:
        return
    USUARIOS_TOTAL.set(len(lista_de_usuarios))
