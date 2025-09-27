def get_num_words(text):
    return len(text.split())

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
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print(f"----------- Word Count ----------")
    print(f"Found {words} total words")
    print(f"--------- Character Count -------")
    for c in chars:
        print(f"{c["char"]}: {c["num"]}")
    print("============= END ===============")