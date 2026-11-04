"""Testes de infraestrutura com Testinfra para o cenário Molecule da role bibliotech."""


def test_diretorio_bibliotech_existe(host):
    """1. Verifica se o diretório /tmp/bibliotech existe."""
    app_dir = host.file("/tmp/bibliotech")  # nosec B108
    assert app_dir.exists  # nosec B101


def test_diretorio_aplicacao_e_diretorio(host):
    """2. Verifica se o diretório da aplicação é realmente um diretório."""
    app_dir = host.file("/tmp/bibliotech")  # nosec B108
    assert app_dir.is_directory  # nosec B101


def test_ambiente_virtual_criado(host):
    """3. Verifica se o ambiente virtual foi criado."""
    venv_dir = host.file("/tmp/bibliotech/venv")  # nosec B108
    assert venv_dir.exists  # nosec B101
    assert venv_dir.is_directory  # nosec B101


def test_executavel_python_venv_existe(host):
    """4. Verifica se o executável Python do ambiente virtual existe."""
    python_bin = host.file("/tmp/bibliotech/venv/bin/python")  # nosec B108
    assert python_bin.exists  # nosec B101
    assert python_bin.is_file  # nosec B101
    assert python_bin.is_executable  # nosec B101


def test_requirements_txt_copiado(host):
    """5. Verifica se o arquivo requirements.txt foi copiado."""
    requirements_file = host.file("/tmp/bibliotech/requirements.txt")  # nosec B108
    assert requirements_file.exists  # nosec B101
    assert requirements_file.is_file  # nosec B101


def test_pasta_tests_copiada(host):
    """6. Verifica se a pasta tests/ foi copiada."""
    tests_dir = host.file("/tmp/bibliotech/tests")  # nosec B108
    assert tests_dir.exists  # nosec B101
    assert tests_dir.is_directory  # nosec B101
