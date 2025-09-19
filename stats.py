def get_word_count(textbook):
    list_of_words = textbook.split()
    return len(list_of_words)

def get_char_count(textbook):
    lower_textbook = textbook.lower()
    char_count = {}
    for char in lower_textbook:
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_char_count(char_dict):
    chars = []
    for char in char_dict:
        pair = {}
        pair["char"] = char
        pair["num"] = char_dict[char]
        chars.append(pair)
    chars.sort(reverse=True, key=sort_on)
    return chars
