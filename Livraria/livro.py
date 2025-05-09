from typing import Optional, NoReturn

class Livro:
    def __init__(self, isbn: str, autor: str, editora: Optional[str, None],
                 titulo: str, genero_literario: str) -> NoReturn:
        """
        Modelo de livro.

        Args:
            isbn: Código único de cada livro.
            autor: Pessoa que escreveu o livro.
            editora: Empresa que publicou. Este campo é opcional.
            titulo: Nome do livro.
            genero_literario: Genero ao qual o livro pertence. ex: Aventura, Romance, etc.
        """

        self.isbn = isbn
        self.autor = autor
        self.editora = editora
        self.titulo = titulo
        self.genero_literario = genero_literario

    @property
    def isbn(self) -> str:
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str) -> None:
        if len(isbn) < 10 or len(isbn) > 13:
            raise ValueError('ISBN inválido. Deve conter 10 ou 13 dígitos.')
        self.__isbn = isbn


# isbn = "123"  # ISBN inválido (muito curto)
# autor = "J.R.R. Tolkien"
# editora = "HarperCollins"
# titulo = "O Senhor dos Anéis"
# genero_literario = "Fantasia"
#
#
# Livro(
#     isbn=isbn,
#     autor=autor,
#     editora=editora,
#     titulo=titulo,
#     genero_literario=genero_literario
# )