import unittest
from unittest.mock import patch

from emprestimos import emprestar_livro


class TestEmprestimoLivro(unittest.TestCase):

    def test_emprestimo_livro_com_sucesso(self):
        livros = [
            {
                "titulo": "Dom Casmurro",
                "id": "L001",
                "disponivel": True
            }
        ]

        with patch("builtins.input", side_effect=["1", "L001"]):
            emprestar_livro(livros)

        self.assertEqual(livros[0]["disponivel"], False)

    def test_emprestimo_livro_indisponivel(self):
        livros = [
            {
                "titulo": "Dom Casmurro",
                "id": "L001",
                "disponivel": False
            }
        ]

        with patch("builtins.input", side_effect=["1", "L001"]):
            emprestar_livro(livros)

        self.assertEqual(livros[0]["disponivel"], False)


if __name__ == "__main__":
    unittest.main()