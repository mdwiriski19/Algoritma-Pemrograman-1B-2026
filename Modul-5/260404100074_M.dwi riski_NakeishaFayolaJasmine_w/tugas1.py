def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = int(input("Masukkan hari ke-: "))

if n > 0:
    print("Jumlah pelanggan hari ke-", n, "adalah:", fibonacci(n))
else:
    print("Masukkan bilangan bulat positif!")


