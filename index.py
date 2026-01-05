kehadiran = float(input('masukan nilai kehadiran :'))
tugas = float(input('masukan nilai tugas :'))
uts = float(input('masukan nilai uts :'))
uas = float(input('masukan nilai uas :'))

total_nilai = (
    kehadiran * 0.10 +
    tugas * 0.20 +
    uts * 0.30 +
    uas * 0.40
)

if total_nilai < 40 :
    nilai = 'E'
elif total_nilai < 55 :
    nilai = 'D'
elif total_nilai < 65 :
    nilai = 'C'
elif total_nilai < 79 :
    nilai = 'B'
else:
    nilai = 'A'


print('Total Nilai :',total_nilai)
print('Akreditasi',nilai)