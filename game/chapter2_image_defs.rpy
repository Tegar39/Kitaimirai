# =============================================================================
#  chapter2_image_defs.rpy
# =============================================================================
#  JEMBATAN ASET SEMENTARA UNTUK BAB 2
# -----------------------------------------------------------------------------
#  File ini mendefinisikan semua image "underscore" (mis. yuuka_smile,
#  bg_classroom, dst.) yang dipakai oleh bab 2 tetapi aset aslinya BELUM ADA
#  di folder game/images/ (folder "chapter 2 osis", "chapter 2 sastra",
#  "chapter 2 solo" masih kosong).
#
#  Semua definisi di bawah ini MENGALIASKAN ke aset yang sudah ada agar game
#  TIDAK CRASH saat bab 2 dimainkan. Begitu aset asli bab 2 sudah dibuat oleh
#  penulis, cukup:
#    1) Letakkan file aslinya di game/images/ (sesuaikan nama file),
#    2) Hapus/hapus-komentari baris alias yang bersangkutan di file ini,
#    3) Atau ganti baris `image nama = "..."` dengan nama file asli.
#
#  File ini AMAN dihapus sewaktu-waktu setelah aset asli tersedia.
# =============================================================================

# -----------------------------------------------------------------------------
# SPRITE — Yuuka
# -----------------------------------------------------------------------------
image yuuka_neutral    = "images/Yuuka/yuuka s00.png"
image yuuka_smile      = "images/Yuuka/yuuka s01.png"
image yuuka_determined = "images/Yuuka/yuuka s03.png"
image yuuka_stern      = "images/Yuuka/yuuka s05.png"
image yuuka_sad        = "images/Yuuka/yuuka s08.png"
image yuuka_blush      = "images/Yuuka/yuuka s13.png"

# -----------------------------------------------------------------------------
# SPRITE — Vina
# -----------------------------------------------------------------------------
image vina_smile = "images/Vina/vina s01.png"

# -----------------------------------------------------------------------------
# SPRITE — Maya
# -----------------------------------------------------------------------------
image maya_neutral  = "images/Maya/maya s00.png"
image maya_shocked  = "images/Maya/maya s03.png"
image maya_stern    = "images/Maya/maya s04.png"

# -----------------------------------------------------------------------------
# SPRITE — Shoko
# -----------------------------------------------------------------------------
image shoko_neutral = "images/Shoko/shoko s00.png"
image shoko_smile   = "images/Shoko/shoko s01.png"
image shoko_blush   = "images/Shoko/shoko s02.png"

# -----------------------------------------------------------------------------
# SPRITE — Yukie
# -----------------------------------------------------------------------------
image yukie_smile = "images/Yukie/yukie s01.png"

# -----------------------------------------------------------------------------
# SPRITE — Nanami Sensei (guru)
# -----------------------------------------------------------------------------
image teacher_t_serious = "images/Nanami Sensei/nanami s01.png"

# -----------------------------------------------------------------------------
# SPRITE — Abby
# -----------------------------------------------------------------------------
image abby_stern = "images/Abby/CharaStudio-2026-06-27-23-37-02-Render.png"

# -----------------------------------------------------------------------------
# BACKGROUND — Rumah / Kamar
# -----------------------------------------------------------------------------
image bg_front_house_morning = "images/background/bg yuukahomemorn.webp"
image bg_mc_room_morning     = "images/background/bg kamarmorning.webp"

# -----------------------------------------------------------------------------
# BACKGROUND — Sekolah & Kelas
# -----------------------------------------------------------------------------
image bg_classroom            = "images/background/bg classroom2.webp"
image bg_classroom_morning    = "images/background/bg classmorn.webp"
image bg_classroom_sunset     = "images/background/bg classroom2eve.webp"
image bg_school_gate          = "images/background/bg roadmorning.webp"
image bg_school_gate_night    = "images/background/bg roadeve.webp"

# -----------------------------------------------------------------------------
# BACKGROUND — Koridor
# -----------------------------------------------------------------------------
image bg_school_corridor           = "images/background/bg lorong3.webp"
image bg_school_corridor_afternoon = "images/background/bg lorong3 sore.webp"
image bg_school_corridor_sunset    = "images/background/bg lorong2.webp"
image bg_school_corridor_night     = "images/background/bg lorongkosong.webp"
image bg_club_corridor             = "images/background/bg lorong.webp"

# -----------------------------------------------------------------------------
# BACKGROUND — Ruang OSIS / Studio Klub (reuse ruang OSIS bab 1)
# -----------------------------------------------------------------------------
image bg_council_room_sunset    = "images/chapter 1/bg event 1_330.webp"
image bg_council_room_interior  = "images/chapter 1/bg event 1_330.webp"
image bg_lit_club_room          = "images/chapter 1/bg event 1_331.webp"
image bg_event_flashback        = "images/chapter 0/bg event 0_80.webp"

# -----------------------------------------------------------------------------
# BACKGROUND — Ruang lain (placeholder terdekat)
# -----------------------------------------------------------------------------
image bg_warehouse_dark     = "images/chapter 0/bg event 0_80.webp"
image bg_stairs_to_rooftop  = "images/background/bg lorong.webp"
image bg_rooftop_morning    = "images/background/bg courtyardmorning.webp"
image bg_storage_room_dark  = "images/chapter 0/bg event 0_80.webp"
image bg_storage_room_bright= "images/background/bg courtyardmorning.webp"

# -----------------------------------------------------------------------------
# LAIN-LAIN
# -----------------------------------------------------------------------------
# Ren'Py tidak otomatis menyediakan image "white" (hanya "black").
image white = Solid("#ffffff")
