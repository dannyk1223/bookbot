def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    count_words(book_text)

def get_book_text(book):
    with open(book) as f:
        whole_text = f.read()
        print(whole_text)
        return whole_text
    
def count_words(text):
    words_list = text.split()
    word_count = len(words_list)
    print(word_count)
    return word_count

main()