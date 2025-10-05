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

def sort_on(characters_list):
    return characters_list["num"]

def sort_characters(characters):
    characters_list = []
    for key, value in characters.items():
        characters_list.append({"char": key, "num": value})
    characters_list.sort(reverse=True, key=sort_on)
    return characters_list