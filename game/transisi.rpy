define flash = Fade(.25, 0, .75, color="#fff")

image bg event 0_80_shake:
    "bg event 0_80" 
    0.2                
    "bg event 0_80_5" with vpunch
    0.2
    repeat

transform geser:
    zoom 1.08
    xalign 0.0
    linear 12.0 xalign 1.0