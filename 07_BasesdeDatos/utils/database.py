"""
1 In memory database
Guarda libros
2 Formato csv: name,author,read\n
"""
#books = '[]'

def create_book_file():
    with open('books.txt') as file :
        pass

def add_book(name,author):
    with open('books.txt', 'a') as file:
       file.write(f'{name},{author},0\n')


def get_all_books():
    with open('books.txt','r') as file:
        lines =[line.strip().split(',') for line in file.readlines()]#quitaba\n
        #[[name,autor,read],name,autor,read]]
        return [
            {'name' : line[0], 'author': line[1], 'read':line[2]}
            for line in lines
        ]

# _algo quiere decir que es privada
def _save_all_books(books):
    with open('books.txt','w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},0\n")

def mark_book_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
    _save_all_books(books)


# def delete(name) :
#     #No es buena idea
#     for book in books:
#         if book['name'] == name:
#                 books.remove(name)

def delete(name) :
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)

