import math

def main():
    try:
        wiadomosc = ""
        with open("messages7.txt", 'r') as in_file:
            lines = in_file.readlines()

        if len(lines) < 23:
            print("Error: Insufficient lines in the file.")
            return

        dlugosc, liczba_wiad, liczba_znieksztalcen = 0, 0, 0

        for ii in range(23):
            wiadomosc = lines[ii].strip()

            if ii == 0:
                dlugosc = int(wiadomosc)
                continue
            elif ii == 1:
                liczba_wiad = int(wiadomosc)
                continue
            elif ii == 2:
                liczba_znieksztalcen = int(wiadomosc)
                continue

            wiad_len = len(wiadomosc)
            tabWiad = [0] * wiad_len

            for jj in range(len(wiadomosc)):
                s = wiadomosc[jj]
                tabWiad[jj] = ord(s) - ord('0')

        tabROB = [0]*64
        tabODP = [0]*64
        tabODP_Ald = [0]*7
        tabWzor = [0]*7
        tabWart = [0]*6
        a, b, c, d, rob, ile = 6, 0, 5, 0, 0, 64

        for i in range(128):
            if i == 0:
                tabWzor = [0]*8
            b = i
            while b > 0:
                tabWzor[a] = b % 2
                b //= 2
                a -= 1
            a = 6

            for j in range(64):
                if j == 0:
                    tabWart = [0]*8
                d = j
                while d > 0:
                    tabWart[c] = d % 2
                    d //= 2
                    c -= 1
                c = 5

                tabROB[j] = tabWart[0]
                for x in range(1, 6):
                    tabROB[j] ^= tabWart[x]
                tabROB[j] = not tabROB[j]
                if tabWzor[0] == 0:
                    tabROB[j] = not tabROB[j]
                for x in range(1, 7):
                    if tabWzor[x] == 0:
                        tabROB[j] ^= tabWart[x-1]

            for e in range(64):
                if tabWiad[e] != tabROB[e]:
                    rob += 1
            if rob < ile:
                ile = rob
                tabODP = tabROB.copy()
                tabODP_Ald = tabWzor.copy()
            rob = 0

        print(''.join(map(str, tabODP)), ile)

    except FileNotFoundError:
        print("Error: File 'messages7.txt' not found.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()