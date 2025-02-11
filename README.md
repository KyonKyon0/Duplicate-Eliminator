# Program Penghapusan Data Duplikat CSV

## Deskripsi
Program ini adalah skrip berbasis Python yang digunakan untuk membaca file CSV, mendeteksi, dan menghapus data duplikat. Program ini juga memungkinkan pengguna untuk menyimpan file CSV yang telah dibersihkan dengan nama baru yang mencakup timestamp.

## Fitur
- Membaca file CSV dan menampilkan informasi dasar tentang data.
- Mendeteksi dan menghapus data duplikat secara otomatis.
- Menampilkan jumlah data duplikat sebelum dan sesudah proses penghapusan.
- Menyediakan opsi untuk menyimpan file CSV yang telah dibersihkan.
- Mencatat timestamp saat program dijalankan.

## Prasyarat
- Python 3.x
- Pandas
- Matplotlib

## Instalasi
1. Pastikan Python sudah terinstal di sistem.
2. Instal dependensi dengan menjalankan perintah berikut:
   ```bash
   pip install pandas matplotlib
   ```

## Cara Penggunaan
1. Simpan file CSV yang akan diproses dalam direktori yang sama dengan skrip Python.
2. Jalankan skrip menggunakan perintah berikut:
   ```bash
   python nama_file.py
   ```
3. Program akan membaca file CSV, menampilkan informasi data, serta jumlah data duplikat sebelum dan setelah penghapusan.
4. Jika ditemukan duplikat, program akan menghapusnya secara otomatis.
5. Pengguna diberikan opsi untuk menyimpan file CSV yang telah dibersihkan dengan nama baru atau tidak.
6. Jika pengguna memilih untuk menyimpan, file baru akan dibuat dengan nama yang mencakup timestamp.

## Catatan Penting
- Pastikan file CSV yang akan diproses memiliki format yang benar.
- Data yang telah dihapus tidak dapat dikembalikan setelah program selesai dijalankan.
- Program ini hanya menghapus baris duplikat berdasarkan keseluruhan isi baris.

## Penulis
**OSCAR VICTORIOUS PUTRA TAMBUNAN (51424063)**  
**UNIVERSITY OF GUNADARMA, DEPOK**

## Lisensi
Program ini dibuat untuk tujuan edukasi dan eksperimen. Penggunaan kembali dan modifikasi diperbolehkan dengan mencantumkan kredit kepada penulis.
