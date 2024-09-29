#ucapan selamat datang
print("***Selamat Datang***")

#memasukan data
print("\nsilahkan LOG IN :")
nama = str(input("Nama = "))
nim = (input("NIM = "))
pin = (input("PIN = "))
pinbenar = 1102024
if pin == pinbenar and nim == int :
    print("\nSelamat Datang", nama)

#proses penginputan barang
    print("\nInput barang anda :")
    a = str(input("Masukan nama barang = "))

#looping input harga dan jumlah barang
    inputbarang = True
    while (inputbarang == True):
        b = int(input("Masukan harga barang (contoh:25000) = Rp."))
        c = int(input("Masukan jumlah barang = "))
        total_harga = b*c
        if total_harga >= 250000:
            diskon = total_harga*75/100
            print("\n*Keterangan*")
            print("Nama barang : ", a)
            print("total harga : ",b,"X",c," =  Rp.", total_harga)
            print("Potongan 25% = Rp." ,int(diskon))

            print("\nIngin menginput ulang harga dan jumlah barang?")
            yt = True
            while (yt == True):
                t = str(input("Ketik (YA/TIDAK)= "))
                if (t == "TIDAK"):
                    inputbarang = False
                    yt = False
                    print("\nuser atas nama :",nama)
                    print("total Pembayaran anda = Rp.",int(diskon))
                    print("***terima kasih***")
                elif (t == "YA"):
                    inputbarang = True
                    yt = False
                    print("\nmasukan harga dan jumlah", a,":")
                else :
                    print("input tidak sesuai")
                    yt = True
        else :
            print("\n*Keterangan*")
            print("Nama barang : ", a)
            print("total harga : ",b,"X",c," = Rp.", total_harga)

            print("\ningin menginput ulang harga dan jumlah barang?")
            yt = True
            while (yt == True):
                t = str(input("ketik (YA/TIDAK)= "))
                if (t == "TIDAK") :
                    inputbarang = False
                    yt = False
                    print("\nuser atas nama :",nama)
                    print("total Pembayaran anda = Rp. ",int(total_harga))
                    print("***terima kasih***")
                elif (t == "YA") :
                    inputbarang = True
                    yt = False
                    print("\nmasukan harga dan jumlah", a,":")
                else :
                    print("input tidak sesuai")
                    yt = True
else :
    print("NIM tidak sesuai atau PIN salah!")
