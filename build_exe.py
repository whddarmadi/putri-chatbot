"""
build_exe.py — Script untuk compile PUTRI menjadi .exe
Jalankan: python build_exe.py

Requirements: pip install pyinstaller
"""

import subprocess
import sys
import os

def build():
    print("=" * 55)
    print("  🌸 PUTRI — Build .exe Script")
    print("  Menggunakan PyInstaller")
    print("=" * 55)

    # Cek PyInstaller
    try:
        import PyInstaller
        print(f"✅ PyInstaller ditemukan: {PyInstaller.__version__}")
    except ImportError:
        print("❌ PyInstaller belum terinstall.")
        print("   Jalankan: pip install pyinstaller")
        sys.exit(1)

    # Command build
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--onefile",                        # satu file .exe
        "--windowed",                       # tanpa console window
        "--name=PUTRI",                     # nama output
        "--add-data=assets;assets",         # sertakan folder assets (Windows: titik koma)
    ]

    # Tambahkan ikon jika ada
    if os.path.exists("assets/icon.ico"):
        cmd += ["--icon=assets/icon.ico"]

    cmd.append("putri.py")

    print("\n🔨 Memulai build...")
    print(f"   Perintah: {' '.join(cmd)}\n")

    result = subprocess.run(cmd, capture_output=False)

    if result.returncode == 0:
        print("\n" + "=" * 55)
        print("  ✅ Build berhasil!")
        print("  📁 File .exe ada di folder: dist/PUTRI.exe")
        print("=" * 55)
    else:
        print("\n" + "=" * 55)
        print("  ❌ Build gagal. Cek pesan error di atas.")
        print("=" * 55)
        sys.exit(1)

if __name__ == "__main__":
    build()
