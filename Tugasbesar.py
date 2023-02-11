import os


def insertionSort(angka):
    for i in range(1, len(angka)):
        key = angka[i]

        j = i-1
        while j >= 0 and key < angka[j]:
            angka[j+1] = angka[j]
            j -= 1
        angka[j+1] = key
    for i in range(len(angka)):
        angka[i] = angka[i]
    return angka


def partition(l, bwh, atas):
    pivot = l[bwh]
    pos_batas = bwh+1
    for j in range(bwh+1, atas):
        if l[j] < pivot:
            l[pos_batas], l[j] = l[j], l[pos_batas]
            pos_batas += 1
    l[pos_batas-1], l[bwh] = l[bwh], l[pos_batas-1]
    return pos_batas


def quicksort(l, bwh, atas):
    if atas <= bwh:
        return
    q = partition(l, bwh, atas)
    quicksort(l, bwh, q-1)
    quicksort(l, q, atas)
    return l


def nilai_maksimal(angka):
    nilai_terbesar = angka[0]

    for nilai in angka:
        if nilai > nilai_terbesar:
            nilai_terbesar = nilai

    return nilai_terbesar


def nilai_minimal(angka):
    nilai_terkecil = angka[0]

    for nilai in angka:
        if nilai < nilai_terkecil:
            nilai_terkecil = nilai

    return nilai_terkecil


def matrik():
    baris = int(input("inputkan baris "))
    kolom = int(input("inputkan Kolom "))
    matrik = []
    for i in range(baris):
        a = []
        for j in range(kolom):
            a.append(int(input("input angka ")))
        matrik.append(a)
    print("\n")
    for i in range(baris):
        for j in range(kolom):
            print(matrik[i][j], end=" ")
        print()


angka = [12, 11, 13, 5, 6]
print("\nnilai Element Array : ", angka, "\n")
print("Menu list:")
print("1.Quick Sort")
print("2.Insertion Sort")
print("3.Menentukan nilai MAX dan MIN")
print("4.Matrix")
print("0.Exit")
pilih = input("Pilih menu yang diinginkan: <0-5> = ")
pilih = int(pilih)


if pilih == 1:
    print("\nQuick Sort ")
    print('Sebelum sort:', angka)
    # fungsi len() untuk menghitung jumlah indeks array atau jumlah data didalam objek
    quicksort(angka, 0, len(angka))
    print('Setelah sort:', angka)

elif pilih == 2:
    print("\nInsertion Sort")
    print('Sebelum sort:', angka)
    print('Setelah sort:', insertionSort(angka))

elif pilih == 3:
    print("\nMenentukan Nilai MAX dan MIN")
    print("Nilai pada element array", angka)
    print('Nilai terbesar:', nilai_maksimal(angka))
    print('Nilai terkecil:', nilai_minimal(angka))

elif pilih == 4:
    matrik()

elif pilih == 0:
    print("Terimakasih!")

else:
    print("Inputan tidak ada!")

# fungsi untuk cleanscreen agar gk banyak riwayat data
on = input("Enter For cleanScreen")
os.system('cls')

# Nama : Ferry Aditya Herman Kelas: IF A 2020 NPM: 5520120021
