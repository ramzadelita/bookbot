BOOK_PATH = "books/frankenstein.txt"

def count_letters(text):
    letter_counts = {}
    for letter in text.lower():
        if letter in letter_counts.keys():
            letter_counts[letter] += 1
        else:
            letter_counts[letter] = 1

    return letter_counts

def print_report(path, word_count, letter_list):
    print(f"--- Begin report of {path} ---")
    print(f"{word_count} words found in the document\n")

    for letter, count in letter_list:
        if str.isalpha(letter):
            print(f"The '{letter}' character was found {count} times")

    return None

# Open book and print report
with open(BOOK_PATH) as f:
    file_contents = f.read()
    word_count = len(file_contents.split())
    letter_dict = count_letters(file_contents)
    letter_list = list(letter_dict.items())
    letter_list.sort()

    print_report(BOOK_PATH, word_count, letter_list)


