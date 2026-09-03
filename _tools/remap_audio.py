# -*- coding: utf-8 -*-
"""
Remap_audio.py
--------------
Mengganti semua referensi audio "underscore" yang tidak ada di bab 2
(berupa 'audio/xxx.mp3') menjadi file audio NYATA yang sudah ada,
agar game tidak crash saat memutar suara di bab 2.

Pemetaan dibuat agar semirip mungkin secara semantik dengan aset yang
dibayangkan penulis. Begitu aset asli tersedia, penulis tinggal mengganti
string di file .rpy kembali (atau menaruh file dengan nama yang sama).

Cara pakai:
    python remap_audio.py
"""
import io
import os

BASE = os.path.dirname(os.path.abspath(__file__))
GAME = os.path.normpath(os.path.join(BASE, "..", "game"))

# ---------------------------------------------------------------------------
# PEMETAAN: referensi yang hilang -> file audio yang benar-benar ada
# ---------------------------------------------------------------------------
AUDIO_MAP = {
    # ---------------- BGM (musik latar) ----------------
    "audio/soft_melancholy.mp3":     "audio/bgm/last meet.mp3",
    "audio/maya_theme.mp3":          "audio/bgm/emptyroom.mp3",
    "audio/school_life.mp3":         "audio/bgm/schoolgate.mp3",
    "audio/afternoon_ambient.mp3":   "audio/bgm/evewalk.mp3",
    "audio/office_ambience.mp3":     "audio/bgm/emptyroom.mp3",
    "audio/tension_ambient.mp3":     "audio/bgm/tiptoeing around.mp3",
    "audio/tension_walking.mp3":     "audio/bgm/evewalk.mp3",
    "audio/sad_piano_emotional.mp3": "audio/bgm/last bridge.mp3",
    "audio/mystery_soft.mp3":        "audio/bgm/whisper good.mp3",
    "audio/walking_home_theme.mp3":  "audio/bgm/gohome.mp3",
    "audio/morning_ambient.mp3":     "audio/bgm/opener1.mp3",
    "audio/school_ambience.mp3":     "audio/bgm/schoolgate.mp3",

    # ---------------- SFX (efek suara) ----------------
    "audio/school_bell.mp3":         "audio/sfx/school bell.mp3",
    "audio/school_bell_long.mp3":    "audio/sfx/school bell.mp3",
    "audio/bell_chime_soft.mp3":     "audio/sfx/sfxbell.mp3",
    "audio/shoes_tap.mp3":           "audio/sfx/walk.mp3",
    "audio/shoes_tap_fast.mp3":      "audio/sfx/walk.mp3",
    "audio/steps_light.mp3":         "audio/sfx/walk.mp3",

    "audio/door_open.mp3":           "audio/sfx/door.mp3",
    "audio/door_open_bang.mp3":      "audio/sfx/door.mp3",
    "audio/door_heavy_open.mp3":     "audio/sfx/door.mp3",
    "audio/door_close_echo.mp3":     "audio/sfx/door.mp3",
    "audio/door_rattle.mp3":         "audio/sfx/door.mp3",
    "audio/heavy_door_close.mp3":    "audio/sfx/door.mp3",
    "audio/door_slide.mp3":          "audio/sfx/sliding door.mp3",
    "audio/door_slide_hard.mp3":     "audio/sfx/sliding door.mp3",
    "audio/door_knock.mp3":          "audio/sfx/knock door.mp3",
    "audio/knock_wood.mp3":          "audio/sfx/knock door.mp3",

    "audio/phone_vibrate.mp3":       "audio/sfx/phone notif.mp3",
    "audio/light_switch_on.mp3":     "audio/sfx/lamp.mp3",
    "audio/light_switch_stuck.mp3":  "audio/sfx/lamp.mp3",
    "audio/folder_thud.mp3":         "audio/sfx/jatoh.mp3",
    "audio/box_crash.mp3":           "audio/sfx/jatoh.mp3",
    "audio/trashcan_clatter.mp3":    "audio/sfx/jatoh.mp3",
    "audio/table_bang.mp3":          "audio/sfx/punch.mp3",
    "audio/heavy_breathing.mp3":     "audio/sfx/breathing.mp3",
    "audio/dust_cough.mp3":          "audio/sfx/breathing.mp3",
    "audio/keys_clinking.mp3":       "audio/sfx/cling.mp3",
    "audio/clothing_rustle.mp3":     "audio/sfx/book.mp3",
    "audio/paper_creak.mp3":         "audio/sfx/paper.mp3",
}

# File bab 2 yang akan diproses
TARGET_FILES = [
    "chapter_2_kesempatan.rpy",
    "chapter_2_main.rpy",
    "chapter_2_osis.rpy",
    "chapter_2_sastra.rpy",
    "chapter_2_end.rpy",
]


def main():
    total_replaced = 0
    for fname in TARGET_FILES:
        path = os.path.join(GAME, fname)
        if not os.path.exists(path):
            print(f"[SKIP] {fname} tidak ditemukan")
            continue
        with io.open(path, "r", encoding="utf-8") as fh:
            text = fh.read()

        count = 0
        for old, new in AUDIO_MAP.items():
            # ganti SEMUA kemunculan string persis (dengan tanda kutip di sekitarnya)
            c = text.count('"' + old + '"')
            if c:
                text = text.replace('"' + old + '"', '"' + new + '"')
                count += c

        if count:
            with io.open(path, "w", encoding="utf-8", newline="") as fh:
                fh.write(text)
            total_replaced += count
            print(f"[OK] {fname}: {count} referensi audio diganti")
        else:
            print(f"[--] {fname}: tidak ada referensi yang perlu diganti")

    print(f"\nTotal referensi audio diganti: {total_replaced}")


if __name__ == "__main__":
    main()
