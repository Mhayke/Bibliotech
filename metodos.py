import livros
import emprestimos
import devolucoes
import usuarios
import monitoramento


def registrar_operacao(operacao, status="sucesso"):
    """Registra o acompanhamento de uma operação no módulo de monitoramento."""
    monitoramento.registrar_operacao(operacao, status)
