baris = int(input("Masukkan jumlah baris lampu: "))
jumlah = int(input("Masukkan jumlah lampu setiap baris: "))

for b in range(1, baris + 1):
    print("Baris", b)

    for l in range(1, jumlah + 1):
        if l % 3 == 0:
            print("Lampu", l, "mengalami gangguan")
        else:
            print("Lampu", l, "berfungsi normal")

print("Periksa sumber listrik utama taman!")
