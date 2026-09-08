import unittest
from unittest.mock import patch

from usuarios import cadastrar_usuario


class TestCadastroUsuario(unittest.TestCase):

    def test_cadastro_usuario_com_sucesso(self):
        usuarios = []

        with patch("builtins.input", side_effect=["João", "001"]):
            cadastrar_usuario(usuarios)

        self.assertEqual(len(usuarios), 1)
        self.assertEqual(usuarios[0]["nome"], "João")
        self.assertEqual(usuarios[0]["identificador"], "001")

    def test_cadastro_usuario_identificador_duplicado(self):
        usuarios = [
            {
                "nome": "João",
                "identificador": "001"
            }
        ]

        with patch("builtins.input", side_effect=["Maria", "001"]):
            cadastrar_usuario(usuarios)

        self.assertEqual(len(usuarios), 1)


if __name__ == "__main__":
    unittest.main()
