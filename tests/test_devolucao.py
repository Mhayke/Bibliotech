import unittest
from unittest.mock import patch

from devolucoes import devolver_livro


class TestDevolverLivro(unittest.TestCase):

    def test_devolver_livro_com_sucesso(self):
        """Deve tornar disponível um livro que estava emprestado."""

        livros = [
            {
                "id": "1",
                "titulo": "Dom Casmurro",
                "disponivel": False
            }
        ]

        # 1 = devolver livro
        # 1 = ID do livro
        # 2 = voltar
        entradas = ["1", "1", "2"]

        with patch("builtins.input", side_effect=entradas):
            with patch("os.system"):
                devolver_livro(livros)

        self.assertTrue(livros[0]["disponivel"])


    def test_devolver_livro_que_ja_esta_disponivel(self):
        """Não deve alterar um livro que já está disponível."""

        livros = [
            {
                "id": "1",
                "titulo": "Dom Casmurro",
                "disponivel": True
            }
        ]

        entradas = ["1", "1", "2"]

        with patch("builtins.input", side_effect=entradas):
            with patch("os.system"):
                devolver_livro(livros)

        self.assertTrue(livros[0]["disponivel"])


    def test_devolver_livro_inexistente(self):
        """Um ID inexistente não deve alterar os livros."""

        livros = [
            {
                "id": "1",
                "titulo": "Dom Casmurro",
                "disponivel": False
            }
        ]

        entradas = ["1", "999", "2"]

        with patch("builtins.input", side_effect=entradas):
            with patch("os.system"):
                devolver_livro(livros)

        self.assertFalse(livros[0]["disponivel"])


    def test_devolver_livro_correto_em_lista_com_varios_livros(self):
        """Deve devolver somente o livro cujo ID foi informado."""

        livros = [
            {
                "id": "1",
                "titulo": "Dom Casmurro",
                "disponivel": False
            },
            {
                "id": "2",
                "titulo": "O Cortiço",
                "disponivel": False
            }
        ]

        entradas = ["1", "2", "2"]

        with patch("builtins.input", side_effect=entradas):
            with patch("os.system"):
                devolver_livro(livros)

        self.assertFalse(livros[0]["disponivel"])
        self.assertTrue(livros[1]["disponivel"])


if __name__ == "__main__":
    unittest.main()
