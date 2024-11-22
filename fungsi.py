# Buatlah sebuah fungsi bernama celcius_ke_fahrenheit yang menerima satu argumen: suhu dalam celcius. Fungsi ini harus mengembalikan suhu yang dikonversi ke Fahrenheit.
# print(celcius_ke_fahrenheit(0))    # Output: 32.0
# print(celcius_ke_fahrenheit(100))  # Output: 212.0
  
  
  
  
  
def celceius_ke_fahrenheit(celcius):
    hasil_konversi = (celcius * 9/5) + 32
    return hasil_konversi

print(celceius_ke_fahrenheit(0))
print(celceius_ke_fahrenheit(100))
print(celceius_ke_fahrenheit(1000))
print('====================')


  #soal nomer 2
# Buatlah sebuah fungsi bernama is_genap yang menerima satu argumen: bilangan bulat. Fungsi ini harus mengembalikan True jika bilangan tersebut genap, dan False jika bilangan tersebut ganjil.
# print(is_genap(4))  # Output: True
# print(is_genap(7))  # Output: False
# print (is_genap(4))
#  #output: True
# print(is_genap(7))
# # output: False

def is_genap(angka):
    return angka % 2 == 0

genap = 4
print(f' Output Dari Bilangan (Genap) Adalah {is_genap (genap)}')
print(is_genap(4))
print(is_genap(7))
print('===============')

# Buatlah fungsi untuk melihat ketrangan lulus atau tidak lulus : 
# nilai (80) #lulus
# nilai(60) #gagal




def nilai(nilai_siswa):
    if nilai_siswa >= 70:
        return "Lulus"
    else:
        return "Gagal"
    
    
print(nilai(80))  
print(nilai(60))  
   

# Buatlah fungsi untuk menampilkan bilangan ganjil yang kurang argumens
# bilangan(20) # 1,3,5,7,9,11,13,15,17,19

def bilangan(n):
    
    # Menampilkan bilangan ganjil dari 1 hingga n-1
    
    for i in range(1, n, 2):
        print(i, end=' ')
bilangan(20) 
