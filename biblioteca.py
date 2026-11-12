class Aluno:
    def __init__(self,nome:str,cpf:str):
        self.__nome = nome
        self.__cpf = cpf
        self.livros_emprestados = []
class Livro:
    def __init__(self,titulo:str,autor:str,isbn:int):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponivel = True

    def __str__(self):
        return f'Autor: {self.autor}\n Titulo: {self.titulo}\n ISBN: {self.isbn}\n Disponivel: {'SIM' if self.disponivel else 'NÃO'}'
    
class Biblioteca:
    def __init__(self):
        self.livros = []

    def cadastrar_livro(self,titulo,autor,isbn):
        livro = Livro(titulo,autor,isbn)
        self.livros.append(livro)


    def emprestar(self,aluno:Aluno,titulo:str):
        livro = self.buscar_titulo(titulo)
        if not livro:
            print("Livro nao disponivel ou nao existe")
        elif not livro.disponivel:
            print("Livro nao esta disponivel ou foi emprestado")
        else:
            aluno.livros_emprestados.append(livro)
            livro.disponivel = False
            print("Livro emprestado com sucesso!")
        

    def devolver(self,aluno:Aluno,titulo:str):
        livro = self.buscar_titulo(titulo)
        if not livro:
            print("Livro nao disponivel ou nao existe")
        elif livro.disponivel:
            print("Voce nao pode devolver um livro disponivel")
        else:
            aluno.livros_emprestados.remove(livro)
            livro.disponivel = True
            print("Livro devolvido com sucesso")

    def listar_livros(self):
        for livros in self.livros:
            print('------------')
            print(f'{livros}')

    def listar_disponiveis(self):
        for livros in self.livros:
            if livros.disponivel:
                print(livros)


    def buscar_titulo(self,texto):
        for livros in self.livros:
            if livros.titulo == texto:
                return livros
        return None
        