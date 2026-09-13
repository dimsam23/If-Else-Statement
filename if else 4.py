nilai = int(input("Masukkan nilaimu = "))

if nilai >= 85:
    nilai = "A"
elif nilai >= 70:
    nilai = "B"
elif nilai >= 59:
    nilai = "BC"
elif nilai >= 50:
    nilai = "C"
elif nilai >= 40:
    nilai = "D"
else:
    nilai = "E"
print ("nilaimu adalah %s" % nilai)