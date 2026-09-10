define flash = Fade(.25, 0, .75, color="#fff")
define circleirisout = Fade(.5, 0, .5, color="#000")
define circleirisin = Fade(.5, 0, .5, color="#000")

image bg event 0_80_shake:
    "bg event 0_80" 
    0.15                # Angka ini adalah durasi gambar tampil (0.15 detik). Makin kecil, makin cepat.
    "bg event 0_80_5" with vpunch
    0.15
    repeat

transform geser:
    zoom 1.08
    xalign 0.0
    linear 12.0 xalign 1.0