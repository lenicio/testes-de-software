import pytest
from livro import Livro

# A classe Livro ainda não existe, mas os testes serão escritos para ela
# Os alunos deverão implementar a classe baseando-se nos testes


def test_quando_criar_livro_com_parametros_validos_deve_criar_objeto():
    """
    Teste para verificar se a criação de um livro com parâmetros válidos
    cria o objeto corretamente.
    """
    # Arrange
    isbn = "9788532530837"
    autor = "J.R.R. Tolkien"
    editora = "HarperCollins"
    titulo = "O Senhor dos Anéis"
    genero_literario = "Fantasia"

    # Act
    livro = Livro(
        isbn=isbn,
        autor=autor,
        editora=editora,
        titulo=titulo,
        genero_literario=genero_literario
    )

    # Assert
    assert livro.isbn == isbn
    assert livro.autor == autor
    assert livro.editora == editora
    assert livro.titulo == titulo
    assert livro.genero_literario == genero_literario


def test_quando_isbn_for_invalido_deve_lancar_erro():
    """
    Teste para verificar se a criação de um livro com ISBN inválido
    lança um erro com a mensagem apropriada.
    """
    # Arrange
    isbn = "123"  # ISBN inválido (muito curto)
    autor = "J.R.R. Tolkien"
    editora = "HarperCollins"
    titulo = "O Senhor dos Anéis"
    genero_literario = "Fantasia"

    # Act & Assert
    with pytest.raises(ValueError, match="ISBN inválido. Deve conter 10 ou 13 dígitos."):
        Livro(
            isbn=isbn,
            autor=autor,
            editora=editora,
            titulo=titulo,
            genero_literario=genero_literario
        )


def test_quando_titulo_for_vazio_deve_lancar_erro():
    """
    Teste para verificar se a criação de um livro com título vazio
    lança um erro com a mensagem apropriada.
    """
    # Arrange
    isbn = "9788532530837"
    autor = "J.R.R. Tolkien"
    editora = "HarperCollins"
    titulo = ""  # Título vazio
    genero_literario = "Fantasia"

    # Act & Assert
    with pytest.raises(ValueError, match="O título do livro não pode ser vazio."):
        Livro(
            isbn=isbn,
            autor=autor,
            editora=editora,
            titulo=titulo,
            genero_literario=genero_literario
        )


def test_quando_autor_for_vazio_deve_lancar_erro():
    """
    Teste para verificar se a criação de um livro com autor vazio
    lança um erro com a mensagem apropriada.
    """
    # Arrange
    isbn = "9788532530837"
    autor = ""  # Autor vazio
    editora = "HarperCollins"
    titulo = "O Senhor dos Anéis"
    genero_literario = "Fantasia"

    # Act & Assert
    with pytest.raises(ValueError, match="O autor do livro não pode ser vazio."):
        Livro(
            isbn=isbn,
            autor=autor,
            editora=editora,
            titulo=titulo,
            genero_literario=genero_literario
        )


def test_quando_editora_for_vazia_deve_lancar_erro():
    """
    Teste para verificar se a criação de um livro com editora vazia
    lança um erro com a mensagem apropriada.
    """
    # Arrange
    isbn = "9788532530837"
    autor = "J.R.R. Tolkien"
    editora = ""  # Editora vazia
    titulo = "O Senhor dos Anéis"
    genero_literario = "Fantasia"

    # Act & Assert
    with pytest.raises(ValueError, match="A editora do livro não pode ser vazia."):
        Livro(
            isbn=isbn,
            autor=autor,
            editora=editora,
            titulo=titulo,
            genero_literario=genero_literario
        )


def test_quando_genero_literario_for_vazio_nao_deve_lancar_erro():
    """
    Teste para verificar se a criação de um livro com gênero literário vazio
    não lança erro, pois este campo é opcional.
    """
    # Arrange
    isbn = "9788532530837"
    autor = "J.R.R. Tolkien"
    editora = "HarperCollins"
    titulo = "O Senhor dos Anéis"
    genero_literario = ""  # Gênero vazio

    # Act
    livro = Livro(
        isbn=isbn,
        autor=autor,
        editora=editora,
        titulo=titulo,
        genero_literario=genero_literario
    )

    # Assert
    assert livro.genero_literario == ""


