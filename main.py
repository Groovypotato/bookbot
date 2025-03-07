from stats import get_num_words
from stats import letter_count
from stats import sorted_words
import sys
filepath = ""

if len(sys.argv) < 2:
    print(" Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    filepath = sys.argv[1]
    

def get_book_text (file_path):
    with open(file_path) as f:
        file_string = f.read()
    return file_string

def main():
    book_text = get_book_text(filepath)
    num_words = get_num_words(book_text)
    count_letters = letter_count(book_text)
    sortedW = sorted_words(count_letters)
    print("============ BOOKBOT ============" )
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for c in sortedW:
        if c["character"].isalpha():
            print(f"{c['character']}: {c['count']}")
    print("============= END ===============")

    
   

main()