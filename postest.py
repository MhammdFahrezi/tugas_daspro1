user = nama_mahasiswa = {'nama_mahasiswa' : 'Muhammad Fahrezi',
'nim_mahasiswa' : '2309116088',
'password' : 'Samarinda77'}

def login() :
    while True :
        nama_mahasiswa = input("masukan nama_mahasiswa :")
        nim_mahasiswa = input("maasukan nim_mahasiswa :" )
        password = input("masukan password :")
        if nama_mahasiswa == user['nama_mahasiswa'] and password == user ['password'] and nim_mahasiswa == user ['nim_mahasiswa'] :
            print ("Login berhasil")  
            break  
        else:
            print("data yang masukan salah")
print("   login       ")
login()
print(" urutan konversi :")
print("1. lb")
print("2. ons")
print("3. gram")
satuan_kg = int(input("hitung satuan_kg :"))
operator = float(input("masukan operator(1,2,3): "))

if  operator == 1 :
    satuan_lb = satuan_kg  * 2,20462 
    print(f"{satuan_kg} kilogram = {satuan_lb} lb")
elif operator == 2 :
    satuan_ons = satuan_kg * 35,274
    print(f"{satuan_kg} kilogram = {satuan_ons} ons")
elif operator == 3 :
    satuan_gram = satuan_kg * 1000
    print(f"{satuan_kg} kilogram = {satuan_gram} gram")
