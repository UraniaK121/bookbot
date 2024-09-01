import string
def main():
    import string
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        string_simple = file_contents.lower()
        count_words(file_contents)
        dicty = count_letter(string_simple)
        listy = []
        for key in dicty:
            listy.append({"name": key, "num":dicty[key]})

        listy.sort(reverse=True, key=sort_on)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{count_words(file_contents)} words found in the document")
        for item in listy:
            print(f"The {item["name"]} was found {item["num"]} times")
        print("--- End report ---")

def count_letter(string_simple):
    letters = [x for x in string_simple]
    alphabet = list(string.ascii_lowercase)
    dict = {}
    count =0
    for alpha in alphabet:
        for letter in letters:
            if alpha == letter:
               count +=1
        dict[alpha]=count
        count =0
    print(dict)
    return dict

def count_words(string_simple):
    words = string_simple.split()
    print(len(words))
    return len(words)

def sort_on(dict):
    return dict["num"]

count_letter("a")

main()

