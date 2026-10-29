# Panduan publikasi ke GitHub

Paket ZIP ini **bukan** repositori GitHub online. Untuk memublikasikan:

1. Masuk ke https://github.com/new dan buat repositori bernama `klasifikasi-sampah-deep-learning` (sebaiknya **Private** lebih dulu agar nama dan NIM pada laporan tidak otomatis publik). Jangan centang pembuatan README/gitignore otomatis karena paket ini sudah berisi file tersebut.
2. Ekstrak ZIP ke komputer. Pastikan menjalankan terminal dari folder yang berisi `README.md`, `data/`, `notebooks/`, dan seterusnya.
3. Jika belum punya Git, instal Git for Windows (https://git-scm.com/downloads/win). Konfigurasi nama/email Git jika diminta.
4. Jalankan `publish_windows.bat` di folder proyek, masukkan URL repositori GitHub saat diminta. Login melalui Git Credential Manager saat browser dibuka.
5. Pastikan file muncul di halaman repositori. Salin URL GitHub ke bagian 8 Lampiran laporan.

**Penting:** Berkas `models/trashnet_mlp.keras` sekitar 38 MB, lebih besar dari batas per-berkas upload web GitHub (25 MB). Gunakan Git CLI (skrip Windows), bukan unggah semua file satu per satu di browser.

Jika GitHub sudah dihubungkan langsung ke ChatGPT, file dapat diterbitkan dengan koneksi tersebut sesuai izin yang diberikan.
