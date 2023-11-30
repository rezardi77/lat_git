def sapa(nama):
        print("Hi"+ nama +". Apa kabar ?")

sapa("Boy")

def print_string(str):
        print(str)

print_string(str = "wleowleo")

def print_info( nama, usia):
            print("Nama : ", nama)
            print("Usia :", usia)

print_info(usia=25, nama="andi")

def print_info(nama, usia=17):
        print("Nama : ", nama)
        print("Usia :", usia)

print_info(usia=19, nama="nana")
print_info(nama="loki")

def print_info(arg1, *vartuple):
        print("Outputnya adalah : ")
        print(arg1)
        for var in vartuple:
                    print(var)
        
print_info(10,20,30)

def sum(arg1, arg2):
        total= arg1+arg2
        print("Di dalam fungsi nilai total : " , total)
        return total
        sum(10,20)
        print("aku", total)
        