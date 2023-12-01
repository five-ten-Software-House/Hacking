use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() -> io::Result<()> {
    let mut wiadomosc = String::new();
    let file = File::open("messages7.txt")?;
    let reader = io::BufReader::new(file);
    let mut lines = reader.lines();

    let mut dlugosc = 0;
    let mut liczba_wiad = 0;
    let mut liczba_znieksztalcen = 0;

    for ii in 0..23 {
        wiadomosc = lines.next().unwrap_or_else(|| Ok("".to_string()))?;

        if ii == 0 {
            dlugosc = wiadomosc.trim().parse().unwrap();
        } else if ii == 1 {
            liczba_wiad = wiadomosc.trim().parse().unwrap();
        } else if ii == 2 {
            liczba_znieksztalcen = wiadomosc.trim().parse().unwrap();
        } else {
            let wiad_len = wiadomosc.len();
            let mut tabWiad: Vec<i32> = vec![0; wiad_len];

            for (jj, s) in wiadomosc.chars().enumerate() {
                tabWiad[jj] = s.to_digit(10).unwrap() as i32;
            }

            let mut tabROB: Vec<i32> = vec![0; 64];
            let mut tabODP: Vec<i32> = vec![0; 64];
            let mut tabODP_Ald: Vec<i32> = vec![0; 7];
            let mut tabWzor: Vec<i32> = vec![0; 7];
            let mut tabWart: Vec<i32> = vec![0; 6];
            let mut a = 6;
            let mut b = 0;
            let mut c = 5;
            let mut d = 0;
            let mut rob = 0;
            let mut ile = 64;

            for i in 0..128 {
                if i == 0 {
                    tabWzor = vec![0; 8];
                }
                b = i;
                while b > 0 {
                    tabWzor[a] = b % 2;
                    b /= 2;
                    a -= 1;
                }
                a = 6;

                for j in 0..64 {
                    if j == 0 {
                        tabWart = vec![0; 8];
                    }
                    d = j;
                    while d > 0 {
                        tabWart[c] = d % 2;
                        d /= 2;
                        c -= 1;
                    }
                    c = 5;

                    tabROB[j] = tabWart[0];

                    for x in 1..6 {
                        tabROB[j] ^= tabWart[x];
                    }

                    tabROB[j] = !tabROB[j];
                    if tabWzor[0] == 0 {
                        tabROB[j] = !tabROB[j];
                    }

                    for x in 1..7 {
                        if tabWzor[x] == 0 {
                            tabROB[j] ^= tabWart[x - 1];
                        }
                    }
                }

                for e in 0..64 {
                    if tabWiad[e] != tabROB[e] {
                        rob += 1;
                    }
                }
                if rob < ile {
                    ile = rob;
                    tabODP.clone_from_slice(&tabROB);
                    tabODP_Ald.clone_from_slice(&tabWzor);
                }
                rob = 0;
            }

            for i in 0..64 {
                print!("{}", tabODP[i]);
            }
            print!(" {}", ile);
            println!();
        }
    }

    Ok(())
}
