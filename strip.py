def terbilang(n):
    angka = ["", "Satu", "Dua", "Tiga", "Empat", "Lima",
             "Enam", "Tujuh", "Delapan", "Sembilan",
             "Sepuluh", "Sebelas"]
    hasil = ""

    if n < 12:
        hasil = angka[n]
    elif n < 20:
        hasil = terbilang(n % 10) + " Belas"
    elif n < 100:
        hasil = terbilang(n // 10) + " Puluh " + terbilang(n % 10)
    elif n < 200:
        hasil = "Seratus " + terbilang(n % 100)
    elif n < 1000:
        hasil = terbilang(n // 100) + " Ratus " + terbilang(n % 100)
    elif n < 2000:
        hasil = "Seribu " + terbilang(n - 1000)
    elif n < 1000000:
        hasil = terbilang(n // 1000) + " Ribu " + terbilang(n % 1000)
    elif n < 1000000000:
        hasil = terbilang(n // 1000000) + " Juta " + terbilang(n % 1000000)
    else:
        hasil = terbilang(n // 1000000000) + " Milyar " + terbilang(n % 1000000000)

    return hasil.strip()

bilangan = int(input("Masukkan bilangan: "))
print("Terbilang:", terbilang(bilangan))
