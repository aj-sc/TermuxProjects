from db_operations import get_db, add_note, list_active_notes

def main() -> None:
    while True:
        print("""Welcome to your home app, press the desired option:

1 - Add a note
2 - Show current notes
3 - Update a note
4 - Delete a note
5 - Exit app

""")

        nav_input = input("Choose an option: ")

        match int(nav_input):
            case 1:
                title = input("Write the title: ")
                body = input("Write the body: ")
                data = get_db()
                add_note(data, title, body)

            case 2:
                data = get_db()
                list_active_notes(data)

            case 3:
                print("Update a note (not implemented yet).")

            case 4:
                print("Delete a note (not implemented yet).")

            case 5:
                print("Exiting app...")
                break

            case _:
                print("Invalid option, try again.")


if __name__ == "__main__":
    main()
