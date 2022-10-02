from view import (show_menu, get_search_surname, get_search_room, get_search_score, 
get_new_pupil, get_remove_id, get_file_name)
from model import (write_txt, add_csv, write_csv, read_csv, find_by_surname, find_by_room, find_by_score, 
add_pupil, remove_pupil)

def work_with_book():
    choice = show_menu()
    book = read_csv('Lesson08/book.csv')

    while(choice != 7):
        if choice == 1:
            surname = get_search_surname()
            print(find_by_surname(book, surname))
        elif choice == 2:
            room = get_search_room()
            print(find_by_room(book, room))
        elif choice == 3:
            score = get_search_score()
            print(find_by_score(book, score))
        elif choice == 4:
            pupil_data = get_new_pupil()
            add_pupil(book, pupil_data)
            add_csv('Lesson08/book.csv', book)
        elif choice == 5:
            pupil_id = get_remove_id()
            remove_pupil(book, pupil_id)
            write_csv('Lesson08/book.csv', book)
        elif choice == 6:
            file_name = get_file_name()
            write_txt(file_name, book)
        choice = show_menu()