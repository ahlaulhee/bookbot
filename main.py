def main():
    book = read_book("./books/frankenstein.txt")
    count = count_words(book)
    chars = count_characters(book)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{count} words found in the document")
    for char in chars:
        print(f"the '{char['name']}' character was found {char['num']} times")
    print("--- End report ---")

def read_book(path):
    with open(path) as f:
        return f.read()

def count_words(book_string):
    words = book_string.split()
    return len(words)

def count_characters(book_string):
    chars = {} 
    for char in book_string.lower():
        if char in "abcdefghijklmnopqrstuvwxyz":
            if char in chars:
                chars[char] = chars[char] + 1
            else:
                chars[char] = 0

    chars_arr = []
    for char in chars:
        chars_arr.append({ "name" : char, "num" : chars[char]})
    chars_arr.sort(reverse=True, key=sort_on)
    return chars_arr

def sort_on(dict):
    return dict["num"]

main()
