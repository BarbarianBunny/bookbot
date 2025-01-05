def main():
    book_name = "frankenstein"
    print_word_count()

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