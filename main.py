import sys
from stats import get_book_text
from stats import num_count
from stats import letter_count
from stats import sorted_list
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print("============ BOOKBOT ============ " )
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        text= num_count(sys.argv[1])
        print(f"Found {text} total words")
        print("--------- Character Count -------")
        letters= letter_count(sys.argv[1])
        yeppers= sorted_list(sys.argv[1])
        for yep in yeppers:
            ch = yep["alph"]
            if ch.isalpha():
                print(f"{ch}: {yep["num"]}")
main()
