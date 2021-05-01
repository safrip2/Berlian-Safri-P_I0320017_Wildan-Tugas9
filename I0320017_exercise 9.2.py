import sys
kamus = {
    "one": "satu",
    "two": "dua",
    "three": "tiga",
    "four": "empat",
    "five": "lima",
    "six": "enam",
    "seven": "tujuh",
    "eight": "delapan",
    "nine": "sembilan",
    "ten": "sepuluh"
}
def main():
    kata = input("masukkan bilangan dalam bagasa inggris e.g 'nine' ")
    if not kata in kamus.keys():
        print(f"bilangan {kata} tidak ditemukan dalam kamus")
        sys.exit(1)
    print(f"arti dari kata {kata} adalah {kamus[kata]}")
if __name__ == '__main__':
    main()