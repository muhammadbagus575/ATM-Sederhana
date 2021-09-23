print("Selamat Datang di ATM saya")
print("Pilih Option :")
print("1. Check Uang Saya")
print("2. Ambil Uang Saya")
print("3. Tabung Uang Saya")
option=int(input("Silahkan pilih option :"))
if option==1:
      print("Uang kamu Berjumlah Rp.300.000")
elif option==2:
      print("Uang kamu Berjumlah Rp.300.000, Mau ambil berapa?")
      print("1. Rp.50.000")
      print("2. Rp.100.00")
      uang_kamu=300000
      option2=int(input("option :"))
      if option2==1:
            hasil=uang_kamu-50000
            print("Uang kamu sekarang Berjumlah :",hasil)
      elif option2==2:
            hasil2=uang_kamu-100000
            print("Uang kamu sekarang Berjumlah :",hasil2)
      else:
            print("keywoard Anda Salah!")
elif option==3:
      uang_kamu=300000
      print("Uang berjumlah Rp.300.000, Mau Nabung Berapa?")
      option3=int(input("Masukan Jumlah Uang :"))
      hasil3=uang_kamu+option3
      print("Jumlah Uang Kamu Sekarang Adalah ",hasil3)
else:
      print("keywoard Anda Salah, Mohon Coba Lagi!")