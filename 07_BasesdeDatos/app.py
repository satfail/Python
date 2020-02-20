from utils import database


INPUT_CHOICE = """
Enter:
- 'a' añadir
- 'l' listar
- 'r' marcar como leido
- 'd' borrar
- 'q' salir
Elige : """


def menu ():
    database.create_book_file()
    user_input = input(INPUT_CHOICE)
    while(user_input!='q'):
        
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Error en el comando, intentelo otra vez")
        user_input = input(INPUT_CHOICE)


def prompt_add_book():
     name = input('Introduzca el nombre : ')
     author = input('Introduzca el autor : ')
     database.add_book(name,author)


def list_books():
    books = database.get_all_books()
    for book in books:
        read = 'YES' if book['read']==1 else 'NO'
        print(f"{book['name']} escrito por {book['name']} leido: {read}")


def prompt_read_book():
    name = input('Introduzca el nombre : ')
    database.mark_book_read(name)


def prompt_delete_book():
     name = input('Introduzca el nombre : ')
     database.delete(name)


menu()