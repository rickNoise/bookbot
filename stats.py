def count_words(string):
    """Count the number of words in the string."""
    return len(string.split())

def get_character_counts(input_string):
    """This function takes the text from the book as a string, and returns the number of times each character, (including symbols and spaces), appears in the string.
    Convert any character to lowercase using the .lower() method, we don't want duplicates.
    Use a dictionary of String -> Integer.

    >>> get_character_counts("stringSTRING")
    {'s': 2, 't': 2, 'r': 2, 'i': 2, 'n': 2, 'g': 2}
    """
    dict = {}
    for char in input_string.lower():
        if char not in dict.keys():
            # add the char and initialise with a count of 1
            dict[char] = 1
        else:
            # increment the char's counter by 1
            dict[char] += 1
    return dict

def dict_sorter(dict):
    def sorting_fn(i):
        return i["value"]
    list = []
    for key, value in dict.items():
        list.append({"key": key, "value": value})
    list.sort(reverse=True, key=sorting_fn)
    return list