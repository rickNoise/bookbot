from stats import count_words, get_character_counts

FILE_PATH = "books/frankenstein.txt"

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    character_count_dict = get_character_counts(get_book_text(FILE_PATH))
    print(f"{count_words(get_book_text(FILE_PATH))} words found in the document")
    print(character_count_dict)

if __name__ == "__main__":
    main()