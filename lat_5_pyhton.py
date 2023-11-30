print("   GEROBAK FRIED CHICKEN  ")
print("===============================")
print("kode jenis potong     harga")
print("===============================")
print("D      dada        Rp. 2500")
print("P      paha        Rp. 2000")
print("S      sayap       Rp. 1500")

banyak_jenis = int(input("banyak jenis : "))
kode_potong = [] 
banyak_potong = []
jenis_potong = []
harga = []
jumlah = []

i= 0
while i<banyak_jenis: 
    print("jenis ke - ", i+1)
    kode_potong.append(input("kode potong [D/P/S] : ")) 
    banyak_potong.append(int(input("banyak potong : ")))

    if kode_potong[i] == "D" or kode_potong[i] == "d" :
        jenis_potong.append("Dada")
        harga.append("2500")
        jumlah.append(banyak_potong[i]*int("2500"))
    elif kode_potong[i] == "P" or kode_potong[i] == "p" :
        jenis_potong.append("Paha")
        harga.append("2000")
        jumlah.append(banyak_potong[i]*int("2000"))
    elif kode_potong[i] == "S" or kode_potong[i] == "s" :
        jenis_potong.append("Sayap")
        harga.append("1500")
        jumlah.append(banyak_potong[i]*int("1500"))
    else : 
        jenis_potong.append("kode salah")
        harga.append("0")
        jumlah.append(banyak_potong[i]*int("0"))
    i= i + 1
print(" GEROBAK FRIED CHIKEN")
print("==========================================")
print("No    Jenis    Harga   banyak    jumlah")
print("      Potong   Satuan   Beli     Harga ")
print("==========================================")

a = 0
while a < banyak_jenis:
    print("%i    %s     %s      %i     %i" % (a+1,jenis_potong[a], harga[a], banyak_potong[a], jumlah[a]))
    a = a + 1

jumlah_bayar = int(input("jumlah bayar Rp. "))
pajak = jumlah_bayar * 0.1
total_bayar = jumlah_bayar + pajak
print("pajak 10 % Rp. ", pajak)
print("total bayar Rp. ", total_bayar)
    