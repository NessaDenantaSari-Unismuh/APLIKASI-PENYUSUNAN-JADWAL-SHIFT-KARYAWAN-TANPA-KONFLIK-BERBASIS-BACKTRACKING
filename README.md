# APLIKASI-PENYUSUNAN-JADWAL-SHIFT-KARYAWAN-TANPA-KONFLIK-BERBASIS-BACKTRACKING

## 📌 Deskripsi Proyek

Proyek ini mengembangkan sistem otomatis untuk penyusunan jadwal shift
karyawan tanpa konflik menggunakan algoritma **Backtracking**. Sistem
dirancang untuk menyelesaikan masalah penjadwalan sebagai **Constraint
Satisfaction Problem (CSP)** dengan mempertimbangkan berbagai batasan
operasional.

Sistem mampu menyusun jadwal kerja mingguan tiga shift (Pagi, Sore,
Malam) untuk beberapa posisi jabatan (Admin, Teknisi, Kasir) dengan
hasil jadwal yang valid, adil, dan bebas bentrokan.

## 🎯 Tujuan Penelitian

-   Mengotomatisasi proses penjadwalan karyawan yang sebelumnya
    dilakukan secara manual.
-   Menerapkan algoritma Backtracking untuk menyelesaikan masalah
    penjadwalan.
-   Menghasilkan jadwal kerja yang memenuhi hard constraints dan soft
    constraints.
-   Menguji efisiensi dan validitas algoritma.

## 🧠 Konsep Utama

### 1. Personnel Scheduling Problem (PSP)

Masalah penjadwalan personel merupakan masalah alokasi sumber daya
manusia ke waktu kerja tertentu dengan mempertimbangkan berbagai
batasan.

### 2. Constraint Satisfaction Problem (CSP)

Masalah CSP terdiri dari: - Variabel (slot waktu dan shift) - Domain
nilai (daftar karyawan) - Constraints (aturan penjadwalan)

### 3. Algoritma Backtracking

Backtracking bekerja dengan: 1. Memilih kandidat solusi. 2. Mengecek
apakah solusi melanggar batasan. 3. Melanjutkan jika valid. 4. Mundur
(backtrack) jika terjadi konflik.

## 📊 Dataset

Dataset yang digunakan berupa data karyawan dalam format CSV yang
mencakup atribut: - ID - Nama - Gender - Jabatan (Admin, Teknisi,
Kasir) - Preferensi Shift - Rating

Jumlah data yang digunakan: 50--100 karyawan.

## ⚙️ Aturan Penjadwalan (Constraints)

### Hard Constraints

-   Karyawan hanya boleh ditempatkan sesuai jabatan.
-   Tidak boleh ada karyawan yang bekerja lebih dari satu shift dalam
    satu hari.
-   Setiap shift harus diisi oleh tim lengkap (Admin, Teknisi, Kasir).

### Soft Constraints

-   Rotasi shift untuk menghindari monoton.
-   Preferensi shift karyawan.

### Aturan Operasional

-   3 shift per hari (Pagi, Sore, Malam).
-   Distribusi tugas menggunakan mekanisme round-robin.

## 🏗️ Tahapan Metodologi

1.  Pengumpulan data karyawan.
2.  Pra-pemrosesan data menggunakan Python dan Pandas.
3.  Perancangan algoritma Backtracking.
4.  Implementasi sistem.
5.  Visualisasi jadwal.
6.  Pengujian validitas sistem.

## 💻 Implementasi Sistem

-   Bahasa pemrograman: Python 3.x
-   Library utama:
    -   Pandas (manajemen data)
    -   Colorama & Rich (visualisasi CLI)
-   Struktur sistem berbasis OOP (Object Oriented Programming).

## 📈 Hasil dan Evaluasi

-   Sistem berhasil menyusun jadwal tanpa konflik.
-   Waktu eksekusi rata-rata \< 1 detik untuk dataset 50 karyawan.
-   Distribusi shift lebih adil melalui mekanisme rotasi.
-   Hasil pengujian black-box menunjukkan semua constraint terpenuhi.

## 🧪 Pengujian Sistem

Pengujian dilakukan dengan metode Black Box Testing: - Uji keunikan
jadwal harian. - Uji rotasi shift global. - Validasi hasil penjadwalan.

## ✅ Kesimpulan

-   Algoritma Backtracking efektif untuk masalah penjadwalan karyawan.
-   Sistem mampu meningkatkan efisiensi dan akurasi penjadwalan.
-   Jadwal yang dihasilkan valid, adil, dan bebas konflik.

## 🚀 Pengembangan Selanjutnya

-   Integrasi soft constraints yang lebih kompleks.
-   Pengembangan antarmuka berbasis Web atau Mobile.
-   Optimasi algoritma untuk dataset skala besar.

## 👩‍💻 Penulis

-   Nessa Denanta Sari
-   Ilma Aqsari

## 📚 Referensi

Penelitian ini mengacu pada berbagai literatur terkait algoritma
Backtracking, CSP, dan penjadwalan personel dalam bidang informatika dan
manajemen operasional.
