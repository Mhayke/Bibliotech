import unittest
from unittest.mock import patch

from emprestimos import emprestar_livro


class TestEmprestimoLivro(unittest.TestCase):

    def test_emprestimo_livro_com_sucesso(self):
        usuarios = [
            {
                "nome": "João",
                "identificador": "001"
            }
        ]

        livros = [
            {
                "titulo": "Dom Casmurro",
                "identificador": "L001",
                "disponibilidade": True
            }
        ]

        with patch("builtins.input", side_effect=["001", "L001"]):
            emprestar_livro(usuarios, livros)

        self.assertEqual(livros[0]["disponibilidade"], False)

    def test_emprestimo_livro_indisponivel(self):
        usuarios = [
            {
                "nome": "João",
                "identificador": "001"
            }
        ]

        livros = [
            {
                "titulo": "Dom Casmurro",
                "identificador": "L001",
                "disponibilidade": False
            }
        ]

        with patch("builtins.input", side_effect=["001", "L001"]):
            emprestar_livro(usuarios, livros)

        self.assertEqual(livros[0]["disponibilidade"], False)


if __name__ == "__main__":
    unittest.main()
```
