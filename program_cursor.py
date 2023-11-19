def hamming_distance(str1, str2):
    return sum(c1 != c2 for c1, c2 in zip(str1, str2))

def generate_all_binary_strings(length):
    return [bin(i)[2:].zfill(length) for i in range(2**length)]

def decode_message(N, n, max_changes, messages):
    original_length = N + 1
    decoded_messages = []

    for message in messages:
        changed_bits = int(message, 2)
        best_match = None
        min_distance = float('inf')

        for binary_string in generate_all_binary_strings(original_length):
            current_distance = hamming_distance(message, binary_string)
            if current_distance <= max_changes and current_distance < min_distance:
                best_match = binary_string
                min_distance = current_distance

        if best_match is not None:
            decoded_messages.append(best_match)
        else:
            decoded_messages.append("No unique original message found")

    return decoded_messages

if __name__ == "__main__":
    with open("input.txt", "r") as file:
        N = int(file.readline().strip())
        n = int(file.readline().strip())
        max_changes = int(file.readline().strip())
        messages = [file.readline().strip() for _ in range(n)]

    result = decode_message(N, n, max_changes, messages)

    with open("output.txt", "w") as output_file:
        for decoded_message in result:
            output_file.write(decoded_message + "\n")

    print("Odkodowane wiadomości zostały zapisane do pliku 'output.txt'.")
