# Klasifikasi Jenis Sampah untuk Daur Ulang Menggunakan Deep Learning

**Kelompok 6 | UTS Pengantar Algoritma Deep Learning (2026)**

Proyek ini membandingkan **Multilayer Perceptron (MLP)** dan **Convolutional Neural Network (CNN)** untuk mengklasifikasikan enam kategori citra sampah menggunakan **TrashNet**: `cardboard`, `glass`, `metal`, `paper`, `plastic`, dan `trash`.

## Status hasil UTS

Hasil *nyata* dari notebook Google Colab yang dijalankan pada dataset test 253 gambar (bukan hasil simulasi):

| Model | Test loss | Test accuracy | Prediksi benar |
|:--|--:|--:|--:|
| MLP | 1,6589 | **19,37%** | 49 / 253 |
| CNN | 0,8943 | **70,75%** | 179 / 253 |

Dataset awal 2.527 gambar valid. Enam gambar dengan konflik label pada tiga pasangan duplikat dikeluarkan. Dataset akhir **2.521 gambar**: **2.016 training**, **252 validation**, dan **253 testing**.

**Batasan:** CNN menunjukkan indikasi overfitting dan recall kelas `plastic` hanya 50%; hasil ini tidak menjamin performa di dunia nyata.

## Struktur proyek

```text
klasifikasi-sampah-deep-learning/
├── data/          # sumber dan petunjuk memperoleh dataset
├── notebooks/     # notebook Colab yang dapat dijalankan ulang
├── src/           # skrip prediksi satu gambar
├── models/        # model Keras terlatih MLP dan CNN
├── reports/       # laporan Word, CSV, grafik, confusion matrix
├── requirements.txt
├── .gitignore
└── README.md
```

## Cara menjalankan notebook (paling mudah: Google Colab)

1. Unduh dataset dari repositori asli: **https://github.com/garythung/trashnet**, pilih arsip `dataset-resized.zip` yang memuat direktori `dataset-resized/` dengan subfolder tiap kelas. Dataset tidak diunggah ulang ke repositori ini.
2. Buka https://colab.research.google.com/ lalu pilih **File → Upload notebook**.
3. Unggah `notebooks/UTS_TrashNet_MLP_CNN_Colab.ipynb` dari repositori ini.
4. Di cell pertama, jika `ZIP_PATH = Path('/content/TrashNet, Garbage Classification.zip')` tidak ada, notebook meminta unggahan ZIP. Pilih ZIP unduhan dataset; nama file boleh berbeda karena notebook mendeteksinya secara otomatis saat diunggah.
5. Jalankan **Runtime → Run all** atau jalankan cell berurutan.
6. Hasil akan berada di `/content/hasil_uts_trashnet/`. Untuk mengunduh, jalankan:

   ```python
   !zip -r /content/hasil_uts_trashnet.zip /content/hasil_uts_trashnet
   from google.colab import files
   files.download('/content/hasil_uts_trashnet.zip')
   ```

> Catatan: Notebook membersihkan berkas identik yang berkonflik label, lalu membagi data secara stratified dengan random seed 42. Eksperimen memakai citra 64×64, normalisasi /255, batch size 32, Adam (learning rate 0,001), sparse categorical crossentropy, dan maksimum 15 epoch dengan EarlyStopping (patience 3).

## Instalasi dan prediksi lokal (opsional)

Butuh Python yang didukung TensorFlow pada perangkatmu. Di folder proyek, jalankan:

```bash
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python src/predict.py --image path/ke/contoh.jpg --model models/trashnet_cnn.keras
```

Gunakan gambar JPEG (`.jpg`/`.jpeg`) saat menjalankan skrip, sesuai pipeline preprocessing notebook.

MLP bisa diuji dengan mengganti parameter `--model` menjadi `models/trashnet_mlp.keras`. Skrip mengeluarkan prediksi dan probabilitas masing-masing kelas. **Hasil inferensi dari foto baru bukan evaluasi terukur di dunia nyata.**

## Berkas hasil dan laporan

- `reports/Laporan_UTS_Kelompok_6.docx`: draf laporan UTS mengikuti struktur dosen (1–8, tanpa BAB).
- `reports/training_curves.png`: kurva akurasi dan loss training/validation.
- `reports/confusion_matrix_cnn.png`, `reports/confusion_matrix_mlp.png`: confusion matrix pada data test.
- `reports/contoh_kesalahan_cnn.png`: contoh kesalahan CNN.
- `reports/perbandingan_model.csv`: nilai asli evaluasi kedua model.
- `models/*.keras`: model tersimpan setelah pelatihan.

## Sumber dan atribusi

- Dataset & repositori: Thung, G. / Yang, M. — https://github.com/garythung/trashnet
- Yang, M., & Thung, G. (2016). *Classification of Trash for Recyclability Status*. Stanford CS229 Project Report. https://cs229.stanford.edu/proj2016/report/ThungYang-ClassificationOfTrashForRecyclabilityStatus-report.pdf

Periksa ketentuan lisensi untuk penggunaan dataset di luar tugas akademik. Dataset tidak didistribusikan dalam repositori ini.
