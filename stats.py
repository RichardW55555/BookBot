def get_num_words(text):
    return len(text.split())

def get_charecter_count(book):
    text = book.lower()
    charecters = {}
    for charecter in text:
        if charecter in charecters:
            charecters[charecter] += 1
        else:
            charecters[charecter] = 1
    return charecters

def sort_charecter_count(charecters):
    sorted_charecters = []
    for key, value in charecters.items():
        sorted_charecters.append({"char": key, "num": value})
    def sort_on(item):
        return item["num"]
    sorted_charecters.sort(key = sort_on, reverse = True)
    return sorted_charecters