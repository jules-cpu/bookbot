import sys
from stats import word_count, char_count, dict_list_sort


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    with open(sys.argv[1]) as f:
        file_contents = f.read()
        count = word_count(file_contents)
        chars = char_count(file_contents)
        sorted_list = dict_list_sort(chars)
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}...")
        print("----------- Word Count ----------")
        print(f"Found {count} total words")
        print("--------- Character Count -------")
        
        for char_dict in sorted_list:
            char = char_dict["char"]
            if char.isalpha():
                print(f"{char}: {char_dict['count']}")
        print("============= END ===============")

main()