print("WARNET BAROKAH")
print("--------------------------------------")
print("--------------------------------------")

pc=input("Pilih PC : ")
lama_sewa=int(input("Lama Sewa : "))

print(" (Biaya sewa 1 jam adalah 5000)")
print("Diskon 10% tiap sewa >3 jam")

if lama_sewa >3:
    diskon=(lama_sewa*5000)*0.1

else:
    lama_sewa*0

total=(lama_sewa*5000)-diskon
print("Total : "+ str(total))
tunai=int(input("Tunai : "))

kembalian=(tunai - total)

print("Kembalian : "+ str(kembalian))

print("--------------------------------------")
print("--------------------------------------")

print("TERIMA KASIH ATAS KUNJUNGAN ANDA")




