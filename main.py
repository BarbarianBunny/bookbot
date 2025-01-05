import string

def main():
    book_name = "frankenstein"
    text = get_text(book_name)
    word_count = get_word_count(text)
    character_counts = get_character_counts(text)
    print_book_report(book_name, word_count, character_counts)
    
def print_book_report(book_name, word_count, character_counts):
    print(f"--- Begin report of {book_name} ---\n")
    print(f"{word_count} words found in the document\n")
    print("Letters found:")
    for key, value in sorted(character_counts.items()):
        if key in string.ascii_lowercase:
            print(f"The '{key}' character was found {value} times")
    print()
    print("Numbers found:")
    for key, value in sorted(character_counts.items()):
        if key in string.digits:
            print(f"The '{key}' character was found {value} times")
    print("\n--- End Report ---")

def get_character_counts(text):
    text = text.lower()
    chars = {}
    for char in text:
        if char in chars:
            continue
        chars[char] = text.count(char)
    chars.pop("\n", None)
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