def sort_on(items):
    return items["num"]

def get_word_count(book_text):
     text = book_text.split()
     word_count = 0
     for word in text:
        word_count += 1
     return f"Found {word_count} total words"
def get_char_count(book_text):
    text = book_text.lower()
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char,0) + 1
    return char_count

def sort_char(book_dict):
    sorted_list = []
    for items in book_dict:
        sorted_list.append({"char": items, "num": book_dict[items]})
    sorted_list.sort(reverse=True,key=sort_on)
    return sorted_list