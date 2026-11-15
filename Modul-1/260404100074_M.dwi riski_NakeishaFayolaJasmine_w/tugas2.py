total_belanja = int(input("Masukkan total belanja: Rp"))

print("Total belanja awal: Rp", total_belanja)

if total_belanja % 100000 == 0:
    total_bayar = 0
    print("Selamat! Belanjaan gratis")

elif total_belanja % 50000 == 0:
    total_bayar = total_belanja * 50 / 100
    print("Diskon 50%")

elif total_belanja % 10000 == 0:
    total_bayar = total_belanja * 80 / 100
    print("Diskon 20%")

elif total_belanja >= 200000:
    total_bayar = total_belanja * 90 / 100
    print("Diskon 10%")

else:
    total_bayar = total_belanja
    print("Tidak mendapat diskon")

print("Total yang harus dibayar: Rp", total_bayar)

poin = "Poin Bertambah" if total_bayar > 0 else "Tidak Ada Poin"
print("Status poin:", poin)
