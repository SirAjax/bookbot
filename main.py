def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = print_word_count(text)
    character_dictionary = character_counter(text)
    print(f"{count} words found in the document")
    create_report(character_dictionary)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def print_word_count(text_to_print):
    words = text_to_print.split()
    return len(words)

def character_counter(text_to_count):
    char = {}
    for c in  text_to_count:
        lowered_character = c.lower()
        if lowered_character in char:
            char[lowered_character] += 1
        else:
            char[lowered_character] = 1
    return char
    
def create_report(character_dictionary):
    for key, value in character_dictionary.items():
        print(f"The {key} character appears {value} times")

main()

