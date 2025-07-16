print("="*20)
print("Kalkulator Sederhana")
print("="*20)

while True:
    print("="*100)
    print("Selamat datang di kalkulator sederhana!")
    a = float(input("Masukkan angka pertama: "))

    print("Pilih operasi yang anda inginkan (+,-,*,/)")
    while True:
        operasi = input("Masukkan operasi yang anda inginkan: ")
        if operasi in ["+", "-", "*", "/"]:
            break
        print("Operasi tidak valid. Silakan coba lagi.")

    b = float(input("Masukkan angka kedua: "))

    if operasi == "+":
        hasil = a + b
    elif operasi == "-":
        hasil = a-b
    elif operasi == "*":
        hasil = a*b
    elif operasi == "/":
        hasil = a/b
    else:
        print("Operasi yang anda masukkan salah")

    print("="*20)
    print(f'Hasil operasi = {hasil}')
    print("="*20)

    while True:
        ulang = input("Ingin menggunakan kalkulator lagi? (Y/N)\n ")
        if ulang == 'n' or ulang =='N':
            exit()
        elif ulang in ['y','Y']:
            break
        else:
            print("o_o salah input bang >_<")
