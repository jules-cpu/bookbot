def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def char_count(file_contents):
    text = file_contents.lower()
    char_count_dict = {}
    for char in text:
        if char not in char_count_dict:
            char_count_dict[char] = 1
        else:
            char_count_dict[char] += 1
    return char_count_dict

def sort_on(dict):
    return dict["count"]

def dict_list_sort(char_count_dict):
    chars_list = []
    for char in char_count_dict:
        char_dict = {"char": char, "count": char_count_dict[char]}
        chars_list.append(char_dict)
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list        







