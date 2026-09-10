label chapter_2:
    scene bg_mc_room_morning with fade
    play music "audio/bgm/opener1.mp3" fadein 2.0

    "{cps=35}The alarm rang exactly at 6:00. Sunlight slipped through the gap in the curtains, forcing my eyes open.{/cps}"
    "{cps=35}I lay still for a moment, staring at the ceiling. Yesterday's events... felt like a nightmare that was far too real.{/cps}"

    # Visual cue based on yesterday's choice
    if milih_club and club_choice == "osis":
        "{cps=35}On my study desk, the Student Council folder seemed to stare back at me. Waiting to be filled with responsibility.{/cps}"
    elif milih_club and club_choice == "sastra":
        "{cps=35}I touched the old book Shoko had given me, still lying beside my pillow. The line about 'consequences' still echoed clearly in my mind.{/cps}"
    elif masuk_club:
        "{cps=35}The decision paper I wrote last night was still in my uniform pocket. The secrets about my older sister and Mom made the weight in my chest refuse to fade.{/cps}"
    else:
        "{cps=35}The room felt empty, a reflection of my own confusion. I still hadn't made any decision about a club.{/cps}"
        "{cps=35}But this is my life. I have to move forward.{/cps}"

    "{cps=35}I have to leave. Whatever happens today, I've already made my choice.{/cps}"

    "{cps=40}I opened the door of my house.{/cps}"
    if milih_club and club_choice == "osis":
        jump chapter_2_osis
    elif milih_club and club_choice == "sastra":
        jump chapter_2_sastra
    elif not milih_club:
        jump chapter_2_kesempatan
