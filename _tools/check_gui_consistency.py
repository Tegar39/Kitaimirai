# -*- coding: utf-8 -*-
"""
check_gui_consistency.py
------------------------
Memeriksa konsistensi antara screens.rpy dan gui.rpy:
  - Semua variabel gui.* yang dipakai di screens.rpy harus DEFINED di gui.rpy
    (atau merupakan properti bawaan gui seperti gui.scale / gui.text_properties).
  - Melaporkan gui.* yang dipakai tapi tidak didefinisikan.
Cara pakai: python check_gui_consistency.py
"""
import io, os, re

BASE = os.path.dirname(os.path.abspath(__file__))
GAME = os.path.normpath(os.path.join(BASE, "..", "game"))

def read(name):
    p = os.path.join(GAME, name)
    with io.open(p, "r", encoding="utf-8") as f:
        return f.read()

screens = read("screens.rpy")
gui = read("gui.rpy")

# 1) Semua gui.X yang dirujuk di screens.rpy
ref_guis = set(re.findall(r"\bgui\.([A-Za-z_][A-Za-z0-9_]*)", screens))
# Fungsi/properti bawaan gui yang TIDAK berupa variabel (jangan dianggap error)
builtin_funcs = {
    "init", "variant", "scale", "rebuild", "preference", "SetPreference",
    "text_properties", "button_properties", "bar_properties",
}
# Variabel yang didefinisikan di gui.rpy
defined_guis = set(re.findall(r"\bgui\.([A-Za-z_][A-Za-z0-9_]*)\s*=", gui))

missing = (ref_guis - defined_guis) - builtin_funcs

print("gui.* yang dipakai di screens.rpy:", len(ref_guis))
print("gui.* yang didefinisikan di gui.rpy:", len(defined_guis))
if missing:
    print("\n[MASALAH] gui.* DIPAKAI tapi TIDAK didefinisikan:")
    for m in sorted(missing):
        print("   - gui." + m)
else:
    print("\n[OK] Semua gui.* yang dipakai sudah didefinisikan (atau built-in).")

# 2) Periksa apakah ada define gui.* yang tidak pernah dipakai (tidak wajib, info saja)
used_or_builtin = ref_guis
unused = defined_guis - used_or_builtin
if unused:
    print("\n[INFO] gui.* didefinisikan tapi tidak dipakai di screens.rpy (kemungkinan dipakai layout lain):")
    for u in sorted(unused):
        print("   - gui." + u)
