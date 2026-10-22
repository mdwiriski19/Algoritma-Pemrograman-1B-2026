
jumlah_penuh = 0

for i in range(1, 11):
    print("\nMahasiswa ke-", i)

    nama = input("Masukkan nama: ")
    ipk = float(input("Masukkan IPK: "))

    if ipk < 3.00:
        print(nama, "tidak memenuhi syarat beasiswa.")
        continue

    penghasilan = int(input("Penghasilan orang tua per bulan: "))

    if penghasilan <= 3000000:
        if jumlah_penuh >= 3:
            print("Kuota beasiswa penuh sudah habis.")
            break
        else:
            print(nama, "mendapatkan beasiswa penuh.")
            jumlah_penuh += 1

    elif penghasilan <= 5000000:
        print(nama, "mendapatkan beasiswa sebagian.")

    else:
        print(nama, "tidak mendapatkan beasiswa.")

    if jumlah_penuh == 3:
        print("Kuota beasiswa penuh sudah terpenuhi.")
        break

print("\nJumlah penerima beasiswa penuh:", jumlah_penuh)