def test_quando_isbn_nao_for_string_deve_lancar_erro():
    """
    Teste para verificar se a criação de um livro com ISBN que não é string
    lança um erro com a mensagem apropriada.
    """
    # Arrange
    isbn = 12345  # ISBN como número, não string
    autor = "J.R.R. Tolkien"
    editora = "HarperCollins"
    titulo = "O Senhor dos Anéis"
    genero_literario = "Fantasia"

    # Act & Assert
    with pytest.raises(TypeError, match="ISBN deve ser uma string."):
        Livro(
            isbn=isbn,
            autor=autor,
            editora=editora,
            titulo=titulo,
            genero_literario=genero_literario
        )


def test_quando_alterar_titulo_deve_atualizar_valor():
    """
    Teste para verificar se a alteração do título de um livro
    atualiza o valor corretamente.
    """
    # Arrange
    livro = Livro(
        isbn="9788532530837",
        autor="J.R.R. Tolkien",
        editora="HarperCollins",
        titulo="O Senhor dos Anéis",
        genero_literario="Fantasia"
    )
    novo_titulo = "O Senhor dos Anéis: A Sociedade do Anel"

    # Act
    livro.titulo = novo_titulo

    # Assert
    assert livro.titulo == novo_titulo


def test_quando_alterar_titulo_para_vazio_deve_lancar_erro():
    """
    Teste para verificar se a alteração do título de um livro para vazio
    lança um erro com a mensagem apropriada.
    """
    # Arrange
    livro = Livro(
        isbn="9788532530837",
        autor="J.R.R. Tolkien",
        editora="HarperCollins",
        titulo="O Senhor dos Anéis",
        genero_literario="Fantasia"
    )

    # Act & Assert
    with pytest.raises(ValueError, match="O título do livro não pode ser vazio."):
        livro.titulo = ""


def test_quando_criar_livro_com_isbn_10_digitos_deve_criar_objeto():
    """
    Teste para verificar se a criação de um livro com ISBN de 10 dígitos
    cria o objeto corretamente.
    """
    # Arrange
    isbn = "8532530834"  # ISBN com 10 dígitos
    autor = "J.R.R. Tolkien"
    editora = "HarperCollins"
    titulo = "O Hobbit"
    genero_literario = "Fantasia"

    # Act
    livro = Livro(
        isbn=isbn,
        autor=autor,
        editora=editora,
        titulo=titulo,
        genero_literario=genero_literario
    )

    # Assert
    assert livro.isbn == isbn


def test_quando_alterar_autor_para_valido_deve_atualizar():
    """
    Verifica se alterar o autor para um valor válido funciona corretamente.
    """
    livro = Livro("9788532530837", "Autor", "Editora", "Título", "Fantasia")
    novo_autor = "Autor Atualizado"

    livro.autor = novo_autor

    assert livro.autor == novo_autor


def test_quando_alterar_autor_para_vazio_deve_lancar_erro():
    """
    Verifica se alterar o autor para vazio lança um erro.
    """
    livro = Livro("9788532530837", "Autor", "Editora", "Título", "Fantasia")

    with pytest.raises(ValueError, match="O autor do livro não pode ser vazio."):
        livro.autor = ""


def test_quando_alterar_editora_para_valido_deve_atualizar():
    """
    Verifica se alterar a editora para um valor válido funciona corretamente.
    """
    livro = Livro("9788532530837", "Autor", "Editora", "Título", "Fantasia")
    nova_editora = "Editora Nova"

    livro.editora = nova_editora

    assert livro.editora == nova_editora


def test_quando_alterar_editora_para_vazio_deve_lancar_erro():
    """
    Verifica se alterar a editora para vazio lança um erro.
    """
    livro = Livro("9788532530837", "Autor", "Editora", "Título", "Fantasia")

    with pytest.raises(ValueError, match="A editora do livro não pode ser vazia."):
        livro.editora = ""


def test_quando_alterar_genero_para_valido_deve_atualizar():
    """
    Verifica se é possível alterar o gênero literário para outro válido.
    """
    livro = Livro("9788532530837", "Autor", "Editora", "Título", "Fantasia")

    livro.genero_literario = "Aventura"

    assert livro.genero_literario == "Aventura"


