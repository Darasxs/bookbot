from stats import *
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
    return book_content

def main():
    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>\n")
        sys.exit(1)
    print("============ *BOOKBOT* ============\n")
    book = get_book_text(sys.argv[1])
    print("Analyzing the book...\n")
    words_number = get_number_of_words(book)
    print("----------- Word Count ----------\n")
    print(f"Found {words_number} total words")
    characters = get_number_of_characters(book)
    print("--------- Character Count -------\n")
    sorted_characters = sort_characters(characters)
    for character in sorted_characters:
        if character["char"].isalpha():
            print(f"{character['char']}: {character['num']}")

main()