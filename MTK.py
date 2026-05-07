# Program Statistik Data Kelompok
# Mean, Median, Modus, Q1, dan Q3

# =========================
# INPUT DATA
# =========================

interval_input = input(
    "Masukkan interval kelas (contoh: 10-19,20-29,30-39): "
)

frekuensi_input = input(
    "Masukkan frekuensi (contoh: 2,8,12,7,3): "
)

# Mengubah interval menjadi list
interval_list = interval_input.split(",")

kelas = []

for interval in interval_list:
    bawah, atas = map(int, interval.split("-"))
    kelas.append((bawah, atas))

# Mengubah frekuensi menjadi list angka
frekuensi = list(map(int, frekuensi_input.split(",")))

n = len(kelas)

# =========================
# DIKETAHUI
# =========================

print("\n=== DIKETAHUI ===")

print("Interval Kelas :")
for i in range(n):
    print(f"Kelas {i+1} = {kelas[i][0]}-{kelas[i][1]}")

print("Frekuensi :", frekuensi)

# Frekuensi kumulatif
fk_list = []
fk = 0

for f in frekuensi:
    fk += f
    fk_list.append(fk)

print("Frekuensi Kumulatif (fk) :", fk_list)

# =========================
# PILIHAN MENU
# =========================

print("\n=== PILIH YANG INGIN DICARI ===")
print("1. Mean")
print("2. Median")
print("3. Modus")
print("4. Kuartil Bawah (Q1)")
print("5. Kuartil Atas (Q3)")

pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

# =========================
# DATA UMUM
# =========================

total_f = sum(frekuensi)
p = kelas[0][1] - kelas[0][0] + 1

# =========================
# MEAN
# =========================

if pilihan == "1":

    total_fx = 0

    print("\n=== PERHITUNGAN ===")

    for i in range(n):
        xi = (kelas[i][0] + kelas[i][1]) / 2
        fx = xi * frekuensi[i]

        print(
            f"Kelas {i+1} | xi = {xi} | f = {frekuensi[i]} | fx = {fx}"
        )

        total_fx += fx

    mean = total_fx / total_f

    print("\n=== HASIL ===")
    print("Σf =", total_f)
    print("Σfx =", total_fx)
    print("Mean =", mean)

# =========================
# MEDIAN
# =========================

elif pilihan == "2":

    posisi = total_f / 2

    fk = 0
    for i in range(n):
        fk += frekuensi[i]

        if fk >= posisi:
            kelas_median = i
            break

    print("\nMedian berada pada kelas ke-", kelas_median + 1)

    tb = kelas[kelas_median][0] - 0.5
    ta = kelas[kelas_median][1] + 0.5

    f = frekuensi[kelas_median]

    fk_sebelum = sum(frekuensi[:kelas_median])

    median = tb + (((posisi - fk_sebelum) / f) * p)

    print("\n=== DIKETAHUI ===")
    print("N =", total_f)
    print("N/2 =", posisi)
    print("tb =", tb)
    print("ta =", ta)
    print("f =", f)
    print("fk sebelum =", fk_sebelum)
    print("p =", p)

    print("\n=== HASIL ===")
    print("Median =", median)

# =========================
# MODUS
# =========================

elif pilihan == "3":

    f1 = max(frekuensi)
    index_modus = frekuensi.index(f1)

    print("\nModus berada pada kelas ke-", index_modus + 1)

    tb = kelas[index_modus][0] - 0.5
    ta = kelas[index_modus][1] + 0.5

    f0 = frekuensi[index_modus - 1] if index_modus > 0 else 0
    f2 = frekuensi[index_modus + 1] if index_modus < n - 1 else 0

    d1 = f1 - f0
    d2 = f1 - f2

    modus = tb + ((d1 / (d1 + d2)) * p)

    print("\n=== DIKETAHUI ===")
    print("tb =", tb)
    print("ta =", ta)
    print("f1 =", f1)
    print("f0 =", f0)
    print("f2 =", f2)
    print("d1 =", d1)
    print("d2 =", d2)
    print("p =", p)

    print("\n=== HASIL ===")
    print("Modus =", modus)

# =========================
# KUARTIL BAWAH (Q1)
# =========================

elif pilihan == "4":

    posisi = total_f / 4

    fk = 0
    for i in range(n):
        fk += frekuensi[i]

        if fk >= posisi:
            kelas_q1 = i
            break

    print("\nQ1 berada pada kelas ke-", kelas_q1 + 1)

    tb = kelas[kelas_q1][0] - 0.5
    ta = kelas[kelas_q1][1] + 0.5

    f = frekuensi[kelas_q1]

    fk_sebelum = sum(frekuensi[:kelas_q1])

    q1 = tb + (((posisi - fk_sebelum) / f) * p)

    print("\n=== DIKETAHUI ===")
    print("N =", total_f)
    print("N/4 =", posisi)
    print("tb =", tb)
    print("ta =", ta)
    print("f =", f)
    print("fk sebelum =", fk_sebelum)
    print("p =", p)

    print("\n=== HASIL ===")
    print("Kuartil Bawah (Q1) =", q1)

# =========================
# KUARTIL ATAS (Q3)
# =========================

elif pilihan == "5":

    posisi = (3 * total_f) / 4

    fk = 0
    for i in range(n):
        fk += frekuensi[i]

        if fk >= posisi:
            kelas_q3 = i
            break

    print("\nQ3 berada pada kelas ke-", kelas_q3 + 1)

    tb = kelas[kelas_q3][0] - 0.5
    ta = kelas[kelas_q3][1] + 0.5

    f = frekuensi[kelas_q3]

    fk_sebelum = sum(frekuensi[:kelas_q3])

    q3 = tb + (((posisi - fk_sebelum) / f) * p)

    print("\n=== DIKETAHUI ===")
    print("3N/4 =", posisi)
    print("tb =", tb)
    print("ta =", ta)
    print("f =", f)
    print("fk sebelum =", fk_sebelum)
    print("p =", p)

    print("\n=== HASIL ===")
    print("Kuartil Atas (Q3) =", q3)

else:
    print("Pilihan tidak valid!")