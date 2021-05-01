import sys
HARI = ("minggu", "senin", "selasa", "rabu", "kamis", "jumat", "sabtu")

def main():
    nohari = int(input("masukkan nomor hari [1..7]: "))
    if nohari < 1 or nohari > 7:
        print(f"tidak ada hari pada no {nohari}")
    print(f"hari ke {nohari} adalah hari {HARI[nohari - 1]}")

if __name__ == '__main__':
    main()