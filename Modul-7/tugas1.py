
tugas = {}

while True:
    print("\n=== MENU TO-DO LIST ===")
    print("1. Tambah Tugas")
    print("2. Tampilkan Tugas")
    print("3. Tandai Tugas Selesai")
    print("4. Hapus Tugas")
    print("5. Jumlah Tugas")
    print("6. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Nama tugas: ")

        if nama in tugas:
            print("Tugas sudah ada!")
        else:
            tugas[nama] = "Belum selesai"
            print("Tugas berhasil ditambahkan!")

    elif pilihan == "2":
        if len(tugas) == 0:
            print("Belum ada tugas.")
        else:
            print("\nDaftar Tugas:")
            for nama, status in tugas.items():
                print(nama, "-", status)

    elif pilihan == "3":
        nama = input("Tugas yang selesai: ")

        if nama in tugas:
            tugas[nama] = "Selesai"
            print("Tugas berhasil diselesaikan!")
        else:
            print("Tugas tidak ditemukan!")

    elif pilihan == "4":
        nama = input("Tugas yang dihapus: ")

        if nama in tugas:
            del tugas[nama]
            print("Tugas berhasil dihapus!")
        else:
            print("Tugas tidak ditemukan!")

    elif pilihan == "5":
        selesai = list(tugas.values()).count("Selesai")
        belum = len(tugas) - selesai

        print("Tugas selesai:", selesai)
        print("Tugas belum selesai:", belum)

    elif pilihan == "6":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid!")
