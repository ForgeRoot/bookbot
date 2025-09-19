from stats import get_word_count, get_char_count, sort_char_count
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    text = get_book_text(sys.argv[1])
    num_words = get_word_count(text)
    chars_dict = get_char_count(text)
    chars_sorted = sort_char_count(chars_dict)
    print_report(sys.argv[1], num_words, chars_sorted)


def print_report(book_path, num_words, chars_sorted):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for pair in chars_sorted:
        if pair["char"].isalpha():
            print(f"{pair["char"]}: {pair["num"]}")
    print("============= END ===============")


def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents


main()