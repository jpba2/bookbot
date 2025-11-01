def get_book_text(filepath):
    with open(f"./{filepath}") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        print(f"Found {word_count} total words")
    return

get_book_text("books/frankenstein.txt")