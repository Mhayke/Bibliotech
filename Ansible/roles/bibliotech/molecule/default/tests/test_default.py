"""Testes de infraestrutura com Testinfra para o cenário Molecule da role bibliotech."""


def test_diretorio_bibliotech_existe(host):
    """1. Verifica se o diretório /tmp/bibliotech existe."""
    app_dir = host.file("/tmp/bibliotech")
    assert app_dir.exists


def test_diretorio_aplicacao_e_diretorio(host):
    """2. Verifica se o diretório da aplicação é realmente um diretório."""
    app_dir = host.file("/tmp/bibliotech")
    assert app_dir.is_directory


def test_ambiente_virtual_criado(host):
    """3. Verifica se o ambiente virtual foi criado."""
    venv_dir = host.file("/tmp/bibliotech/venv")
    assert venv_dir.exists
    assert venv_dir.is_directory


def test_executavel_python_venv_existe(host):
    """4. Verifica se o executável Python do ambiente virtual existe."""
    python_bin = host.file("/tmp/bibliotech/venv/bin/python")
    assert python_bin.exists
    assert python_bin.is_file
    assert python_bin.is_executable


def test_requirements_txt_copiado(host):
    """5. Verifica se o arquivo requirements.txt foi copiado."""
    requirements_file = host.file("/tmp/bibliotech/requirements.txt")
    assert requirements_file.exists
    assert requirements_file.is_file


def test_pasta_tests_copiada(host):
    """6. Verifica se a pasta tests/ foi copiada."""
    tests_dir = host.file("/tmp/bibliotech/tests")
    assert tests_dir.exists
    assert tests_dir.is_directory

