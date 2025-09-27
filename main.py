from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    # book_path = "books/frankenstein.txt"
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    with open(book_path) as f:
        file_contents = f.read()
    word_count = get_num_words(file_contents)
    chars = character_count(file_contents)

    chars_list = create_sorted_dict(chars)

    print_report(book_path, word_count, chars_list)

main()
