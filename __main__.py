from biblioteca import *
def main():
    biblioteca = Biblioteca()
    aluno = Aluno("João", "12345678900")

    while True:
        print("\n====== SISTEMA DE BIBLIOTECA ======")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Listar livros disponíveis")
        print("4 - Buscar livro")
        print("5 - Emprestar livro")
        print("6 - Devolver livro")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            isbn = input("ISBN: ")
            biblioteca.cadastrar_livro(titulo, autor, isbn)

        elif opcao == "2":
            biblioteca.listar_livros()

        elif opcao == "3":
            biblioteca.listar_disponiveis()

        elif opcao == "4":
            titulo = input("Digite o título: ")
            livro = biblioteca.buscar_titulo(titulo)
            print(livro if livro else "Livro não encontrado")

        elif opcao == "5":
            titulo = input("Digite o título do livro: ")
            biblioteca.emprestar(aluno, titulo)

        elif opcao == "6":
            titulo = input("Digite o título do livro: ")
            biblioteca.devolver(aluno, titulo)

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()