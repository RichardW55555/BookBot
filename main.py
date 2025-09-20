import sys
from stats import get_num_words, get_charecter_count, sort_charecter_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    charecters = get_charecter_count(text)
    report = sort_charecter_count(charecters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in report:
        ch = char["char"]
        cnt = char["num"]
        if str(ch).isalpha():
            print(f"{ch}: {cnt}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()