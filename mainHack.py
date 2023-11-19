def get_data(file):
    with open(file, "r") as file:
        number_of_len_word = int(file.readline().strip())
        number_of_words_to_decode = int(file.readline().strip())
        number_of_statistical_error = int(file.readline().strip())
        encrypted_text = list(file.read())

    return (
        number_of_len_word,
        number_of_words_to_decode,
        number_of_statistical_error,
        encrypted_text,
    )


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


# print(get_data("messeges7.in")[2])
print(Xor([1, 1, 1, 0]))
