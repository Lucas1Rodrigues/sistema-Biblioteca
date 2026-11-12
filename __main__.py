from biblioteca import *
def main():
    biblioteca = Biblioteca()
    biblioteca.cadastrar_livro("Harry potter","jk rowling",123)
    al1 = Aluno("Lucas",7080545246)
    biblioteca.emprestar(al1,"Harry potter")
    biblioteca.listar_livros()

if __name__ == "__main__":
    main()