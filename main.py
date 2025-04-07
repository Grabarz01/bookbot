from stats import get_num_words
from stats import get_dic_of_chars
from stats import get_sorted_dic
import sys

def main():
	if (len(sys.argv) != 2):
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	path_to_book = sys.argv[1]
	file_content = get_book_text(path_to_book)
	dic = get_dic_of_chars(file_content)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {path_to_book}...")
	print("----------- Word Count ----------")
	print(f"Found {get_num_words(file_content)} total words")
	list_dics = get_sorted_dic(dic)
	for dic in list_dics:
		if dic["char"].isalpha():
			print(f"{dic['char']}: {dic['num']}")

def get_book_text(filepath):
	with open(filepath) as f:
		return(f.read())



main()