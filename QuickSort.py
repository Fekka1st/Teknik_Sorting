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


angka = [34, 21, 45, 32, 12, 31, 19, 23, 54, 31, 25, 27]
print('Sebelum sort:', angka)
quicksort(angka, 0, len(angka))
print('Setelah sort:', angka)
print(len(angka))
