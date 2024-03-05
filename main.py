def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    letters_dict = count_letters(book_text)
    sorted_letters = sorted_letters_dict(letters_dict)



    print(f"--- Begin report of {book_path} ---")
    print(f"{count_words(book_text)} words found in the document\n")
    for dict in sorted_letters:
        print(f"The '{dict["letter"]}' character was found {dict["num"]}")
    print("--- End report ---")

def get_book_text(book):
    with open(book) as f:
        whole_text = f.read()
        return whole_text
    
def count_words(text):
    words_list = text.split()
    word_count = len(words_list)
    return word_count


def count_letters(text):
    letters_dict = {}
    lowered_text = text.lower()
    for letter in lowered_text:
        if letter in letters_dict:
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1
    return letters_dict

def sort_on(dict):
    return dict["num"]


def sorted_letters_dict(dict):
    letters_and_count = []
    for key in dict:
        if key.isalpha():
            letters_and_count.append({"letter": key, "num": dict[key]})
    letters_and_count.sort(reverse=True, key=sort_on)

    return letters_and_count

main()