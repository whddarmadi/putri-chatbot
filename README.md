# 🌸 P.U.T.R.I.
### *Pemroses Ucapan Teks Responsif Indonesia*

> **Chatbot Rule-Based Bilingual berbasis arsitektur ELIZA**  
> Terinspirasi dari ELIZA — sistem AI percakapan pertama di dunia oleh MIT (1966)

---

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=for-the-badge)](#)
[![GUI](https://img.shields.io/badge/GUI-Tkinter-blue?style=for-the-badge)](#)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Portfolio%20Project-orange?style=for-the-badge)](#)
[![HTML](https://img.shields.io/badge/Web-HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)](#)

</div>

---

## 📖 Deskripsi

<div align="center">
  <img src="assets/putri.png" width="180" alt="PUTRI Character" style="border-radius: 50%; border: 3px solid #e94560;">
  [![GitHub](https://img.shields.io/badge/GitHub-whddarmadi-181717?style=flat-square&logo=github)]([https://github.com/whddarmadi](https://whddarmadi.github.io/putri-chatbot/putri.html))
</div>

---

**PUTRI** adalah *conversational agent* berbasis aturan (rule-based) yang dikembangkan menggunakan Python murni. Proyek ini mengimplementasikan teknik dasar Natural Language Processing (NLP) melalui pencocokan pola Regular Expression (Regex) dan teknik refleksi linguistik, yang merupakan inti dari arsitektur ELIZA klasik.

Nilai jual utama PUTRI adalah kemampuannya melakukan **code-mixing** (campur kode) antara **Bahasa Indonesia** dan **Bahasa Jawa** secara natural — menjadikannya relevan secara budaya bagi pengguna dari Pulau Jawa dan sekitarnya.

---

## ✨ Fitur Utama

| Fitur | Keterangan |
|---|---|
| 🧠 **Teknik Refleksi ELIZA** | Capture groups untuk memantulkan kembali pernyataan user, menciptakan ilusi empati mesin |
| 🌏 **Bilingual ID-Jawa** | Mengenali dan merespons dalam bahasa Indonesia dan bahasa Jawa secara natural |
| 🗂️ **100+ Pola Aturan** | Mencakup sapaan, panggilan, identitas, religi, makanan khas Jawa, binatang ternak, nama tempat, keluh kesah, umpatan, hingga easter egg tersembunyi |
| 🧹 **Preprocessing Cerdas** | Normalisasi slang (yg→yang, gk→nggak, dll) untuk pencocokan lebih robust |
| 🖥️ **GUI Desktop** | Antarmuka grafis berbasis Tkinter — tidak perlu terminal! |
| 💬 **Typing Indicator** | Animasi "PUTRI sedang mengetik..." untuk pengalaman percakapan yang lebih natural |
| 📝 **Simpan Log Chat** | Export riwayat percakapan ke file `.txt` otomatis dengan timestamp |
| 🔒 **Zero Dependencies** | Hanya menggunakan Python Standard Library (re, tkinter, threading) |
| 📦 **Portable .exe** | Bisa dikompilasi menjadi file `.exe` untuk distribusi tanpa Python |
| 🌐 **Versi HTML** | Alternatif berbasis browser, bisa dibuka langsung tanpa instalasi apapun |

---

## 🗂️ Struktur Proyek

```
putri-chatbot/
│
├── putri.py               # 🧠 Main app — engine chatbot + GUI
├── PUTRI_(2026).ipynb     # 📓 Notebook original — prototype & eksperimen awal
├── build_exe.py           # 🔨 Script build ke .exe
├── requirements.txt       # 📋 Dependencies
├── .gitignore             # 🚫 File yang dikecualikan dari Git
├── README.md              # 📖 Dokumentasi ini
├── putri.html             # 🌐 Aplikasi chatbot versi html
│
├── screenshots/           # 📸 Screenshot antarmuka
│   ├── putri_html.png         # Tampilan versi HTML
│   └── putri_py.png           # Tampilan versi Python/Desktop
│
└── assets/
    └── putri.png          # 🖼️ Ilustrasi karakter PUTRI
```

---

## 🚀 Cara Menjalankan

### Prasyarat
- Python 3.8 atau lebih baru
- Modul `tkinter` (sudah termasuk di instalasi Python standar)

### Jalankan Langsung (Python)
```bash
# Clone repo
git clone https://github.com/whddarmadi/putri-chatbot.git
cd putri-chatbot

# Jalankan aplikasi
python putri.py
```

### Build ke .exe (Windows)
```bash
# Install PyInstaller
pip install pyinstaller

# Jalankan script build
python build_exe.py

# File .exe tersedia di:
# dist/PUTRI.exe
```

> ⚠️ **Catatan Build**: File `.exe` yang dihasilkan bisa langsung dijalankan di Windows **tanpa perlu Python terinstall**. Cocok untuk distribusi ke pengguna umum.

---

## 💬 Contoh Interaksi

```
Kamu : halo putri!
PUTRI: Hai hai! Udah kangen aja nih sama PUTRI ✨

Kamu : nama saya Wahid
PUTRI: Halo Wahid! Salam kenal ya, PUTRI seneng deh ngobrol sama kamu ✨

Kamu : aku merasa capek banget hari ini
PUTRI: Lho, kok bisa kamu ngerasa capek banget hari ini? Coba cerita ke PUTRI pelan-pelan.

Kamu : koding mulu sampai pusing
PUTRI: Ngoding nopo mancing emosi niki? Sing sabar ya ngadepin sintaks error 🥲💻

Kamu : assalamualaikum
PUTRI: Wa'alaikumsalam wr. wb.! Ada yang bisa PUTRI bantu hari ini? 😇

Kamu : put, udah makan belum?
PUTRI: Putri mah makannya listrik! Kalau colokan cabut, ya lapar deh 🔌😂

Kamu : suka cempe ga?
PUTRI: CEMPE!! 🐐💕 Itu binatang paling menggemaskan sedunia! Putri suka banget sama cempe!

Kamu : jancuk!
PUTRI: Hei! Bahasanya dijaga dong! PUTRI ga mau denger kata-kata kayak gitu 😤🚫
```

---

## 🖼️ Tampilan Antarmuka

<div align="center">

| Versi HTML (Browser) | Versi Desktop (Python) |
|:---:|:---:|
| ![HTML Interface](screenshots/putri_html.png) | ![Desktop Interface](screenshots/putri_py.png) |
| Buka langsung di browser | Aplikasi desktop standalone |

</div>

---

## 🏗️ Arsitektur Teknis

### Sistem Aturan (Rule Engine)
```
Input Pengguna
      │
      ▼
[Preprocessing]          → lowercase, strip, normalisasi slang
      │
      ▼
[Pattern Matching]       → iterasi dictionary aturan (Regex)
      │
   Cocok?
   ├─ Ya  → Ekstrak capture groups → Refleksi ke jawaban → Output
   └─ Tidak → Fallback response (jaring pengaman)
```

### Teknik Utama

**1. Refleksi Linguistik (ELIZA Technique)**
```python
r'aku merasa (.*)': [
    'Lho, kok bisa kamu ngerasa {0}?',
    'Sejak kapan kamu merasa {0}? 🥺'
]
# "aku merasa lelah" → "Lho, kok bisa kamu ngerasa lelah?"
```

**2. Preprocessing Slang**
```python
slang_map = {
    r'\byg\b': 'yang',
    r'\bgk\b':  'nggak',
    r'\bntr\b': 'nanti',
    # ...
}
```

**3. Sistem Fallback**
Jika tidak ada pola yang cocok, PUTRI memilih respons fallback secara acak dan mempersonalisasinya jika nama user sudah diketahui dari sesi tersebut.

---

## 📚 Konsep NLP yang Diterapkan

| Konsep | Implementasi di PUTRI |
|---|---|
| **Pattern Matching** | `re.search()` dengan pola Regex pada setiap input |
| **Capture Groups** | `(.*)` dan `\b(kata1\|kata2)\b` untuk ekstraksi teks |
| **Text Normalization** | Lowercase, strip whitespace, normalisasi singkatan slang |
| **Template Response** | `str.format(*groups)` untuk refleksi dinamis |
| **Randomization** | `random.choice()` agar respons tidak monoton |
| **Code-switching** | Deteksi dan respons bilingual ID-Jawa |

---

## 🧑‍💻 Pengembang

**Wahid S. Darmadi**

[![GitHub](https://img.shields.io/badge/GitHub-whddarmadi-181717?style=flat-square&logo=github)](https://github.com/whddarmadi)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-whddarmadi-0A66C2?style=flat-square&logo=linkedin)](https://linkedin.com/in/whddarmadi)
[![Instagram](https://img.shields.io/badge/Instagram-wahwahcreative-E4405F?style=flat-square&logo=instagram)](https://www.instagram.com/wahwahcreative/)

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE).  
Bebas digunakan, dimodifikasi, dan didistribusikan dengan menyertakan atribusi.

---

## 🙏 Referensi & Inspirasi

- Weizenbaum, J. (1966). *ELIZA — A Computer Program for the Study of Natural Language Communication Between Man and Machine.* Communications of the ACM.
- Python Documentation — [`re` module](https://docs.python.org/3/library/re.html)
- Python Documentation — [`tkinter` module](https://docs.python.org/3/library/tkinter.html)

---

<div align="center">
<sub>Dibuat dengan semangat ngulik NLP di Indonesia</sub>
</div>
