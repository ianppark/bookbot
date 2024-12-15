def main():
    book_path = "books/frankenstein.txt"
    book_text = open_book_file(book_path)
    word_count = count_words(book_text)
    char_count = count_chars(book_text)
    print_report(word_count, char_count, book_path)
    

def open_book_file(book_path):
    with open(book_path) as f:
        text = f.read()
    return text

def count_words(text):
    words_list = text.split()
    return len(words_list)

def count_chars(text):
    char_counts = {}
    for char in text:
        if char.isalpha():
            if char.lower() not in char_counts.keys():
                char_counts[char.lower()] = 1
            else:
                char_counts[char.lower()] += 1
    

    char_list = []
    for entry in char_counts:
        char_list.append({"char": entry, "count": char_counts[entry]})
    
    char_list.sort(reverse=True, key=sort_on)

    return char_list

def sort_on(dict):
    return dict["count"]


def print_report(word_count, char_count, book_path):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print()
    for entry in char_count:
        char = entry["char"]
        count = entry["count"]
        print(f"The '{char}' character was found {count} times")
    print("--- End report ---")


main()