print("Selamat datang di program analisan skincare")
username=input("Silahkan masukan nama anda : ").lower()
userage=(int)input("Silahkan masukan umur anda : ")
user_phone=input("Silahkan masukan nomor telepon anda : ")

print("Halo", username)
print("Facewash, Sunscreen, Moisturizer, Toner")
jenis_skincare=input("Skincare apa yang  ingin dicari? ").lower()
tipe_kulit=input("Masukan tipe kulit anda. (Berminyak/Kering/Kombinasi)").lower()

if jenis_skincare==("Facewash"):
    if tipe_kulit==("Berminyak"):
        if userage>=20:
            print("Kami menyarankan merk A1")
        elif userage<=20:
            print("Kami menyarankan merk A2")
        else:
            print("Kami tidak bisa menemukan saran produk yang cocok")
    elif tipe_kulit==("Kering"):
        if userage>=20:
            print("Kami menyarankan merk A3")
        elif userage<=20:
            print("Kami menyarankan merk A4")
        else:
            print("Kami tidak bisa menemukan saran produk yang cocok")
    elif tipe_kulit==("Kombinasi"):
        if userage>=20:
            print("Kami menyarankan merk A5")
        elif userage<=20:
            print("Kami menyarankan merk A6")
        else:
            print("Kami tidak bisa menemukan saran produk yang cocok")  
elif jenis_skincare ==("Sunscreen"):
    if tipe_kulit==("Berminyak"):
       print("Kami menyarankan merk B1")
    elif tipe_kulit==("Kering"):
       print("Kami menyarankan merk B2")
    elif tipe_kulit==("Kombinasi"):
       print("Kami menyarankan merk B3")
    else:
        print("Kami tidak bisa menemukan saran produk yang cocok")
elif jenis_skincare == ("Moisturizer"):
    if tipe_kulit == ("Berminyak"):
        print("Kami menyarankan produk C1")
    elif tipe_kulit == ("Kering"):
        print("Kami menyarankan produk C2")
    elif tipe_kulit == ("Kombinasi"):
        print("Kami menyarankan produk C3")
elif jenis_skincare == ("Toner"):
    if tipe_kulit == ("Berminyak"):
        print("Kami menyarankan produk d1")
    elif tipe_kulit == ("Kering"):
        print("Kami menyarankan produk d2")
    elif tipe_kulit == ("Kombinasi"):
        print("Kami menyarankan produk d3")
else:
    print("Kami tidak dapat menampilkan produk yang anda cari")


