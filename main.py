def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
    word_count = count_words(file_contents)
    chars = character_count(file_contents)

    chars_list = create_sorted_dict(chars)

    print_report(book_path, word_count, chars_list)

def count_words(file_contents):
    word_count = 0
    words = file_contents.split()
    return len(words)

def character_count(file_contents):
    char_dict = {}
    for c in file_contents:
        lower_c = c.lower()
        if lower_c.isalpha():  
            if lower_c in char_dict:
                char_dict[lower_c] += 1
            else:
                char_dict[lower_c] = 1

    return char_dict

def create_sorted_dict(dict):
    new_dict = []
    for key in dict:
        new_entry = {"char": key, "num": dict[key]}
        new_dict.append(new_entry)
    new_dict.sort(reverse=True, key=sort_on)
    return new_dict

def sort_on(dict):
    return dict["num"]

def print_report(path, words, chars):
    print(f"--- Begin report of {path} ---")
    print(f"{words} words found in the document")
    print()
    for c in chars:
        print(f"The {c["char"]} character was found {c["num"]} times")
    print("--- End report ---")

main()