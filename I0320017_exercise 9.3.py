A = [
    [23, 11, 54, 38, 76],
    [14, 12, 20, 22, 21],
    [10, 13, 18, 17, 24],
    [35, 33, 39, 32, 29]
]
baris = 4
kolom = 5

def main():
    print("isi array A:")
    i = 0
    while i < baris:
        j = 0
        while j < kolom:
            print("%d" % A[i][j], end='')
            j += 1
        i += 1
        print()
if __name__ == '__main__':
    main()