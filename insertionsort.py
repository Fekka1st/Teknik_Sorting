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


angka = [12, 11, 13, 5, 6]

print("Insertion Sort")
print('Sebelum sort:', angka)
print('Setelah sort:', insertionSort(angka))
