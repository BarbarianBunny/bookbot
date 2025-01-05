def main():
    book_name = "frankenstein"
    print_word_count(book_name)
    text = get_text(book_name)
    character_counts = get_character_counts(text)
    print_sorted_dict(character_counts)
    
def get_character_counts(text):
    text = text.lower()
    chars = {}
    for char in text:
        if char in chars:
            continue
        chars[char] = text.count(char)
    return chars

def print_sorted_dict(dict):
    for key, value in sorted(dict.items()):
        print(key + ": " + str(value))

def get_text(book_name):
    book_path = "books/" + book_name.lower() + ".txt"
    with open(book_path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def print_word_count(book_name):
    text = get_text(book_name)
    word_count = get_word_count(text)
    print(f"{book_name.title()} has {word_count} words.")


main()