
def evaluasi_pc(nama, status, ram):
    try:
        ram = int(ram)

        if status.lower() == "normal" and ram >= 8:
            kelayakan = "Layak"
        else:
            kelayakan = "Tidak Layak"

    except ValueError:
        kelayakan = "Format RAM Kacau"

    return {
        "PC": nama,
        "Status": kelayakan
    }


inventaris = []

jumlah = int(input("Masukkan jumlah PC: "))

for i in range(jumlah):
    print("\nData PC ke-", i + 1)

    nama = input("Nama PC: ")
    status = input("Status (Normal/Rusak): ")
    ram = input("Kapasitas RAM (GB): ")

    data = [nama, status, ram]
    inventaris.append(data)

print("\n=== HASIL EVALUASI ===")

for data in inventaris:
    hasil = evaluasi_pc(data[0], data[1], data[2])

    print(
        "{'PC': '" + hasil["PC"] +
        "', 'Status': '" + hasil["Status"] + "'}"
    )
