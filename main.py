from stats import get_word_count, get_char_count, sort_char
import sys


def get_book_text(book_path):
    file_contents = ""
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    book_char_count = sort_char(get_char_count(book_text))

    print("============ BOOKBOT ============")
    print("Analyzing book found at ./books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_word_count(book_text)} total words")
    print("--------- Character Count -------")
    for items in book_char_count:
        if items.get("char").isalpha():
            print(f"{items.get("char")}: {items.get("num")}")
    print("============= END ===============")
main()