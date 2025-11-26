def hello(nama, kota, umur):
    print(f'hello nama saya adalah {nama}, saya tinggal di {kota}, umur saya adalah {umur}')

hello('mad', 'depok', 10)

def perkalian(angka1,angka2):
    return angka1+angka2

print(f'hasil perkalian dari {perkalian(5,2)}')



def celcius_ke_fahrenheit(c):
    return (c * 9/5) + 32

print(celcius_ke_fahrenheit(0))    # Output: 32.0
print(celcius_ke_fahrenheit(100))  # Output: 212.0


def is_genap(n):
    return n % 2 == 0

print(is_genap(4))  # Output: True
print(is_genap(7))  # Output: False


def nilai(n):
    if n >= 70:
        return "lulus"
    else:
        return "gagal"

print(nilai(80))  # lulus
print(nilai(60))  # gagal

def bilangan(n):
    ganjil = []
    for i in range(1, n):
        if i % 2 != 0:
            ganjil.append(i)
    return ganjil

print(bilangan(20))  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]