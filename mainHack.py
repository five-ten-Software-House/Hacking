def Xor(arr):
    result = 0
    i = 0
    j = i + 1
    while j < len(arr):
        if arr[i] in [0, 1] and arr[j] in [0, 1]:
            result = int(arr[i] != arr[j])
            arr[i] = result
            i += 1
            j = i + 1
        else:
            return "Invalid input"
    return result


def Not(x):
    if x in (0, 1):
        if x == 1:
            return 0
        else:
            return 1


def decode(len_of_original_word, number_of_words_to_decode, number_of_error, encrypted_word):
    len_of_original_word += 1
    decoded_message = []
    i = 0
    
    
    

print(Xor([1, 1, 1, 0, 1, 1, 0]))

print(len("01100110100100"))

with open("file", "r") as file:
        N = len_of_original_word = int(file.readline().strip())
        n = number_of_words_to_decode = int(file.readline().strip())
        e = number_of_error = int(file.readline().strip())
        encrypted_text = list(file.read())