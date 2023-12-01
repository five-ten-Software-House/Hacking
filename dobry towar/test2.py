def main():
    wiadomosc = ""
    with open("messages7.txt", "r") as in_file:
        lines = in_file.readlines()
        dlugosc = int(lines[0])
        liczba_wiad = int(lines[1])
        liczba_znieksztalcen = int(lines[2])

        for ii in range(3, 26):
            wiadomosc = lines[ii].strip()
            wiad_len = len(wiadomosc)
            tabWiad = [int(s) for s in wiadomosc]

            tabROB = [0] * 64
            tabODP = [0] * 64
            tabODP_Ald = [0] * 7
            tabWzor = [0] * 7
            tabWart = [0] * 6
            a = 6
            b = 0
            c = 5
            d = 0
            rob = 0
            ile = 64

            for i in range(128):
                if i == 0:
                    tabWzor = [0] * 8
                b = i
                while b > 0:
                    tabWzor[a] = b % 2
                    b //= 2
                    a -= 1
                a = 6

                for j in range(64):
                    if j == 0:
                        tabWart = [0] * 8
                    d = j
                    while d > 0:
                        tabWart[c] = d % 2
                        d //= 2
                        c -= 1
                    c = 5

                    tabROB[j] = tabWart[0]
                    for x in range(1, 6):
                        tabROB[j] = tabROB[j] ^ tabWart[x]
                    tabROB[j] = not tabROB[j]
                    if tabWzor[0] == 0:
                        tabROB[j] = not tabROB[j]
                    for x in range(1, 7):
                        if tabWzor[x] == 0:
                            tabROB[j] = tabROB[j] ^ tabWart[x - 1]

                    rob += sum(1 for e in range(64) if tabWiad[e] != tabROB[e])

                    if rob < ile:
                        ile = rob
                        tabODP = tabROB[:]
                        tabODP_Ald = tabWzor[:]

            print("".join(str(bit) for bit in tabODP), ile)

if __name__ == "__main__":
    main()
