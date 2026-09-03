# -- Definisi Karakter --
default persistent.textbox_alpha = 1.0
define mc = Character("[mc_name]",what_prefix="「", what_suffix="」", color="#efefef")
define mom = Character("Mama",what_prefix="「", what_suffix="」", color="#ffffff")
define y = Character("Yuuka",what_prefix="「", what_suffix="」", color="#ffffff")
define m = Character("Maya",what_prefix="「", what_suffix="」", color="#ffffff")
define v = Character("Vina",what_prefix="「", what_suffix="」", color="#ffffff")
define sh = Character("Shoko",what_prefix="「", what_suffix="」", color="#ffffff")
define yk = Character("Yukie",what_prefix="「", what_suffix="」", color="#ffffff")
define t = Character("Nanami Sensei",what_prefix="「", what_suffix="」", color="#ffffff")
define host = Character("Pembawa Acara",what_prefix="「", what_suffix="」", color="#ffffff")
define p = Character("Panitia",what_prefix="「", what_suffix="」", color="#efefef")
define g1 = Character("Gadis",what_prefix="「", what_suffix="」", color="#efefef")
define g2 = Character("Gadis",what_prefix="「", what_suffix="」", color="#efefef")
define g4 = Character("Gadis",what_prefix="「", what_suffix="」", color="#efefef")
define g5 = Character("Gadis",what_prefix="「", what_suffix="」", color="#efefef")
define mrd = Character("Teman Sekelas",what_prefix="「", what_suffix="」", color="#efefef")
define guru = Character("Guru",what_prefix="「", what_suffix="」", color="#efefef")
define ayah = Character("Ayah",what_prefix="「", what_suffix="」", color="#efefef")
define mi = Character("Megumi",what_prefix="「", what_suffix="」", color="#efefef")
define unknown = Character("Suara Misterius",what_prefix="「", what_suffix="」", color="#efefef")
define f = Character("Fumi",what_prefix="「", what_suffix="」", color="#efefef")
define sz = Character("Shizu",what_prefix="「", what_suffix="」", color="#efefef")
define sa = Character("Sayoko",what_prefix="「", what_suffix="」", color="#efefef")
define ri = Character("Rina",what_prefix="「", what_suffix="」", color="#efefef")
define yu = Character("Yuki",what_prefix="「", what_suffix="」", color="#efefef")
define ab = Character("Abby",what_prefix="「", what_suffix="」", color="#efefef")
define ry = Character("Ryuu",what_prefix="「", what_suffix="」", color="#efefef")

default yuuka_rel = 0
default maya_rel = 0 
default vina_rel = 0
default shoko_rel = 0
default yukie_rel = 0
default fumi_rel = 0
default abby_rel = 0
default ryuu_rel = 0
image bg_lorong = Movie(play="movies/lorong.webm", loop=True, size=(1920, 1080))
transform sedikit_blur:
    blur 5
# -- Variabel Plot & Flags (PENTING: Agar Chapter 1 & 2 tidak error) --
default club_choice = None 
default milih_club = False
default masuk_club = False
default jajan = False      # Flag untuk rute kantin
default ciduk = False      # Flag untuk rute ketahuan Maya
default guess_correct = False # Flag untuk tebak Yukie/Shoko
default jujur = False      # Flag untuk pilihan jujur ke Yuuka
default silent = False
default correct_answer = False
default correct_answer_2 = False
default pasang = False     # Flag untuk pilihan diam (gunakan huruf kecil semua)
default spots_searched = 0
default check_rak = False
default check_meja = False
default check_peti = False
default tebak = False
default trobos = False
default apatis = False
default tell_yuuka = False
default callyuukafirst = False 

transform scroll_left:
    xpan -180          # mulai dari posisi kiri gambar
    linear 30.0 xpan 180  # geser ke kanan selama 10 detik
    repeat    

transform hallway_walk:
    zoom 1.45
    xalign 0.5
    yalign 0.5

    parallel:
        linear 12.0 zoom 1.58

    parallel:
        block:
            ease 0.30 yoffset -6
            ease 0.30 yoffset 4
            repeat

    parallel:
        block:
            ease 0.70 xoffset -3
            ease 0.70 xoffset 3
            repeat


transform hallway_idle:
    zoom 1.50
    xalign 0.5
    yalign 0.5
    xoffset 0
    yoffset 0


transform maya_walk_front:
    xalign 0.5
    yalign 1.0
    yoffset 10

    parallel:
        block:
            ease 0.35 yoffset 0
            ease 0.35 yoffset 10
            repeat

    parallel:
        block:
            ease 0.60 xoffset -4
            ease 0.60 xoffset 4
            repeat


transform maya_stop_front:
    xalign 0.5
    yalign 1.0
    xoffset 0
    yoffset 0

transform pan_up:
    zoom 1.3
    yalign 1.0
    xalign 0.5
    linear 5.0 yalign 0.8 


label start:
    "{cps=60}Game ini dibuat dengan Koikatsu Studio dan Ren'Py{/cps}"
    "{cps=60}Selamat bermain!{/cps}"
    
    python:
        mc_name = renpy.input("Enter your name:", default="Ren")
        mc_name = mc_name.strip() or "Ren"
    jump prolog



