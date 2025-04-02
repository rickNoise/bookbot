import sys
from stats import count_words, get_character_counts, dict_sorter

# ensure user has entered appropriate number of args from CLI
if len(sys.argv) != 2:
    print("Usage: Usage: python3 main.py <path_to_book>")
    sys.exit(1)

FILE_PATH = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    character_count_dict = get_character_counts(get_book_text(FILE_PATH))
    sorted_dict_list = dict_sorter(character_count_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {FILE_PATH}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(get_book_text(FILE_PATH))} total words")
    print("--------- Character Count -------")
    for dict in sorted_dict_list:
        if dict["key"].isalpha():
            print(f"{dict["key"]}: {dict["value"]}")
    print("============= END ===============")

if __name__ == "__main__":
    main()