from utils2 import database_json

user_choice = """
Enter
'a' to add a new book
'l' to list all book
'r' to mark book as read
'd' to delete a book
'q' to quit

Your choice: """

def menu():
    database_json.create_book_table()
    user_input = input(user_choice)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command please try again.")

        user_input = input(user_choice)

def prompt_add_book():
    name = input("Enter the new book name: ").title()
    author = input("Enter the new book author: ").title()
    database_json.add_book(name, author)

def list_books():
    for book in database_json.get_all_books():
        read = "Yes" if book["Read"] == True else "No"
        print(f"{book['name']} by {book['author']}, Read: {read}")


def prompt_read_book():
    name = input("Enter the name of the book you just finished reading: ").title()
    database_json.mark_book_as_read(name)


def prompt_delete_book():
    name = input("Enter the name of book to delete: ").title()
    database_json.delete_book(name)


menu()