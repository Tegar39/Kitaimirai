label chapter_2:
    scene bg_mc_room_morning with fade
    play music "audio/morning_ambient.mp3" fadein 2.0

    "{cps=35}Alarm berbunyi tepat pukul 06.00. Cahaya matahari menembus celah gorden, memaksa mataku untuk terbuka.{/cps}"
    "{cps=35}Aku terdiam sejenak, menatap langit-langit kamar. Kejadian kemarin... rasanya seperti mimpi buruk yang terlalu nyata.{/cps}"

    # Visual cue berdasarkan pilihan kemarin
    if milih_club and club_choice == "osis":
        "{cps=35}Di atas meja belajarku, map OSIS itu seolah menatapku balik. Menunggu untuk diisi dengan tanggung jawab.{/cps}"
    elif milih_club and club_choice == "sastra":
        "{cps=35}Aku meraba buku tua pemberian Shoko di samping bantal. Kalimat tentang 'konsekuensi' itu masih terngiang jelas.{/cps}"
    elif masuk_club:
        "{cps=35}Kertas keputusan yang kutulis semalam masih ada di saku seragamku. Rahasia tentang Kakak dan Mama membuat berat di dadaku tak kunjung hilang.{/cps}"
    else:
        "{cps=35}Kamar ini terasa hampa, seperti cerminan dari kebingunganku. Aku belum membuat keputusan apapun tentang klub.{/cps}"
        "{cps=35}Namun hidupku. Aku harus melangkah maju.{/cps}"

    "{cps=35}Aku harus berangkat. Apapun yang terjadi hari ini, aku sudah memilihnya.{/cps}"

    "{cps=40}Aku membuka pintu rumahku{/cps}"
    if milih_club and club_choice == "osis":
        jump chapter_2_osis
    elif milih_club and club_choice == "sastra":
        jump chapter_2_sastra
    elif not milih_club:
        jump chapter_2_kesempatan
    