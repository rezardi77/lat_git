# Menginput modul skor & modul keprbadian
import skor
import kepribadian

# User menginput data diri
username=input("Silahkan masukan nama anda : ").upper()
userage=input("Silahkan masukan umur anda : ")

#Header
print("HALO", username)
print("\n SELAMAT DATANG DI PROGRAM TEST KEPRIBADIAN")
print("\nProgram test ini berisi 11 pertanyaan yang harus anda jawab\n dengan jujur agar hasil bisa akurat")
print("Ikuti petunjuk dibawah ini untuk menjawab test ini")
print("Jawab dengan mengisi A,B,C, atau D")

#Pertanyaan 
print("\n1. Suatu saat, kamu dia ajak pergi ke restoran bersama teman mu. Apa yang kamu lakukan ?")
print("\nA.Pilih menu apapun yang kamu suka \nB.Minta di jelaskan tiap menu nya \nC.Tidak terlalu peduli dengan menu yang di pesan kan \nD.Memilih menu yang terbaik/termahal")
p1=input("Jawaban kamu : ").lower()
skor1=skor.skor_jawaban(p1)

print("\n2. Suatu saat, ketika kamu pergi keluar kota, kamu lapar dan ingin makan siang. Tempat seperti apa yang kamu pilih ?")
print("\nA.Restoran langganan \nB.Survey dahulu di internet \nC.Murah dan enak \nD.Coba tempat baru")
p2=input("Jawaban kamu : ").lower()
skor2=skor.skor_jawaban(p2)


print("\n3. Apa yang kamu lakukan ketika ada janji ?")
print("\nA.Suka telat \nB.Datang tepat waktu \nC.Lupa kalau ada janji \nD.Datang sebelum waktu nya")
p3=input("Jawaban kamu : ").lower
skor3=skor.skor_jawaban(p3)


print("\n4. Baju seperti apa yang menjadi kesukaan mu ?")
print("\nA.Casual \nB.Formal \nC.Berwarna cerah \nD.Berwarna gelap")
p4=input("Jawaban KAMU : ").lower()
skor4=skor.skor_jawaban(p4)


print("\n5. Apa jenis/genre musik kesukaan mu ?")
print("\nA.Santai : reggea/ska \nB.Sedih/galau : Pop \nC.Semangat : Punk \nD.Keras: Metal/rock")
p5=input("Jawaban kamu : ").lower()
skor5=skor.skor_jawaban(p5)


print("\n6. Apa yang kamu lakukan jika kamu baru saja membeli barang baru ?")
print("\nA.Biasa saja \nB. Menjaganya sepenuh hati \nC.Memamerkan nya \nD.Memanfaatkan nya secara maksimal")
p6=input("Jawaban kamu : ").lower()
skor6=skor.skor_jawaban(p6)


print("\n7. Mana yang termasuk hobi mu ?")
print("\nA.Main catur \nB.Membaca \nC.Menyanyi \nD.Olahraga ")
p7=input("Jawaban kamu : ").lower()
skor7=skor.skor_jawaban(p7)


print("\n8. Bagaimana jika kamu inging mengungkapkan sesuatu kepada orang lain ?")
print("\nA.Merasa sungkan \nB.Pikir matang-matang \nC.Asal bicara \nD.Apa ada nya")
p8=input("Jawaban kamu : ").lower()
skor8=skor.skor_jawaban(p8)


print("\n9. Apa yang menjadi cita citamu-mu ?")
print("\nA.Dosen \nB.Penulis \nC.Artis \nD.Presiden")
p9=input("Jawaban kamu : ").lower()
skor9=skor.skor_jawaban(p9)


print("\n10.Dari beberapa hal berikut, mana yang kamu takuti ?")
print("\nA.Keluar dari zona nyaman \nB.Dikritik \nC.Ditolak \nD.Dimanfaatkan")
p10=input("Jawaban kamu : ").lower()
skor10=skor.skor_jawaban(p10)


print("\n11.Dari beberapa hal berikut, mana yanng menjadi prioritas mu ?")
print("\nA.Menghindari konflik \nB.Kesempurnaan \nC.Kebersamaan \nD.Target")
p11=input("Jawaban kamu : ").lower()
skor11=skor.skor_jawaban(p11)


print("\n12.Jika pada suatu saat kamu berteemu musuh mu yang sdua sangat dendam padamu, dan kamu di tantang berkelahi, apa yang kamu lakukan ?")
print("\nA.Ajak berdamai \nB.Kabur \nC.Hanya bisa teriak \nD.Menghajarnya")
p12=input("Jawaban kamu : ")
skor12=skor.skor_jawaban(p12)
# Untuk mendapatkan skor sesuai jawaban yang di pilih user, modul "skor" di panggil

#Skor dari pertanyaan di jumlahkan dan di berikan hasil nya menggunakan modul skor & modul kepribadian
print(kepribadian.skor_total(skor1,skor2,skor3,skor4,skor5,skor6,skor7,skor8,skor9,skor10,skor11,skor12))


