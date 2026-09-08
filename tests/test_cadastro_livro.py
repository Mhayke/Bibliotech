import unittest
from unittest.mock import patch

from livros import cadastrar_livro


class TestCadastroLivro(unittest.TestCase):

    def test_cadastro_livro_com_sucesso(self):
        livros = []

        with patch("builtins.input", side_effect=["4", "Harry Potter"]):
            cadastrar_livro(livros)

        self.assertEqual(len(livros), 1)
        self.assertEqual(livros[0]["id"], "4")
        self.assertEqual(livros[0]["titulo"], "Harry Potter")
        self.assertEqual(livros[0]["disponivel"], True)

    def test_cadastro_livro_id_duplicado(self):
        livros = [
            {
                "id": "1",
                "titulo": "Senhor dos Anéis",
                "disponivel": True
            }
        ]

        with patch("builtins.input", side_effect=["1", "O Hobbit"]):
            cadastrar_livro(livros)

        self.assertEqual(len(livros), 1)
        self.assertEqual(livros[0]["titulo"], "Senhor dos Anéis")


if __name__ == "__main__":
    unittest.main()

