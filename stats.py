def get_number_of_words(book_content):
    number = 0
    words = book_content.split()
    number = len(words)
    return number

def get_number_of_characters(book_content):
    characters = {}

    for char in book_content:
        lowercase = char.lower()
        if lowercase not in characters:
            characters[lowercase] = 1
        else:
            characters[lowercase] += 1
    return characters