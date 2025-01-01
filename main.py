def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    return file_contents

def wordcount(file_contents):
    words = file_contents.split()
    word_counter = len(words)
    return word_counter

def char_count(file_contents):
    lower_case = file_contents.lower()
    char_dict = {}
    
    for char in lower_case:
        if char.isalpha():
            if char in char_dict:
                char_dict[char] += 1
            else:
                char_dict[char] = 1
    
    
    char_dict_list = [{'character':k, 'count': v} for k, v in char_dict.items()]
    return char_dict_list

def char_sort(char_entry):
    return char_entry["count"]

file_contents = main()
word_count = wordcount(file_contents)
character_count = char_count(file_contents)
character_count.sort(reverse=True, key=char_sort)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{word_count} words found in the document\n")

for entry in character_count:
    print(f"The '{entry['character']}' character was found '{entry['count']}'")