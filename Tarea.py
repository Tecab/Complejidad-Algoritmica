def word_counter(arr, start_idx, end_idx):
    count = 0
    for i in range(start_idx, end_idx + 1):
        words = arr[i].split()
        count += len(words)
    return count

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam arcu arcu, euismod mollis rhoncus quis, egestas at leo. Maecenas luctus neque nulla, vel imperdiet lacus ultrices vel. Mauris eget eros vel lacus molestie blandit."
array = text.split()
result_a = word_counter(array, 0, len(array) - 1)
print(result_a)

def word_count_per_line(text):
    lines = text.split('\n')
    for line in lines:
        words = line.split()
        print(len(words))

txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n Nam arcu arcu, euismod mollis rhoncus quis, egestas at leo.\n Maecenas luctus neque nulla, vel imperdiet lacus ultrices vel."
word_count_per_line(txt)

def word_count_in_file(file):
    try:
        with open(file, 'r') as file_content:
            content = file_content.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"El archivo {file} no fue encontrado.")
        return 0

file_name = "lorem.txt"
result_c = word_count_in_file(file_name)
print(result_c)
