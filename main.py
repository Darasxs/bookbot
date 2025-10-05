from stats import *

def get_book_text(filepath):
    with open(filepath) as f:
        book_content = f.read()
    return book_content

def main():
    print("============ *BOOKBOT* ============\n")
    book = get_book_text("/home/daras/workspace/bookbot/books/frankenstein.txt")
    print("Analyzing the book...\n")
    words_number = get_number_of_words(book)
    print("----------- Word Count ----------\n")
    print(f"Found {words_number} total words")
    characters = get_number_of_characters(book)
    print("--------- Character Count -------\n")
    sorted_characters = characters.sort(reverse = True, key=value)
    print(sorted_characters)

main()