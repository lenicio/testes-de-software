class Livro:
    def __init__(self, isbn, autor, editora, titulo, genero_literario):
        self.isbn = isbn
        self.autor = autor
        self.editora = editora
        self.titulo = titulo
        self.genero_literario = genero_literario

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn):
        if len(isbn) < 10 or len(isbn) > 13:
            raise ValueError('ISBN inválido. Deve conter 10 ou 13 dígitos.')
        self.__isbn = isbn
