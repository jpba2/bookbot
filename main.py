def get_book_text(filepath):
    with open(f"./{filepath}") as f:
        file_contents = f.read()
        print(file_contents)
    return

get_book_text("books/frankenstein.txt")