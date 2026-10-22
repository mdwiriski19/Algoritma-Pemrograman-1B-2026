suhu = float(input("Masukkan suhu reaktor : "))
tekanan = float(input("Masukkan tekanan gas : "))

print("\n=== MONITORING REAKTOR ===")
print("Suhu Reaktor   :", suhu, )
print("Tekanan Gas    :", tekanan, )

if suhu > 1000:
    if tekanan > 50:
        status = "MELTDOWN! SEGERA EVAKUASI!"
    else:
        status = "Bahaya Suhu: Segera Turunkan Daya!"

elif suhu > 500:
    if tekanan > 30:
        status = "Tekanan Tidak Stabil"
    else:
        status = "Operasi Reaktor Normal"
else:
    status = "Reaktor Belum Cukup Panas"

print("Status Bahaya  :", status)

pompa = "Pompa Maksimal" if suhu > 800 else "Pompa Normal"

print("Status Pompa   :", pompa)