def test_quando_isbn_contem_letras_deve_lancar_erro():
    """
    Verifica se a criação de um livro com ISBN contendo letras lança um erro.
    """
    # Arrange
    isbn = "978X53253083Y"  # ISBN com letras
    autor = "J.R.R. Tolkien"
    editora = "HarperCollins"
    titulo = "O Senhor dos Anéis"
    genero_literario = "Fantasia"

    # Act & Assert
    with pytest.raises(ValueError, match="ISBN inválido. Deve conter apenas dígitos."):
        Livro(
            isbn=isbn,
            autor=autor,
            editora=editora,
            titulo=titulo,
            genero_literario=genero_literario
        )


def test_quando_isbn_for_none_deve_lancar_erro():
    """
    Verifica se a criação de um livro com ISBN None lança um erro.
    """
    # Arrange
    isbn = None
    autor = "J.R.R. Tolkien"
    editora = "HarperCollins"
    titulo = "O Senhor dos Anéis"
    genero_literario = "Fantasia"

    # Act & Assert
    with pytest.raises(ValueError, match="ISBN não pode ser None."):
        Livro(
            isbn=isbn,
            autor=autor,
            editora=editora,
            titulo=titulo,
            genero_literario=genero_literario
        )


def test_quando_titulo_for_none_deve_lancar_erro():
    """
    Verifica se a criação de um livro com título None lança um erro.
    """
    # Arrange
    isbn = "9788532530837"
    autor = "J.R.R. Tolkien"
    editora = "HarperCollins"
    titulo = None
    genero_literario = "Fantasia"

    # Act & Assert
    with pytest.raises(ValueError, match="O título do livro não pode ser None."):
        Livro(
            isbn=isbn,
            autor=autor,
            editora=editora,
            titulo=titulo,
            genero_literario=genero_literario
        )


def test_quando_autor_for_none_deve_lancar_erro():
    """
    Verifica se a criação de um livro com autor None lança um erro.
    """
    # Arrange
    isbn = "9788532530837"
    autor = None
    editora = "HarperCollins"
    titulo = "O Senhor dos Anéis"
    genero_literario = "Fantasia"

    # Act & Assert
    with pytest.raises(ValueError, match="O autor do livro não pode ser None."):
        Livro(
            isbn=isbn,
            autor=autor,
            editora=editora,
            titulo=titulo,
            genero_literario=genero_literario
        )


def test_quando_editora_for_none_deve_lancar_erro():
    """
    Verifica se a criação de um livro com editora None lança um erro.
    """
    # Arrange
    isbn = "9788532530837"
    autor = "J.R.R. Tolkien"
    editora = None
    titulo = "O Senhor dos Anéis"
    genero_literario = "Fantasia"

    # Act & Assert
    with pytest.raises(ValueError, match="A editora do livro não pode ser None."):
        Livro(
            isbn=isbn,
            autor=autor,
            editora=editora,
            titulo=titulo,
            genero_literario=genero_literario
        )


def test_quando_genero_literario_for_none_deve_ser_string_vazia():
    """
    Verifica se a criação de um livro com gênero literário None
    define o gênero como string vazia.
    """
    # Arrange
    isbn = "9788532530837"
    autor = "J.R.R. Tolkien"
    editora = "HarperCollins"
    titulo = "O Senhor dos Anéis"
    genero_literario = None

    # Act
    livro = Livro(
        isbn=isbn,
        autor=autor,
        editora=editora,
        titulo=titulo,
        genero_literario=genero_literario
    )

    # Assert
    assert livro.genero_literario == ""


def test_representacao_string_do_livro():
    """
    Verifica se a representação string do livro está formatada corretamente.
    """
    # Arrange
    isbn = "9788532530837"
    autor = "J.R.R. Tolkien"
    editora = "HarperCollins"
    titulo = "O Senhor dos Anéis"
    genero_literario = "Fantasia"

    livro = Livro(isbn, autor, editora, titulo, genero_literario)

    # Act
    representacao = str(livro)

    # Assert
    assert representacao == f"Livro: {titulo}, Autor: {autor}, Editora: {editora}, ISBN: {isbn}, Gênero: {genero_literario}"

