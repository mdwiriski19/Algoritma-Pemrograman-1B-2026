anggota = []
while True:
    nama = input("Masukkan nama anggota (ketik selesai untuk berhenti): ")

    if nama.lower() == "selesai":
        break

    anggota.append(nama)

print("\nDaftar anggota:", anggota)

for nama in anggota:
    if nama.lower() == "admin" or len(nama) < 4:
        print(nama, "tidak valid")
    else:
        print(nama, "valid")

hapus = input("\nMasukkan nama penyusup yang ingin dihapus: ")

if hapus in anggota:
    anggota.remove(hapus)
    print("Nama", hapus, "berhasil dihapus.")
else:
    print("Nama", hapus, "tidak ditemukan dalam daftar.")

print("Daftar anggota akhir:", anggota)
