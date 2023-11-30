# Membuat List 2 Dimensi
my_list=[['1','2','3'], ['4','5','6'], ['7','8','9'], ['0',' ',' ']]

print("Baris Pertama, Kolom Pertama adalah")
print(my_list[0][0])
print("Baris Kedua, Kolom Kedua adalah")
print(my_list[1][1])
print("Baris Ketiga, Kolom Ketiga adalah")
print(my_list[2][2])
print("Baris Kempat, Kolom Pertama adalah")
print(my_list[3][0])


# Tugas

list_nim=[]
list_uts=[]
list_uas=[]
list_total=[]

ulang=2
for i in range(ulang):
   print ("data Ke - " + str(i+1)) 
   list_nim.append(input("Masukkan Nim anda : "))
   list_uts.append(int(input("Masukkan Nilai UTS anda: ")))
   list_uas.append(int(input("Masukkan Nilai UAS : ")))

for i in range(ulang):
   list_total.append((list_uas[i] + list_uts[i]) / 2)


print("=============================================================")
print("Nim     Nilai Uts     Nilai UAS                Total")
print("=============================================================")

for i in range(ulang):
   print ("%s \t %i \t\t %i \t\t\t %i" % (list_nim[i],list_uts[i],list_uas[i],list_total[i]))
   print("=============================================================")