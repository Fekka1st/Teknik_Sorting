def selection_sort(nilai):
    # i menunjukkan berapa banyak item yang diurutkan
    for i in range(len(nilai)-1):
        # Untuk menemukan nilai minimum dari segmen yang tidak disortir
        # pertama asumsikan bahwa elemen pertama adalah yang terendah
        min_index = i
        # Kami kemudian menggunakan j untuk mengulang elemen yang tersisa
        dex = 0
        for j in range(i+1, len(nilai)):
            if nilai[j] < nilai[min_index]:
                min_index = j

        # Setelah menemukan item terendah dari wilayah yang tidak disortir, tukar dengan item yang tidak disortir pertama
        nilai[i], nilai[min_index] = nilai[min_index], nilai[i]
    return nilai


nilai = [3, 4, 1, 6, 2]
print("ini nilai sebelum disorting : ", nilai)
print("Ini nilai sesudah disorting : ", selection_sort(nilai))
