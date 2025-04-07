def get_num_words(file_content):
	words = file_content.split()
	return (len(words))

def get_dic_of_chars(file_content):
	lower_case = file_content.lower()
	dic_result = {}
	for letter in lower_case:
		if(not (letter in dic_result)):
			dic_result[letter] = 1
		else:
			dic_result[letter] += 1
	return (dic_result)
	
def sort_on(dict):
	return dict["num"]

def get_sorted_dic(dic):
	list_of_dics = []
	for key in dic:
		list_of_dics.append({"char": key, "num": dic[key]})
	list_of_dics.sort(reverse=True, key=sort_on)
	return list_of_dics
	
	
		