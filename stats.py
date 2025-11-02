def get_num_words(filepath):
    with open(f"./{filepath}") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_count = len(words)
    return word_count

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
        return character_count

# get_character_count("/books/frankenstein.txt")

def sort_on(dict):
    return dict["num"]

def sorted_characters(character_count):
    letter_list = []
    for characters in character_count:
        if characters.isalpha() == False:
            continue
        else:
            dict_entry = {"char": characters, "num": character_count[characters]}
            letter_list.append(dict_entry)
    letter_list.sort(reverse=True, key=sort_on)
    return letter_list
                
