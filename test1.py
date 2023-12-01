def decode_message(length, num_messages, max_bits, distorted_messages):
    # Funkcja do obliczania wartości logicznej formuły ϕA dla danego wartościowania
    def calculate_phiA(p1, p2, p3):
        return (((not p3) ^ p2) ^ ((not ((not p1) ^ p3)) ^ (not p3)))

    decoded_messages = []

    for distorted_message in distorted_messages:
        # Inicjalizacja wartości na None, oznacza brak rozwiązania
        solution = None

        # Sprawdzenie wszystkich możliwych wartościowań
        for k in range(8):
            p1 = (k >> 2) & 1
            p2 = (k >> 1) & 1
            p3 = k & 1

            # Obliczenie wartości logicznej formuły ϕA
            phiA_value = calculate_phiA(p1, p2, p3)

            # Sprawdzenie, czy zakłócona wiadomość pasuje do danego wartościowania
            if bin(phiA_value).count('1') == distorted_message.count('1'):
                if solution is None:
                    solution = bin(k)[2:].zfill(3)
                else:
                    # Jeśli istnieje więcej niż jedno dopasowanie, to wynik jest niejednoznaczny
                    solution = None
                    break

        # Dodanie odkodowanej wiadomości do listy wyników
        if solution is not None:
            decoded_messages.append(solution)
        else:
            decoded_messages.append("Błąd: Wiadomość niejednoznaczna.")

    return decoded_messages


# Przykładowe użycie
length = 4
num_messages = 1
max_bits = 1
distorted_messages = ["11101001"]

result = decode_message(length, num_messages, max_bits, distorted_messages)
print("Oczekiwany wynik:", ["0111"])
print("Wynik funkcji:", result)
