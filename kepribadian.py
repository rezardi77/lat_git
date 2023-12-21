# Menghitung skor total
def skor_total(a,b,c,d,e,f,g,h,i,j,k,l):
    total=a+b+c+d+e+f+g+h+i+j+k+l

    print("\nSkor kamu adalah : ", total)

# Mendapatkan jenis kepribadian sesuai skor total yang di dapat
    if total <= 120 and total<=200:
        print("Kamu adalah seorang Plegmatis")
        print("\nKepribadian : \nCinta damai, tenang, setia, cuek, rendah hati,sabar,konsisten, pintar menyembunyikan emosi, mudah bersyukur, menyenangkan dan tidak suka menyinggung perasaan")
        print("\nKekurangan : \n Tidak punya motivasi, tidak tegas, sulit mengambil keputusan, sulit keluar dari zona nyaman, suka menunda-nunda")
        print("\nBakat : \nProblem solving, mampu  menghindari konflik dan menjadi penengah, tidak banyak bicara tapi langsung mencari cara termuda, tahap terhadap tekanan")
        print("\nContoh profesi : \nGuru, dosen, pengajar, konsultan")
    elif total >=210 and total <=300:
        print("Kamu adalah seorang Melankolis")
        print("\nkepribadian : \nDisiplin,sangat menghargai waktu, teliti (rinci/detail), menyukai kerapian, sensitif terhadap perasaan, hemat ")
        print("\nKekurangan : \nMudah tersinggung, pesimis, pendendam, punya standar yang tinggi & sulit di senangi orang lain, sulit bersosialisasi, suka mengkritik tapi tidak suka di kritik ")
        print("\nBakat : \nPerencana yang baik, suka menganalisa artistik dalam seni, filasofis dan puitis")
        print("\nContoh profesi : penulis, akuntan, seniman")
    elif total >= 310 and total <=400:
        print("Kamu adalah seorang Sanguinis")
        print("\nkepribadian : \nAntusias, bersemangat, suka senyum, ramah, penuh rasa ingin tau, mudah berubah,  mudah bersosialisasi, tidak pendendam")
        print("\nKekurangan : \nSuka membesar-besarkan masalah, susah diam, mudah ikut-ikutan, emosional mudah dikendalikan oleh keadaan, mendahulukan bicara daripada kerja, egois, dan mudah marah")
        print("\nBakat : \nPembicara yang baik, populer, menonjol, pandai menyanyi ")
        print("\nContoh profesi : \nenterprener, artis, marketing, public relation")
    elif total >= 410 and total<=480:
        print("Kamu adalah seorang Koleris")
        print("\nkepribadian : \nTegas, dominan suka tantangan, tidak mudah menyerah, berjiwa pemimpin, punya target yang jelas, suka dengan perubahan, mandiri, dan gerak cepat ")
        print("\nKekurangan : \nSuka konflik, suka mengatur, karakternya yang diktator kerap dihindari orang lain, tidak sabaran, kaku, tidak mau mengakui kesalahannya dan ceroboh")
        print("\nBakat : \nBerorganisasi, membuat target, memiliki ambisi besar, pandai memotivasi")
        print("\nContoh profesi : \npengusaha,  motivator, politikus")
    else:
        print("Kamu adalah seorang KOMUNIS")