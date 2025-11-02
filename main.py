from stats import (get_num_words,
                   get_character_count,
                   sorted_characters,
                   sort_on
)

file_path = "books/frankenstein.txt"

def book_report(file_path):
    word_count = get_num_words(file_path)
    character_count = sorted_characters(get_character_count(file_path))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for i in range(0, len(character_count)):
        print(f"{character_count[i]["char"]}: {character_count[i]["num"]}")
    print("============= END ===============")
    

book_report(file_path)
