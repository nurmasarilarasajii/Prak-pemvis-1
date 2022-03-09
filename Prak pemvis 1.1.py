abjad = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

a = int(input('Masukkan angka yang digunakan untuk menggeser huruf : '))

def ubah(kalimat,angka):
    kalimat = kalimat.lower()
    hasil_ubah = ''
    for karakter in kalimat:
        if karakter in abjad:
            index_lama = abjad.index(karakter)
            index_baru = (index_lama + angka) % len(abjad)
            abjad_baru = abjad[index_baru]
            hasil_ubah = hasil_ubah + abjad_baru
        else:
            hasil_ubah = hasil_ubah + ' '
    return hasil_ubah

kalimat = input('Masukkan kalimat : ')
kalimat_hasil = ubah(kalimat,a)
print ('Kalimat yang ingin anda ubah adalah',kalimat,'dengan penggeseran kata sebanyak',a)
print('Maka hasilnya adalah : ',kalimat_hasil)
