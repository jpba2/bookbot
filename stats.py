def get_num_words(filepath):
    with open(f"./{filepath}") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
        print(f"Found {word_count} total words")
    return 

# get_num_words("/books/frankenstein.txt")

def get_character_count(filepath):
    with open(f"./{filepath}") as f:
        file_contents = f.read()
        lower_case = file_contents.lower()
        character_count = {}
        for character in lower_case:
            if character in character_count:
                character_count[character] += 1
            else:
                character_count[character] = 1
        print(character_count)
    return

# get_character_count("/books/frankenstein.txt")

