# Program Python untuk implementasi MergeSort
# Menggabungkan dua subarray arr[].
# Subarray pertama adalah arr[l..m]
# Subarray kedua adalah arr[m+1..r]
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    # buat array temp
    L = [0] * (n1)
    R = [0] * (n2)
    # Salin data ke array temp L[] dan R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
   # Gabungkan array temp kembali ke arr[l..r]
    i = 0     # Indeks awal dari subarray pertama
    j = 0     # Indeks awal dari subarray kedua
    k = l     # Indeks awal dari subarray ketiga
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    # Salin elemen L[] yang tersisa, jika ada
    # apakah ada?
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    # Salin elemen R[] yang tersisa, jika ada
    # apakah ada?
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
# l adalah untuk indeks kiri dan r adalah indeks kanan dari
# sub-array arr yang akan diurutkan


def mergeSort(arr, l, r):
    if l < r:
        # Sama seperti (l+r)//2, tetapi menghindari overflow untuk
        # l dan h besar
        m = l+(r-l)//2
       # Urutkan bagian pertama dan kedua
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)


arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("\nMerge Sort")
print("Data array sebelum di sorting")
for i in range(n):
    print("%d" % arr[i]),

mergeSort(arr, 0, n-1)
print("\n\nData array sesudah di sorting")
for i in range(n):
    print("%d" % arr[i]),
